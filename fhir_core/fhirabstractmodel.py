from __future__ import annotations as _annotations

import decimal

"""Base class for all FHIR elements. """

import inspect
import logging
import typing
import warnings
from collections import OrderedDict
from functools import lru_cache

import typing_extensions
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    PydanticDeprecatedSince20,
    SerializationInfo,
    model_serializer,
    model_validator,
)
from pydantic.fields import FieldInfo
from pydantic_core import InitErrorDetails, PydanticCustomError, ValidationError
from typing_extensions import Literal, Self

from .constraints import HAS_XML_SUPPORT, HAS_YAML_SUPPORT
from .utils import get_base64_encoder, is_primitive_type

if HAS_YAML_SUPPORT:
    from .yaml_utils import yaml_dumps, yaml_loads
if HAS_XML_SUPPORT:
    from .xml_utils import xml_dumps, xml_loads

if typing.TYPE_CHECKING:
    from pydantic.main import TupleGenerator

__author__ = "Md Nazrul Islam"
__email__ = "email2nazrul@gmail.com"

logger = logging.getLogger(__name__)
ROOT_KEY = "root"
FHIR_COMMENTS_FIELD_NAME = "fhir_comments"
FHIRErrorCodes = Literal[
    "fhir-validation-missing-resource-type",
    "fhir-validation-wrong-resource-type",
    "model_field_validation.missing",
]


class FHIRAbstractModel(BaseModel):
    """Abstract base model class for all FHIR elements."""

    __fhir_serialization_exclude_comment__: bool = False
    # __resource_type__: Literal['ResourceType'] = 'ResourceType'
    __resource_type__: str = "__resource_type__"

    fhir_comments: typing.Union[str, typing.List[str]] | None = Field(
        None, alias="fhir_comments", json_schema_extra={"element_property": False}
    )

    def __init__(self, /, **data: typing.Any) -> None:  # type: ignore
        """
        from pydantic_core import PydanticCustomError
        raise PydanticCustomError(
            'sequence_str',
            "'{type_name}' instances are not allowed as a Sequence value",
            {'type_name': value_type.__name__},
        )
        https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.InitErrorDetails
        """
        if self.__resource_type__ is Ellipsis:
            raise ValueError("__resource_type__ must be defined in subclasses")

        resource_type = data.pop("resource_type", None)
        if "resourceType" in data and "resourceType" not in self.model_fields:
            resource_type = data.pop("resourceType", None)

        if resource_type is not None and resource_type != self.__resource_type__:
            expected_resource_type = self.__resource_type__
            error_type: PydanticCustomError = PydanticCustomError(
                "fhir-validation-wrong-resource-type",
                """``{module_name}.{class_name}`` expects resource type ``{expected_resource_type}``,
                    but got ``{resource_type}``. Make sure resource type name is correct and right
                    ModelClass has been chosen.""",
                {
                    "module_name": self.__class__.__module__,
                    "class_name": self.__class__.__name__,
                    "expected_resource_type": expected_resource_type,
                    "resource_type": resource_type,
                },
            )
            error_: InitErrorDetails = {
                "type": error_type,
                "loc": ("resource_type",),
                "input": resource_type,
            }
            raise ValidationError.from_exception_data(self.__class__.__name__, [error_])

        BaseModel.__init__(self, **data)

    @classmethod
    def element_properties(
        cls: typing.Type["FHIRAbstractModel"],
    ) -> typing.Generator[FieldInfo, None, None]:
        """ """
        for field_info in cls.model_fields.values():
            if field_info.json_schema_extra.get("element_property", False):  # type: ignore
                yield field_info

    @classmethod
    def elements_sequence(cls) -> typing.List[str]:
        """returning all elements names from ``Resource`` according specification,
        with preserving original sequence order.
        """
        return []

    @classmethod
    @lru_cache(maxsize=1024, typed=True)
    def has_resource_base(cls) -> bool:
        """ """
        # xxx: calculate metrics, other than cache it!
        for cl in inspect.getmro(cls)[:-3]:
            if cl.__name__ == "Resource":
                return True
        return False

    @classmethod
    @lru_cache(maxsize=None, typed=True)
    def get_resource_type(cls: typing.Type["FHIRAbstractModel"]) -> str:
        """ """
        return cls.__resource_type__

    @classmethod
    @lru_cache(maxsize=None, typed=True)
    def get_alias_mapping(
        cls: typing.Type["FHIRAbstractModel"],
    ) -> typing.Dict[str, str]:
        """Mappings between field's name and alias"""
        aliases = cls.elements_sequence()
        return {
            fi.alias: fn for fn, fi in cls.model_fields.items() if fi.alias in aliases
        }

    @classmethod
    def get_json_encoder(cls) -> typing.Callable[[typing.Any], typing.Any]:
        """ """
        return cls.__pydantic_serializer__.to_json

    def model_dump_json(
        self,
        *,
        indent: int | None = None,
        # FHIR custom
        exclude_comments: bool = False,
        **pydantic_kwargs,
    ) -> str:
        """Usage docs: https://docs.pydantic.dev/2.7/concepts/serialization/#modelmodel_dump_json

        Generates a JSON representation of the model using Pydantic's `to_json` method.

        Args:
            indent: Indentation to use in the JSON output. If None is passed, the output will be compact.
            exclude_comments: If the FHIR comment should be excluded.
                    By default, FHIR comments are included.
            pydantic_kwargs: Original pydantic BaseModel.model_dump() parameters.
                    Normally you don't need to use other params.

        Returns:
            A JSON string representation of the model.
        """
        """Fully overridden method but codes are copied from BaseMode and business logic added
        in according to support ``fhir_comments``filter and other FHIR specific requirments.
        """
        by_alias = pydantic_kwargs.pop("by_alias", None)
        if by_alias is None:
            by_alias = True
        exclude_none = pydantic_kwargs.pop("exclude_none", None)
        if exclude_none is None:
            exclude_none = True

        org_config_val = None
        if exclude_comments is not None:
            org_config_val = self.__fhir_serialization_exclude_comment__
            self.__fhir_serialization_exclude_comment__ = exclude_comments

        result = BaseModel.model_dump_json(
            self,
            indent=indent,
            by_alias=by_alias,
            exclude_none=exclude_none,
            **pydantic_kwargs,
        )
        if exclude_comments is not None:
            self.__fhir_serialization_exclude_comment__ = org_config_val
        return result

    def model_dump_yaml(
        self,
        *,
        # YAML
        indent: int | None = None,
        # FHIR custom
        exclude_comments: bool = False,
        **pydantic_kwargs,
    ) -> str:
        """
        Generates a YAML representation of the model using PyYAML.

        Args:
            indent: Indentation to use in the YAML output. If None is passed, the output will be compact.
            exclude_comments: If the FHIR comment should be excluded.
                    By default, FHIR comments are included.
            pydantic_kwargs: Original pydantic BaseModel.model_dump() parameters.
                    Normally you don't need to use other params.

        Returns:
            A YAML string representation of the model.
        """
        """Fully overridden method but codes are copied from BaseMode and business logic added
        in according to support ``fhir_comments``filter and other FHIR specific requirments.
        """
        if not HAS_YAML_SUPPORT:
            raise ModuleNotFoundError(
                "You need to install ``PyYAML`` package to use this method. "
            )
        result = self.model_dump(exclude_comments=exclude_comments, **pydantic_kwargs)

        return yaml_dumps(result, indent=indent, return_bytes=False, sort_keys=False)

    def model_dump_xml(
        self,
        *,
        # XML
        pretty_print: bool = False,
        xml_declaration=True,
        # FHIR custom
        exclude_comments: bool = False,
        **pydantic_kwargs,
    ) -> str:
        """
        Generates a YAML representation of the model using PyYAML.

        Args:
            pretty_print: .
            exclude_comments: If the FHIR comment should be excluded.
                    By default, FHIR comments are included.
            xml_declaration:
            pydantic_kwargs: Original pydantic BaseModel.model_dump() parameters.
                    Normally you don't need to use other params.

        Returns:
            A XML string representation of the model.
        """
        if not HAS_XML_SUPPORT:
            raise ModuleNotFoundError(
                "You need to install ``lxml`` package to use this method. "
            )
        return xml_dumps(
            self,
            pretty_print=pretty_print,
            xml_declaration=xml_declaration,
            with_comments=exclude_comments is False,
        )

    def model_dump(
        self,
        *,
        # our custom
        exclude_comments: bool = False,
        **pydantic_kwargs,
    ) -> typing.Dict[str, typing.Any]:
        """Usage docs: https://docs.pydantic.dev/2.7/concepts/serialization/#modelmodel_dump

        Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

        Args:
            exclude_comments: If the FHIR comment should be excluded.
                    By default, FHIR comments are included.
            pydantic_kwargs: Original pydantic BaseModel.model_dump() parameters.
                    Normally you don't need to use other params.

        Returns:
            A dictionary representation of the model.

        if len(pydantic_kwargs) > 0:
            logger.warning(
                f"{self.__class__.__name__}.dict method accepts only"
                "´by_alias´, ´exclude_none´, ´exclude_comments` as parameters"
                " since version v6.2.0, any extra parameter is simply ignored. "
                "You should not provide any extra argument."
        )
        """
        by_alias = pydantic_kwargs.pop("by_alias", None)
        if by_alias is None:
            by_alias = True
        mode = pydantic_kwargs.pop("mode", None)
        if mode is None:
            mode = "python"

        exclude_none = pydantic_kwargs.pop("exclude_none", None)
        if exclude_none is None:
            exclude_none = True

        org_config_val = None
        if exclude_comments is not None:
            org_config_val = self.__fhir_serialization_exclude_comment__
            self.__fhir_serialization_exclude_comment__ = exclude_comments

        result = BaseModel.model_dump(
            self,
            mode=mode,
            by_alias=by_alias,
            exclude_none=exclude_none,
            **pydantic_kwargs,
        )
        if exclude_comments is not None:
            self.__fhir_serialization_exclude_comment__ = org_config_val
        return result

    @typing_extensions.deprecated(
        "The `dict` method is deprecated; use `model_dump` instead.", category=None
    )
    def dict(  # noqa: D102
        self,
        *,
        # FHIR custom
        exclude_comments: bool = False,
        **pydantic_kwargs,
    ) -> typing.Dict[str, typing.Any]:
        warnings.warn(
            "The `dict` method is deprecated; use `model_dump` instead.",
            category=PydanticDeprecatedSince20,
        )
        return self.model_dump(exclude_comments=exclude_comments, **pydantic_kwargs)

    @typing_extensions.deprecated(
        "The `json` method is deprecated; use `model_dump_json` instead.", category=None
    )
    def json(  # noqa: D102
        self,
        *,
        indent: int | None = None,
        # FHIR custom
        exclude_comments: bool = False,
        **pydantic_kwargs,
    ) -> str:
        warnings.warn(
            "The `json` method is deprecated; use `model_dump_json` instead.",
            category=PydanticDeprecatedSince20,
        )
        return self.model_dump_json(
            indent=indent, exclude_comments=exclude_comments, **pydantic_kwargs
        )

    @classmethod
    def model_validate_yaml(
        cls,
        yaml_data: str | bytes | bytearray,
        *,
        strict: bool | None = None,
        context: typing.Any | None = None,
    ) -> Self:
        """Usage docs: https://pypi.org/project/fhir.resources/#YAML

        Validate the given YAML data against the Pydantic model.

        Args:
            yaml_data: The YAML data to validate.
            strict: Whether to enforce types strictly.
            context: Extra variables to pass to the validator.

        Returns:
            The validated Pydantic model.

        Raises:
            ValueError: If `yaml_data` is not a YAML string.
        """
        if not HAS_YAML_SUPPORT:
            raise ModuleNotFoundError(
                "You need to install ``PyYAML`` package to use this method. "
            )
        data = yaml_loads(yaml_data)
        return cls.model_validate(data, strict=strict, context=context)

    @classmethod
    def model_validate_xml(
        cls,
        xml_data: str | bytes | bytearray,
        *,
        strict: bool | None = None,
        context: typing.Any | None = None,
    ) -> Self:
        """Usage docs: https://pypi.org/project/fhir.resources/#XML

        Validate the given XML data against the Pydantic model.

        Args:
            xml_data: The YAML data to validate.
            strict: Whether to enforce types strictly.
            context: Extra variables to pass to the validator.

        Returns:
            The validated Pydantic model.

        Raises:
            ValueError: If `xml_data` is not valid XML.
        """
        if not HAS_XML_SUPPORT:
            raise ModuleNotFoundError(
                "You need to install ``lxml`` package to use this method. "
            )

        me = xml_loads(cls, xml_data)
        if typing.TYPE_CHECKING:
            me = typing.cast(Self, me)
        return me

    # Serializers
    @model_serializer(mode="wrap", when_used="always", return_type=OrderedDict)
    def fhir_model_serializer(
        self,
        serialize: typing.Callable[[typing.Any], typing.Any],
        info: SerializationInfo,
    ) -> OrderedDict:
        return OrderedDict(self._fhir_iter(serialize, info))

    # Private methods
    def _fhir_iter(
        self,
        serialize: typing.Callable[[typing.Any], typing.Any],
        info: SerializationInfo,
    ) -> "TupleGenerator":
        if self.__class__.has_resource_base():
            yield "resourceType", self.__resource_type__

        alias_maps = self.get_alias_mapping()
        for prop_name in self.elements_sequence():
            field_key = alias_maps[prop_name]
            field_info = self.model_fields[field_key]
            is_primitive = is_primitive_type(field_info)
            dict_key = info.by_alias and field_info.alias or field_key
            value = self.__dict__.get(field_key, None)
            if not is_primitive and value is not None:
                value = self._serialize_non_primitive_value(value, serialize, info)
            else:
                value = self._serialize_primitive_value(value, field_info)
            if value is not None or (info.exclude_none is False and value is None):
                yield dict_key, value

            # looking for comments or primitive extension for primitive data type
            if is_primitive:
                ext_key = f"{field_key}__ext"
                ext_val = self.__dict__.get(ext_key, None)
                if ext_val is not None:
                    ext_val = self._serialize_non_primitive_value(
                        ext_val, serialize, info
                    )
                if ext_val is not None:
                    dict_key_ = (
                        info.by_alias and self.model_fields[ext_key].alias or ext_key
                    )
                    if ext_val is not None and len(ext_val) > 0:
                        yield dict_key_, ext_val
        # looking for comments
        comments = self.__dict__.get(FHIR_COMMENTS_FIELD_NAME, None)

        if comments is not None and not self.__fhir_serialization_exclude_comment__:
            yield FHIR_COMMENTS_FIELD_NAME, comments

    def _serialize_non_primitive_value(
        self,
        value: typing.Any,
        serialize: typing.Callable[[typing.Any], typing.Any],
        info: SerializationInfo,
    ) -> typing.Any:
        """ """
        if isinstance(value, list):
            if len(value) == 0:
                return value
            container = list()
            for val in value:
                container.append(
                    self._serialize_non_primitive_value(val, serialize, info)
                )
            return container

        if value is None:
            return value
        if isinstance(value, FHIRAbstractModel):
            return value.model_dump(
                exclude_comments=self.__fhir_serialization_exclude_comment__,
                mode=info.mode,
                by_alias=info.by_alias,
                exclude_none=info.exclude_none,
            )
        else:
            return serialize(value)

    def _serialize_primitive_value(
        self,
        value: typing.Any,
        field_info: FieldInfo,
    ) -> typing.Any:
        """ """
        if isinstance(value, list):
            if len(value) == 0:
                return value
            container = list()
            for val in value:
                container.append(self._serialize_primitive_value(val, field_info))
            return container

        if value is None:
            return value
        if isinstance(value, (bytes, bytearray)):
            _enc_klass = get_base64_encoder(field_info)
            if _enc_klass:
                return _enc_klass.encode(value)
        if isinstance(value, decimal.Decimal):
            # @TODO: the function types.py#Decimal.__get_pydantic_core_schema__._serialize
            # somehow is not called, until the reason is found, we serialize from here!
            return float(value)
        return value

    @model_validator(mode="after")
    def validate_after_model_construction(self) -> Self:
        """ """
        # do after validation for primitive elements
        self._validate_required_primitive_elements()

        # do after validation for one of many
        self._validate_one_of_many()

        return self

    def _validate_one_of_many(self):
        """https://www.hl7.org/fhir/formats.html#choice
        A few elements have a choice of more than one data type for their content.
        All such elements have a name that takes the form nnn[x].
        The "nnn" part of the name is constant, and the "[x]" is replaced with
        the title-cased name of the type that is actually used.
        The table view shows each of these names explicitly.

        Elements that have a choice of data type cannot repeat - they must have a
        maximum cardinality of 1. When constructing an instance of an element with a
        choice of types, the authoring system must create a single element with a
        data type chosen from among the list of permitted data types.
        """
        one_of_many_fields = self.get_one_of_many_fields()
        if len(one_of_many_fields) == 0:
            return

        for prefix, fields in one_of_many_fields.items():
            assert (
                self.model_fields[fields[0]].json_schema_extra["one_of_many"] == prefix  # type: ignore
            )
            required = (
                self.model_fields[fields[0]].json_schema_extra["one_of_many_required"]  # type: ignore
                is True
            )
            found = False
            for field in fields:
                if getattr(self, field, None) is not None:
                    if found is True:
                        raise ValueError(
                            "Any of one field value is expected from "
                            f"this list {fields}, but got multiple!"
                        )
                    else:
                        found = True
            if required is True and found is False:
                raise ValueError(f"Expect any of field value from this list {fields}.")

    def _validate_required_primitive_elements(self):
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = self.get_required_fields()
        if len(required_fields) == 0:
            return
        _missing = object()

        errors: typing.List[InitErrorDetails] = list()
        alias_maps = self.get_alias_mapping()

        for name, ext in required_fields:
            field_key = alias_maps[name]
            field_info = self.model_fields[field_key]
            ext_field_info = self.model_fields[ext]
            value = getattr(self, field_key, _missing)
            if value not in (_missing, None):
                continue
            ext_value = getattr(self, ext, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value, "__resource_type__", None)
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:  # type: ignore
                        missing_ext = False
                else:
                    validate_pass = True
                    # for validator in ext_field.type_.__get_validators__():
                    #    try:
                    #        ext_value = validator(v=ext_value)
                    #    except ValidationError as exc:
                    #        errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                    #        validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:  # type: ignore
                        missing_ext = False
            if missing_ext:
                if typing.TYPE_CHECKING:
                    error_: InitErrorDetails
                if value in (_missing, None):
                    # 'field required'
                    error_type = PydanticCustomError(
                        "model_field_validation.missing",
                        "Value for the field '{field_name}' is required.",
                        {"field_name": field_info.alias},
                    )
                    error_ = {
                        "type": error_type,
                        "loc": (field_info.alias,),  # type: ignore
                        "input": value,
                    }
                    errors.append(error_)

        if len(errors) > 0:
            raise ValidationError.from_exception_data(self.__class__.__name__, errors)  # type: ignore

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """This method should be overridden in each subclass.
        [("type", "type__ext")]"""
        return []

    def get_one_of_many_fields(self) -> typing.Dict[str, typing.List[str]]:
        """This method should be override in subclasses to specify one set of fields

        return {
            "allowed": ["allowedMoney", "allowedString", "allowedUnsignedInt"],
            "used": ["usedMoney", "usedUnsignedInt"],
        }
        """
        return {}

    model_config = ConfigDict(
        extra="forbid", validate_assignment=True, populate_by_name=True
    )
