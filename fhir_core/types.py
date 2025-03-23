from __future__ import annotations as _annotations

import abc
import dataclasses
import datetime
import decimal
import logging
import re
import typing
from functools import lru_cache

import typing_extensions
from annotated_types import SLOTS, BaseMetadata, Ge, GroupedMetadata, Le, MaxLen, MinLen
from pydantic import AnyUrl, Base64Bytes, GetCoreSchemaHandler
from pydantic._internal._fields import pydantic_general_metadata
from pydantic._internal._validators import import_string
from pydantic.types import UUID4
from pydantic_core import InitErrorDetails, PydanticCustomError
from pydantic_core import Url as PydanticUrl
from pydantic_core import ValidationError, core_schema
from pydantic_core.core_schema import ValidationInfo
from typing_extensions import Annotated

from .constraints import (
    FHIR_PRIMITIVES,
    FHIR_PRIMITIVES_MAPS,
    FHIR_TYPES_MAPS,
    TYPES_ID_MAX_LENGTH,
    TYPES_STRING_ALLOW_EMPTY_STR,
)
from .fhirabstractmodel import FHIRAbstractModel

__author__ = "Md Nazrul Islam"
__email__ = "email2nazrul@gmail.com"

FHIR_DATE_PARTS = re.compile(r"(?P<year>\d{4})(-(?P<month>\d{2}))?(-(?P<day>\d{2}))?$")
LOGGER = logging.getLogger(__name__)


class FhirBase(metaclass=abc.ABCMeta):
    """The base type aka validator for FHIR resource model.

    ```py
    from fhir.resources.core.fhirabstractmodel import FHIRAbstractModel
    from fhir.resources.core.types import create_fhirabstractmodel
    from pydantic import Field

    class Patient(FHIRAbstractModel):
        __resource_type__ = "Patient"
        name: str = Field(..., title="Patient name")

    PatientType = create_fhir_type('PatientType', 'fhir.resources.patient.Patient')

    class CarePlan(FHIRAbstractModel):
        __resource_type__ = "CarePlan"
        subject: PatientType = Field(..., title="Patient")

    care_plan = CarePlan(subject={'name': 'Petter paddle'})
    print(care_plan)
    #>  subject=Patient(name='Petter paddle')
    ```
    """

    if typing.TYPE_CHECKING:
        _model_klass: str
    else:
        __slots__ = ("_model_klass",)

    @classmethod
    @lru_cache(typed=True)
    def get_model_klass(cls) -> typing.Type[FHIRAbstractModel]:
        """ """
        return import_string(cls._model_klass)

    @classmethod
    @lru_cache(typed=True)
    def produce_inner_schema(
        cls, source_type: typing.Any, handler: GetCoreSchemaHandler
    ) -> typing.Optional[core_schema.CoreSchema]:
        if isinstance(source_type, cls):
            # @TODO: find the best way to generate schema from actual class!
            schema = handler.generate_schema(FHIRAbstractModel)
            return schema
        if typing.get_origin(source_type) is not None:
            for tp in typing.get_args(source_type):
                inner_schema = cls.produce_inner_schema(tp, handler)
                if inner_schema:
                    return inner_schema
        return None

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: typing.Type["FhirBase"], handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        """
        Return a Pydantic CoreSchema with the FHIR resource validation.

        Args:
            source_type: The source type to be converted.
            handler: The handler to get the CoreSchema.

        Returns:
            A Pydantic CoreSchema with the FHIR resource validation.

        """
        inner_schema = cls.produce_inner_schema(source_type, handler)  # type: ignore
        if inner_schema is None:
            # show warning log
            inner_schema = core_schema.any_schema()

        def serialize(
            value: typing.Any, info: core_schema.SerializationInfo
        ) -> typing.Dict[str, typing.Any]:
            if typing.TYPE_CHECKING:
                value = typing.cast(FHIRAbstractModel, value)
            if info.mode == "json":
                # todo: what would be differences?
                return value.model_dump()
            else:
                return value.model_dump()

        def _validate(
            input_value: typing.Union[str, bytes, dict, FHIRAbstractModel],
            validator: typing.Callable[[FHIRAbstractModel], typing.Any],
            validation_info: ValidationInfo,
        ) -> FHIRAbstractModel:
            """
            Validate a FHIR resource from the provided value of str or dict or FHIR resource itself.

            Args:
                input_value: The str or dict or FHIR resource value to be validated.
                validator: The source type to be converted.
                validation_info: Validation info.

            Returns:
                FHIRAbstractModel: The parsed FHIR resource.

            """
            model_klass = source_type.get_model_klass()
            if typing.TYPE_CHECKING:
                model_klass = typing.cast(typing.Type[FHIRAbstractModel], model_klass)
            return validator(cls.fhir_model_validator(input_value, model_klass))

        return core_schema.with_info_wrap_validator_function(
            _validate,
            inner_schema,
            serialization=core_schema.plain_serializer_function_ser_schema(
                serialize,
                info_arg=True,
                when_used="always",
            ),
        )

    @classmethod
    def fhir_model_validator(
        cls,
        value: typing.Union[str, bytes, dict, FHIRAbstractModel],
        model_klass: typing.Type[FHIRAbstractModel],
    ):
        if value is None:
            LOGGER.debug("None value is provided for %s", model_klass)
            return value

        if isinstance(value, (str, bytes)):
            value = model_klass.model_validate_json(value)

        elif isinstance(value, dict):
            value = model_klass.model_validate(value)

        errors: typing.List[InitErrorDetails] = list()
        if typing.TYPE_CHECKING:
            error_: InitErrorDetails

        if not isinstance(value, model_klass):
            error_type = PydanticCustomError(
                "model_validation_format",
                "Value is expected from the instance of {model_class}, but got type {type}",
                {"model_class": model_klass.__name__, "type": type(value)},
            )
            error_ = {
                "type": error_type,
                "loc": ("root",),
                "input": value,
            }
            errors.append(error_)

        if len(errors) == 0:
            if model_klass.__resource_type__ != value.__resource_type__:
                error_type = PydanticCustomError(
                    "model_validation_format",
                    'Expected resource_type is "{model_name}", but value has resource_type "{resource_type}"',
                    {
                        "model_name": model_klass.__resource_type__,
                        "resource_type": value.__resource_type__,
                    },
                )
                error_ = {
                    "type": error_type,
                    "loc": ("root",),
                    "input": value,
                }
                errors.append(error_)
        if len(errors) > 0:
            raise ValidationError.from_exception_data(cls.__name__, errors)
        else:
            del errors

        return value

    def __hash__(self) -> int:
        return hash(self._model_klass)


class FhirElementOrResourceBase(FhirBase):
    """Special type of validator for FHIR Resource & Element model.
    There are many cases that value type is declared as ResourceType
    but expect any of FHIR resource that derived from Base Resource.
    Fx. domainresource.DomainResource.contained: typing.List[fhirtypes.ResourceType]
    """

    @classmethod
    def fhir_model_validator(
        cls,
        value: typing.Union[str, bytes, dict, FHIRAbstractModel],
        model_klass: typing.Type[FHIRAbstractModel],
    ):

        _model_klass = model_klass
        if isinstance(value, FHIRAbstractModel):
            _model_klass = value.__class__
        elif isinstance(value, dict) and "resourceType" in value:
            _model_klass = import_string(
                FHIR_TYPES_MAPS[value["resourceType"] + "Type"]
            )
        elif isinstance(value, (str, bytes)):
            # @TODO: need to parse json?
            pass

        errors: typing.List[InitErrorDetails] = list()
        if typing.TYPE_CHECKING:
            error_: InitErrorDetails

        if model_klass.__name__ == "Resource":
            if not _model_klass.has_resource_base():
                error_type = PydanticCustomError(
                    "model_validation_format",
                    "Provided FHIR resource {model_class} should be derived from / based on Resource.",
                    {"model_class": _model_klass.__name__},
                )
                error_ = {
                    "type": error_type,
                    "loc": ("root",),
                    "input": _model_klass,
                }
                errors.append(error_)

        elif model_klass.__name__ == "Element":
            if _model_klass.has_resource_base():
                error_type = PydanticCustomError(
                    "model_validation_format",
                    "Provided FHIR resource {model_class} should be derived from / based on Element.",
                    {"model_class": _model_klass.__name__},
                )
                error_ = {
                    "type": error_type,
                    "loc": ("root",),
                    "input": _model_klass,
                }
                errors.append(error_)
        else:
            error_type = PydanticCustomError(
                "model_validation_format",
                "Only Element or Resource model is allowed to use this validator.",
                {},
            )
            error_ = {
                "type": error_type,
                "loc": ("root",),
                "input": model_klass,
            }
            errors.append(error_)

        if len(errors) > 0:
            raise ValidationError.from_exception_data(cls.__name__, errors)
        else:
            del errors

        return FhirBase.fhir_model_validator(value, _model_klass)


@dataclasses.dataclass(frozen=True, **SLOTS)
class String(GroupedMetadata):
    """A sequence of Unicode characters	xs:string	JSON String
    Note that strings SHALL NOT exceed 1,048,576 (1024*1024) characters in size.
    Because UTF-8 characters can be expressed with more than one byte, the string size may be more than 1MB.
    Strings SHOULD not contain Unicode character points below 32, except for u0009 (horizontal tab),
    u000D (carriage return) and u000A (line feed). Leading and Trailing whitespace is allowed, but SHOULD be
    removed when using the XML format. Note: This means that a string that consists only of whitespace could
    be trimmed to nothing, which would be treated as an invalid element value. Therefore strings SHOULD always
    contain non-whitespace content
    This datatype can be bound to a ValueSet
    Regex: ^[\\s\\S]+$ (see notes below)

    ```py
    from pydantic import BaseModel
    from typing_extension import Annotated
    from fhir_core.types import String

    StringType = Annotated[str, String(allow_empty_str=False)]

    class StringModel(BaseModel):
        myString: StringType = None
    model = StringModel(myString='My string')
    print(model.myString)
    #> My string
    ```
    """

    allow_empty_str = TYPES_STRING_ALLOW_EMPTY_STR
    __visit_name__ = "string"

    def __iter__(self) -> typing.Iterator[BaseMetadata]:
        """ """
        regex = "[ \r\n\t\\S]+"
        if self.allow_empty_str:
            # note: there is limitation for empty string match regex, fx new line (\n) will be matched.
            regex = "(" + regex + ")|(^$)"
        yield pydantic_general_metadata(pattern=regex)


@dataclasses.dataclass(frozen=True, **SLOTS)
class Base64Binary:
    """A stream of bytes, base64 encoded (RFC 4648 )
    Just a symbolic class, no need to further check with regex as value is already decoded.
    """

    __visit_name__ = "base64Binary"
    regex = r"^(\s*([0-9a-zA-Z+=]){4}\s*)+$"

    def __hash__(self) -> int:
        """ """
        return hash(self.__class__)


@dataclasses.dataclass(frozen=True, **SLOTS)
class Code(GroupedMetadata):
    """Indicates that the value is taken from a set of controlled
    strings defined elsewhere (see Using codes for further discussion).
    Technically, a code is restricted to a string which has at least one
    character and no leading or trailing whitespace, and where there is
    no whitespace other than single spaces in the contents"""

    __visit_name__ = "code"

    def __iter__(self) -> typing.Iterator[BaseMetadata]:
        """ """
        regex = r"^[^\s]+(\s[^\s]+)*$"
        yield pydantic_general_metadata(pattern=regex)

    def __hash__(self) -> int:
        return hash(self.__class__)


@dataclasses.dataclass(frozen=True, **SLOTS)
class Id(GroupedMetadata):
    """Any combination of upper- or lower-case ASCII letters
    ('A'..'Z', and 'a'..'z', numerals ('0'..'9'), '-' and '.',
    with a length limit of 64 characters.
    (This might be an integer, an un-prefixed OID, UUID or any other identifier
    pattern that meets these constraints.)

    But it is possible to change the default behaviour by patching constraint.TYPES_ID_MAX_LENGTH value!

    There are a lots of discussion about ``Resource.Id`` length of value.
        1. https://bit.ly/360HksL
        2. https://bit.ly/3o1fZgl
    We see there is some agreement and disagreement, because of that we decide to make
    it more flexible. Now it is possible configure three types of constraints.
    """

    pattern = r"^[A-Za-z0-9\-.]+$"
    min_length = 1
    max_length = TYPES_ID_MAX_LENGTH
    __visit_name__ = "id"

    def __iter__(self) -> typing.Iterator[BaseMetadata]:
        """ """
        if self.min_length is not None:
            yield MinLen(self.min_length)
        if self.max_length is not None:
            yield MaxLen(self.max_length)
        if self.pattern:
            yield pydantic_general_metadata(pattern=self.pattern)


@dataclasses.dataclass(**SLOTS)
class Decimal:
    """Rational numbers that have a decimal representation.
    See below about the precision of the number"""

    pattern = re.compile(r"^-?(0|[1-9][0-9]*)(\.[0-9]+)?([eE][+-]?[0-9]+)?$")
    __visit_name__ = "decimal"

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: typing.Type["Decimal"], handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        """
        Return a Pydantic CoreSchema with Decimal validation.

        Args:
            source_type: The source type to be converted.
            handler: The handler to get the CoreSchema.

        Returns:
            A Pydantic CoreSchema with Decimal.

        """

        def _serialize(
            value: typing.Union[str],
            info: core_schema.SerializationInfo,
        ) -> typing.Union[float]:
            """Encodes a Decimal as float."""
            return float(value)

        def _validate(
            input_value: decimal.Decimal,
            validator: typing.Callable[
                [typing.Union[str, decimal.Decimal]], typing.Any
            ],
            validation_info: ValidationInfo,
        ) -> decimal.Decimal:
            """
            Validate a decimal value.

            Args:
                input_value: The Decimal value to be validated.
            Returns:
                Decimal

            """
            if not cls.pattern.match(str(input_value)):
                raise ValueError

            return decimal.Decimal(input_value)

        return core_schema.with_info_wrap_validator_function(
            _validate,
            core_schema.decimal_schema(),
            serialization=core_schema.plain_serializer_function_ser_schema(
                _serialize,
                info_arg=True,
                when_used="always",
                return_schema=core_schema.decimal_schema(),
            ),
        )

    def __hash__(self) -> int:
        return hash(self.__class__)


@dataclasses.dataclass(frozen=True, **SLOTS)
class Integer(GroupedMetadata):
    """A signed integer in the range −2,147,483,648..2,147,483,647 (32-bit;
    for larger values, use decimal)"""

    pattern = re.compile(r"^[0]|[-+]?[1-9][0-9]*$")
    min_length: int = -2147483648
    max_length: int = 2147483647

    __visit_name__ = "integer"

    def __iter__(self) -> typing.Iterator[BaseMetadata]:
        """ """
        yield Le(self.max_length)

        yield Ge(self.min_length)


class Integer64(GroupedMetadata):
    """A signed integer in the range
    -9,223,372,036,854,775,808 to +9,223,372,036,854,775,807 (64-bit).
    This type is defined to allow for record/time counters that can get very large"""

    pattern = re.compile(r"^[0]|[-+]?[1-9][0-9]*$")

    min_length: int = -9223372036854775807
    max_length: int = 9223372036854775807
    __visit_name__ = "integer64"

    def __iter__(self) -> typing.Iterator[BaseMetadata]:
        """ """
        yield Le(self.max_length)

        yield Ge(self.min_length)


class UnsignedInt(Integer):
    """Any non-negative integer in the range 0..2,147,483,647"""

    regex = re.compile(r"^[0]|([1-9][0-9]*)$")
    __visit_name__ = "unsignedInt"
    min_length = 0


class PositiveInt(UnsignedInt):
    """Any positive integer in the range 1..2,147,483,647"""

    regex = re.compile(r"^\+?[1-9][0-9]*$")
    __visit_name__ = "positiveInt"
    min_length = 1


@dataclasses.dataclass(frozen=True, **SLOTS)
class PatternConstraint(GroupedMetadata):
    if typing.TYPE_CHECKING:
        pattern: re.Pattern

    def __iter__(self) -> typing.Iterator[BaseMetadata]:
        """ """
        yield pydantic_general_metadata(pattern=self.pattern.pattern)


class Uri(PatternConstraint):
    """A Uniform Resource Identifier Reference (RFC 3986 ).
    Note: URIs are case sensitive.
    For UUID (urn:uuid:53fefa32-fcbb-4ff8-8a92-55ee120877b7)
    use all lowercase xs:anyURI A JSON string - a URI
    Regex: \\S* (This regex is very permissive, but URIs must be valid.
    Implementers are welcome to use more specific regex statements
    for a URI in specific contexts)
    URIs can be absolute or relative, and may have an optional fragment identifier
    This data type can be bound to a ValueSet"""

    __visit_name__ = "uri"
    pattern = re.compile(r"\S*")


class Oid(PatternConstraint):
    """An OID represented as a URI (RFC 3001 ); e.g. urn:oid:1.2.3.4.5"""

    __visit_name__ = "oid"
    pattern = re.compile(r"^urn:oid:[0-2](\.(0|[1-9][0-9]*))+$")


class Uuid:
    """A UUID (aka GUID) represented as a URI (RFC 4122 );
    e.g. urn:uuid:c757873d-ec9a-4326-a141-556f43239520"""

    __visit_name__ = "uuid"


class Canonical(Uri):
    """A URI that refers to a resource by its canonical URL (resources with a url property).
    The canonical type differs from a uri in that it has special meaning in this specification,
    and in that it may have a version appended, separated by a vertical bar (|).
    Note that the type canonical is not used for the actual canonical URLs that are
    the target of these references, but for the URIs that refer to them, and may have
    the version suffix in them. Like other URIs, elements of type canonical may also have
    #fragment references"""

    __visit_name__ = "canonical"


@dataclasses.dataclass(frozen=True, **SLOTS)
class Url:
    """A Uniform Resource Locator (RFC 1738 ).
    Note URLs are accessed directly using the specified protocol.
    Common URL protocols are http{s}:, ftp:, mailto: and mllp:,
    though many others are defined"""

    path_pattern = re.compile(r"^/(?P<resourceType>[^\s?/]+)(/[^\s?/]+)*")
    __visit_name__ = "url"

    @classmethod
    @lru_cache(typed=True)
    def produce_inner_schema(
        cls, source_type: typing.Any, handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema | None:
        if source_type is str:
            return core_schema.str_schema()
        if source_type is PydanticUrl:
            return core_schema.url_schema()
        if typing.get_origin(source_type) is not None:
            for tp in typing.get_args(source_type):
                inner_schema = cls.produce_inner_schema(tp, handler)
                if inner_schema:
                    return inner_schema
        return None

    @classmethod
    def _validate_url(  # type: ignore
        cls,
        input_value: typing.Union[str, PydanticUrl],
        validator: typing.Callable[[typing.Union[str, PydanticUrl]], typing.Any],
    ) -> typing.Union[str, PydanticUrl]:
        """ """
        # todo: check with 'mailto:', 'mllp:', 'llp:'
        # todo: validate email?
        # if input_value.startswith("mailto:"):
        #    schema = input_value[0:7]
        #    email = input_value[7:]
        #    realname = parseaddr(email)[0]
        #    name, email = validate_email(email)
        #    if realname:
        #        email = formataddr((name, email))
        #    return schema + email
        if isinstance(input_value, PydanticUrl):
            return input_value

        if input_value in FHIR_PRIMITIVES:
            # Extensions may contain a valueUrl for a primitive FHIR type
            # no further validation
            return input_value

        try:
            return validator(input_value)
        except ValidationError as exc:
            # we are allowing relative path
            if not input_value.startswith("/"):
                matched = cls.path_pattern.match("/" + input_value)
            else:
                matched = cls.path_pattern.match(input_value)
            if matched is not None:
                if re.match(
                    r"^[A-Za-z0-9\-.#]+$", matched.groupdict().get("resourceType", "")
                ):
                    # @ToDo: required resource type validation?
                    return input_value
            raise

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: typing.Any, handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        """
        Return a Pydantic CoreSchema with the url validation.

        Args:
            source_type: The source type to be converted.
            handler: The handler to get the CoreSchema.

        Returns:
            A Pydantic CoreSchema with the url validation.

        """
        inner_schema = cls.produce_inner_schema(source_type, handler)

        def _validate(
            input_value: typing.Union[str, PydanticUrl],
            validator: typing.Callable[[typing.Union[str, PydanticUrl]], typing.Any],
            validation_info: ValidationInfo,
        ) -> typing.Union[str, PydanticUrl]:
            """
            Validate a URL from the provided str value.

            Args:
                input_value: The Decimal value to be validated.
            Returns:
                URL or str

            """
            if isinstance(input_value, PydanticUrl):
                return validator(input_value)
            return cls._validate_url(input_value, validator)

        if typing.TYPE_CHECKING:
            assert inner_schema
        return core_schema.with_info_wrap_validator_function(
            _validate,
            inner_schema,
        )


class Markdown(PatternConstraint):
    """A FHIR string (see above) that may contain markdown syntax for optional processing
    by a markdown presentation engine, in the GFM extension of CommonMark format (see below)
    """

    __visit_name__ = "markdown"
    pattern = re.compile(r"\s*(\S|\s)*")


class Xhtml:  # type:ignore
    __visit_name__ = "xhtml"


@dataclasses.dataclass(frozen=True, **SLOTS)
class Date:
    """A date, or partial date (e.g. just year or year + month)
    as used in human communication. The format is YYYY, YYYY-MM, or YYYY-MM-DD,
    e.g. 2018, 1973-06, or 1905-08-23.
    There SHALL be no time zone. Dates SHALL be valid dates"""

    pattern = re.compile(
        r"([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|"
        r"[1-9]000)(-(0[1-9]|1[0-2])(-(0[1-9]|[1-2]"
        r"[0-9]|3[0-1]))?)?"
    )
    __visit_name__ = "date"

    @classmethod
    def produce_inner_schema(cls):
        """ """
        return core_schema.date_schema()

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: typing.Any, handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        """
        Return a Pydantic CoreSchema with the FHIR Date, DateTime, Time and Instant validation.

        Args:
            source_type: The source type to be converted.
            handler: The handler to get the CoreSchema.

        Returns:
            A Pydantic CoreSchema with the FHIR resource validation.

        """

        # inner_schema = cls.produce_inner_schema(source_type, handler)
        def _serialize(
            value: typing.Union[str, datetime.datetime, datetime.date, datetime.time],
            info: core_schema.SerializationInfo,
        ) -> typing.Union[str, datetime.datetime, datetime.date, datetime.time]:
            if isinstance(value, str):
                return value
            if info.mode == "json":
                return value.isoformat()
            else:
                return value

        def _validate(
            input_value: typing.Union[str, PydanticUrl],
            validator: typing.Callable[[typing.Union[str, PydanticUrl]], typing.Any],
            validation_info: ValidationInfo,
        ) -> typing.Union[datetime.date, str]:
            """
            Validate a date from the provided str value.

            Args:
                input_value: The date value to be validated.
            Returns:
                Date or str.

            """
            validated_value = cls._validate_date(input_value, validator)
            if (
                cls.__name__ == DateTime.__name__
                and isinstance(validated_value, datetime.datetime)
                and isinstance(input_value, str)
            ):
                if "T" in input_value and validated_value.tzinfo is None:
                    # a datetime with time MUST have a timezone
                    raise ValueError(
                        "Datetime must be timezone aware if it has a time component."
                    )
                if "T" not in input_value and validated_value.time():
                    # a datetime without time MUST NOT have a time component
                    validated_value = validated_value.date().isoformat()
            return validated_value

        return core_schema.with_info_wrap_validator_function(
            _validate,
            cls.produce_inner_schema(),
            serialization=core_schema.plain_serializer_function_ser_schema(
                _serialize,
                info_arg=True,
                when_used="always",
            ),
        )

    @classmethod
    def _validate_date(
        cls,
        input_value: typing.Any,
        validator: typing.Callable[[typing.Any], typing.Any],
    ) -> typing.Union[datetime.date, str]:
        """ """
        if not isinstance(input_value, str):
            # default handler
            return validator(input_value)

        match = FHIR_DATE_PARTS.match(input_value)
        if match and not match.groupdict().get("day"):
            if match.groupdict().get("month") and int(match.groupdict()["month"]) > 12:
                raise ValueError
            # we keep original
            return input_value

        return validator(input_value)


class DateTime(Date):
    """A date, date-time or partial date (e.g. just year or year + month) as used
    in human communication. The format is YYYY, YYYY-MM, YYYY-MM-DD or
    YYYY-MM-DDThh:mm:ss+zz:zz, e.g. 2018, 1973-06, 1905-08-23,
    2015-02-07T13:28:17-05:00 or 2017-01-01T00:00:00.000Z.
    If hours and minutes are specified, a time zone SHALL be populated.
    Seconds must be provided due to schema type constraints but may be
    zero-filled and may be ignored at receiver discretion.
    Dates SHALL be valid dates. The time "24:00" is not allowed.
    Leap Seconds are allowed - see below"""

    pattern = re.compile(
        r"([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|"
        r"[1-9]000)(-(0[1-9]|1[0-2])(-(0[1-9]|[1-2][0-9]|"
        r"3[0-1])(T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|"
        r"60)(\.[0-9]+)?(Z|([+\-])((0[0-9]|"
        r"1[0-3]):[0-5][0-9]|14:00)))?)?)?"
    )
    __visit_name__ = "dateTime"

    @classmethod
    def produce_inner_schema(cls):
        """ """
        return core_schema.datetime_schema()


class Instant(DateTime):
    """An instant in time in the format YYYY-MM-DDThh:mm:ss.sss+zz:zz
    (e.g. 2015-02-07T13:28:17.239+02:00 or 2017-01-01T00:00:00Z).
    The time SHALL specified at least to the second and SHALL include a time zone.
    Note: This is intended for when precisely observed times are required
    (typically system logs etc.), and not human-reported times - for those,
    use date or dateTime (which can be as precise as instant,
    but is not required to be). instant is a more constrained dateTime

    Note: This type is for system times, not human times (see date and dateTime below).
    """

    pattern = re.compile(
        r"([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|"
        r"[1-9]000)-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|"
        r"3[0-1])T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]"
        r"|60)(\.[0-9]+)?(Z|([+\-])((0[0-9]|"
        r"1[0-3]):[0-5][0-9]|14:00))"
    )
    __visit_name__ = "instant"


@dataclasses.dataclass(frozen=True, **SLOTS)
class Time:
    """A time during the day, in the format hh:mm:ss.
    There is no date specified. Seconds must be provided due
    to schema type constraints but may be zero-filled and may
    be ignored at receiver discretion.
    The time "24:00" SHALL NOT be used. A time zone SHALL NOT be present.
    Times can be converted to a Duration since midnight."""

    pattern = re.compile(r"([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\.[0-9]+)?")
    __visit_name__ = "time"

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: typing.Any, handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        """
        Return a Pydantic CoreSchema with the Time validation.

        Args:
            source_type: The source type to be converted.
            handler: The handler to get the CoreSchema.

        Returns:
            A Pydantic CoreSchema with the time validation.

        """

        # inner_schema = cls.produce_inner_schema(source_type, handler)

        def _validate(
            input_value: typing.Union[str, PydanticUrl],
            validator: typing.Callable[[typing.Union[str, PydanticUrl]], typing.Any],
            validation_info: ValidationInfo,
        ) -> typing.Union[str, PydanticUrl]:
            """
            Validate a MAC Address from the provided str value.

            Args:
                input_value: The Decimal value to be validated.
            Returns:
                time.

            """
            return cls._validate_time(input_value, validator)

        return core_schema.with_info_wrap_validator_function(
            _validate,
            core_schema.time_schema(),
        )

    @classmethod
    def _validate_time(cls, input_value, validator):
        """ """
        if isinstance(input_value, str):
            if not cls.pattern.match(input_value):
                raise ValueError

        return validator(input_value)


# **************************************
# ****  FHIR Primitive Types ***********
# **************************************
# boolean
BooleanType = bool
FHIR_PRIMITIVES_MAPS[BooleanType] = "boolean"

# string
StringType = Annotated[str, String()]
FHIR_PRIMITIVES_MAPS[StringType] = "string"
FHIR_PRIMITIVES_MAPS[String] = "string"

# base64Binary
Base64BinaryType = Annotated[Base64Bytes, Base64Binary()]
FHIR_PRIMITIVES_MAPS[Base64BinaryType] = "base64Binary"
FHIR_PRIMITIVES_MAPS[Base64Binary] = "base64Binary"

# code
CodeType = Annotated[str, Code()]
FHIR_PRIMITIVES_MAPS[CodeType] = "code"
FHIR_PRIMITIVES_MAPS[Code] = "code"

# id
IdType = Annotated[str, Id()]
FHIR_PRIMITIVES_MAPS[IdType] = "id"
FHIR_PRIMITIVES_MAPS[Id] = "id"

# decimal
DecimalType = Annotated[decimal.Decimal, Decimal()]
FHIR_PRIMITIVES_MAPS[DecimalType] = "decimal"
FHIR_PRIMITIVES_MAPS[Decimal] = "decimal"

# integer
IntegerType = Annotated[int, Integer()]
FHIR_PRIMITIVES_MAPS[IntegerType] = "integer"
FHIR_PRIMITIVES_MAPS[Integer] = "integer"

# integer64
Integer64Type = Annotated[int, Integer64()]
FHIR_PRIMITIVES_MAPS[Integer64Type] = "integer64"
FHIR_PRIMITIVES_MAPS[Integer64] = "integer64"

# unsignedInt
UnsignedIntType = Annotated[int, UnsignedInt()]
FHIR_PRIMITIVES_MAPS[UnsignedIntType] = "unsignedInt"
FHIR_PRIMITIVES_MAPS[UnsignedInt] = "unsignedInt"

# positiveInt
PositiveIntType = Annotated[int, PositiveInt()]
FHIR_PRIMITIVES_MAPS[PositiveIntType] = "positiveInt"
FHIR_PRIMITIVES_MAPS[PositiveInt] = "positiveInt"

# uri
UriType = Annotated[str, Uri()]
FHIR_PRIMITIVES_MAPS[UriType] = "uri"
FHIR_PRIMITIVES_MAPS[Uri] = "uri"

# canonical
CanonicalType = Annotated[str, Canonical()]
FHIR_PRIMITIVES_MAPS[CanonicalType] = "canonical"
FHIR_PRIMITIVES_MAPS[Canonical] = "canonical"

# oid
OidType = Annotated[str, Oid()]
FHIR_PRIMITIVES_MAPS[OidType] = "oid"
FHIR_PRIMITIVES_MAPS[Oid] = "oid"

# uuid
UuidType = UUID4
FHIR_PRIMITIVES_MAPS[UuidType] = "uuid"

# url
UrlType = Annotated[typing.Union[AnyUrl, str], Url()]
FHIR_PRIMITIVES_MAPS[UrlType] = "url"
FHIR_PRIMITIVES_MAPS[Url] = "url"

# markdown
MarkdownType = Annotated[str, Markdown()]
FHIR_PRIMITIVES_MAPS[MarkdownType] = "markdown"
FHIR_PRIMITIVES_MAPS[Markdown] = "markdown"

# xhtml
XhtmlType = Annotated[str, Xhtml()]
FHIR_PRIMITIVES_MAPS[XhtmlType] = "xhtml"
FHIR_PRIMITIVES_MAPS[Xhtml] = "xhtml"

# date
DateType = Annotated[datetime.date, Date()]
FHIR_PRIMITIVES_MAPS[DateType] = "date"
FHIR_PRIMITIVES_MAPS[Date] = "date"

# dateTime
DateTimeType = Annotated[datetime.datetime, DateTime()]
FHIR_PRIMITIVES_MAPS[DateTimeType] = "dateTime"
FHIR_PRIMITIVES_MAPS[DateTime] = "dateTime"

# instant
InstantType = Annotated[datetime.datetime, Instant()]
FHIR_PRIMITIVES_MAPS[InstantType] = "instant"
FHIR_PRIMITIVES_MAPS[Instant] = "instant"

# time
TimeType = Annotated[datetime.time, Time()]
FHIR_PRIMITIVES_MAPS[TimeType] = "time"
FHIR_PRIMITIVES_MAPS[Time] = "time"


# factory function
def _create_fhir_type(
    klass_name: str, model_klass: str, base_class: typing_extensions.Type[FhirBase]
) -> typing.Type[FhirBase]:
    """ """
    klass = type(klass_name, (base_class,), {"_model_klass": model_klass})

    if typing.TYPE_CHECKING:
        klass = typing.cast(typing.Type[FhirBase], klass)

    if klass_name not in FHIR_TYPES_MAPS:
        FHIR_TYPES_MAPS[klass_name] = model_klass

    return klass  # type: ignore


def create_fhir_type(klass_name: str, model_klass: str) -> typing.Type[FhirBase]:
    """ """
    return _create_fhir_type(klass_name, model_klass, FhirBase)


def create_fhir_element_or_resource_type(
    klass_name: str, model_klass: str
) -> typing.Type[FhirBase]:
    """ """
    return _create_fhir_type(klass_name, model_klass, FhirElementOrResourceBase)


__all__ = [
    "FhirBase",
    "create_fhir_type",
    "create_fhir_element_or_resource_type",
    "BooleanType",
    "StringType",
    "Base64BinaryType",
    "CodeType",
    "IdType",
    "IntegerType",
    "Integer64Type",
    "DecimalType",
    "UnsignedIntType",
    "PositiveIntType",
    "CanonicalType",
    "UriType",
    "OidType",
    "UuidType",
    "UrlType",
    "MarkdownType",
    "XhtmlType",
    "DateType",
    "DateTimeType",
    "InstantType",
    "TimeType",
]
