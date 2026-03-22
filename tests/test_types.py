import decimal
import importlib
import json
import typing
import uuid
from datetime import date, datetime, timedelta, timezone

import pytest
from pydantic import BaseModel, Field
from pydantic_core import ValidationError
from typing_extensions import Annotated

from fhir_core import types as fhir_types
from fhir_core.fhirabstractmodel import FHIRAbstractModel
from fhir_core.types import Date, DateTime
from tests.fixtures.resources import fhirtypes

__author__ = "Md Nazrul Islam"
__email__ = "email2nazrul@gmail.com"


class MyFhirPatientModel(FHIRAbstractModel):
    __resource_type__ = "MyFhirPatientModel"
    name: fhir_types.StringType = Field(..., title="Name")


MyFhirPatientModelType = fhir_types.create_fhir_type(
    "MyFhirPatientModelType", "tests.test_types.MyFhirPatientModel"
)


def test_fhirbase_type():
    """ """

    class MyHospitalModel(FHIRAbstractModel):
        __resource_type__ = "MyHospitalModel"
        patients: typing.List[MyFhirPatientModelType]


def test_string_type():
    """ """

    class MySimpleStringModel(BaseModel):
        name: fhir_types.StringType = Field(..., alias="name", title="My Name")

    model = MySimpleStringModel(name="Joe Bussen")
    assert model.name == "Joe Bussen"

    with pytest.raises(ValidationError) as exc_info:
        # empty string should not be allowed
        MySimpleStringModel(name="")

    assert exc_info.type is ValidationError
    from fhir_core import constraints

    constraints.TYPES_STRING_ALLOW_EMPTY_STR = True

    importlib.reload(fhir_types)
    importlib.reload(fhirtypes)
    StringType = Annotated[str, fhir_types.String()]

    class MySimpleStringModel2(BaseModel):
        name: StringType = Field(..., alias="name", title="My Name")

    model = MySimpleStringModel2(name="")
    assert model.name == ""

    constraints.TYPES_STRING_ALLOW_EMPTY_STR = False
    importlib.reload(fhir_types)
    importlib.reload(fhirtypes)

    class MySimpleStringModel3(BaseModel):
        names: typing.List[fhir_types.StringType] = Field(
            ..., alias="names", title="My Name"
        )

    model = MySimpleStringModel3(names=["Joe", "Bussen"])
    assert model.names[1] == "Bussen"

    with pytest.raises(ValidationError) as exc_info:
        # empty string should not be allowed
        MySimpleStringModel3(names=["Joe", None])
    assert "input_type=NoneType" in str(exc_info)

    class MySimpleStringModel4(BaseModel):
        names: typing.List[typing.Union[StringType, None]] = Field(
            ..., alias="names", title="My Name"
        )

    model = MySimpleStringModel4(names=["Joe", "", None])
    assert model.names[2] is None


def test_bool_type():
    """ """

    class MySimpleBooleanModel(BaseModel):
        isTrue: fhir_types.BooleanType = Field(..., alias="isTrue", title="Is True")

    assert MySimpleBooleanModel(isTrue="true").isTrue is True
    assert MySimpleBooleanModel(isTrue="false").isTrue is False
    assert MySimpleBooleanModel(isTrue=True).isTrue is True


def test_code_type():
    """ """


def test_uuid():
    """ """

    class MySimpleUUIDModel(BaseModel):
        myUUID: fhir_types.UuidType = Field(..., alias="myUUID", title="UUID")

    model = MySimpleUUIDModel(myUUID="8c7f56df-b047-47c4-9391-7733e00fe512")
    assert isinstance(model.myUUID, uuid.UUID)
    # test with short version
    MySimpleUUIDModel(myUUID="8c7f56dfb04747c493917733e00fe512")
    assert (
        MySimpleUUIDModel(myUUID="8c7f56dfb04747c493917733e00fe512").myUUID
        == model.myUUID
    )

    with pytest.raises(ValidationError) as exc_info:
        MySimpleUUIDModel(myUUID="8c7f56dfb04747c493917733e00fe51")
    assert "Input should be a valid UUID" in str(exc_info)


def test_decimal_type():
    """ """

    class MySimpleDecimalModel(BaseModel):
        point: fhir_types.DecimalType = Field(
            ..., alias="point", title="My Decimal Point"
        )

    model = MySimpleDecimalModel(point="0.14009")
    assert isinstance(model.point, decimal.Decimal)


def test_date_type():
    """ """

    class MySimpleDateModel(BaseModel):
        birthday: fhir_types.DateType = Field(..., alias="birthday", title="Birthday")

    # Test with only year
    model = MySimpleDateModel(birthday="2016")
    isinstance(model.birthday, str)
    # test with year and month
    model = MySimpleDateModel(birthday="2016-09")
    isinstance(model.birthday, str)


def test_uri_type():
    """ """

    class MySimpleDateModel(BaseModel):
        minRules: fhir_types.UriType = Field(..., alias="minRules", title="Min Rules")

    assert MySimpleDateModel(minRules="None").model_dump()["minRules"] == "None"


def test_fhir_type_integer64():
    import sys

    from pydantic import BaseModel

    from fhir_core.types import Integer64  # noqa
    from fhir_core.types import Integer64Type

    # Input should be less than or equal to 2147483647 [type=less_than_equal, input_value='9223372036854775807', input_type=str]
    class MyModel(BaseModel):
        size: Integer64Type

    Integer64.max_length == sys.maxsize
    Integer64.min_length == sys.maxsize * -1

    import sys

    assert MyModel(size=f"{sys.maxsize}"), "Should not raise an exception"
    assert (
        MyModel(size=f"{sys.maxsize}").size == sys.maxsize
    ), f"Should be {sys.maxsize}"
    assert MyModel(size=sys.maxsize).size == sys.maxsize, f"Should be {sys.maxsize}"

    _ = MyModel(size=0)
    assert _.size == 0, "Should be zero"

    _.size = sys.maxsize
    assert _.size == sys.maxsize, "Should be sys.maxsize"

    _.size = sys.maxsize * -1
    assert _.size == sys.maxsize * -1, "Should be negative sys.maxsize"

    with pytest.raises(ValidationError):
        MyModel(size=sys.maxsize + 1)

    with pytest.raises(ValidationError):
        _ = (sys.maxsize + 1) * -1
        print(_)
        MyModel(size=_)


valid_instant_test_inputs = [
    (
        "2016-09-07T12:35:14+00:00",  # isoformat
        datetime(2016, 9, 7, 12, 35, 14, tzinfo=timezone.utc),
    ),
    (
        "2016-09-07T12:35:14Z",  # zulu timezone
        datetime(2016, 9, 7, 12, 35, 14, tzinfo=timezone.utc),
    ),
    (
        "2016-09-07T12:35:14+05:00",  # isoformat with offset
        datetime(2016, 9, 7, 12, 35, 14, tzinfo=timezone(timedelta(hours=5))),
    ),
    (
        "2016-09-07T15:49:01.1+00:00",  # isoformat partial fractional seconds
        datetime(2016, 9, 7, 15, 49, 1, microsecond=100_000, tzinfo=timezone.utc),
    ),
    (
        "2016-09-07T15:49:01.123456+00:00",  # isoformat max fractional seconds
        datetime(2016, 9, 7, 15, 49, 1, microsecond=123_456, tzinfo=timezone.utc),
    ),
    (
        "2016-09-07T15:49:01.1Z",  # zulu partial fractional seconds
        datetime(2016, 9, 7, 15, 49, 1, microsecond=100_000, tzinfo=timezone.utc),
    ),
    (
        "2016-09-07T15:49:01.123456Z",  # zulu max fractional seconds
        datetime(2016, 9, 7, 15, 49, 1, microsecond=123_456, tzinfo=timezone.utc),
    ),
    (
        datetime(
            2016, 9, 7, 12, 35, 14, microsecond=123_456, tzinfo=timezone.utc
        ),  # datetime input
        datetime(2016, 9, 7, 12, 35, 14, microsecond=123_456, tzinfo=timezone.utc),
    ),
]

valid_date_test_inputs = [
    (date(2016, 9, 7), date(2016, 9, 7)),  # date input
    ("2016-09-13", date(2016, 9, 13)),  # valid full date
    ("2016-09", "2016-09"),  # valid year + month
    ("2016", "2016"),  # valid year only
]


class MySimpleDateModel(BaseModel):
    time_stamp: fhir_types.DateType = Field(..., alias="time_stamp", title="TimeStamp")


@pytest.mark.parametrize(
    ("valid_date", "model_dump_expected"),
    valid_date_test_inputs
    + [
        (datetime(2016, 9, 13), date(2016, 9, 13)),  # valid datetime object
    ],
)
def test_date_type_valid(
    valid_date: typing.Union[str, date], model_dump_expected: typing.Union[str, date]
):
    """valid dates. See https://hl7.org/fhir/datatypes.html#date"""
    if isinstance(model_dump_expected, str):
        assert Date.pattern.match(
            model_dump_expected
        ), "Expected value should match regex - checking test data"

    assert (
        MySimpleDateModel(time_stamp=valid_date).model_dump()["time_stamp"]
        == model_dump_expected
    )

    assert json.loads(MySimpleDateModel(time_stamp=valid_date).model_dump_json()) == {
        "time_stamp": model_dump_expected.isoformat()
        if isinstance(model_dump_expected, date)
        else model_dump_expected,
    }


class MySimpleDateTimeModel(BaseModel):
    time_stamp: fhir_types.DateTimeType = Field(
        ..., alias="time_stamp", title="TimeStamp"
    )


@pytest.mark.parametrize(
    ("datetime_value", "model_dump_expected"),
    valid_instant_test_inputs
    + valid_date_test_inputs
    + [
        (
            datetime(2016, 9, 13, tzinfo=timezone.utc),
            datetime(2016, 9, 13, tzinfo=timezone.utc),
        ),  # valid datetime object
    ],
)
def test_datetime_type_valid(
    datetime_value: typing.Union[str, datetime],
    model_dump_expected: typing.Union[str, date, datetime],
):
    """ """
    if isinstance(model_dump_expected, str):
        assert DateTime.pattern.match(
            model_dump_expected
        ), "Expected value should match regex - checking test data"

    assert json.loads(
        MySimpleDateTimeModel(time_stamp=datetime_value).model_dump_json()
    ) == {
        "time_stamp": model_dump_expected.isoformat()
        if isinstance(model_dump_expected, (date, datetime))
        else model_dump_expected,
    }

    assert (
        MySimpleDateTimeModel(time_stamp=datetime_value).model_dump()["time_stamp"]
        == model_dump_expected
    )


@pytest.mark.parametrize(
    ("datetime_value", "error_message"),
    [
        (
            "2016-09-07T12:35:14",  # missing timezone
            "DateTime value string does not match spec regex",
        ),
        (
            "2016-09-07T12:35",  # missing minutes
            "DateTime value string does not match spec regex",
        ),
        (
            datetime.now(),  # missing timezone info
            "DateTime must be timezone aware",
        ),
    ],
)
def test_datetime_type_invalid(
    datetime_value: typing.Union[str, datetime], error_message: str
):
    """The time SHALL specified at least to the second and SHALL include a timezone offset. See https://hl7.org/fhir/datatypes.html#dateTime"""
    with pytest.raises(ValidationError, match=error_message):
        MySimpleDateTimeModel(time_stamp=datetime_value)


class MySimpleInstantModel(BaseModel):
    instant: fhir_types.InstantType = Field(..., alias="instant", title="Instant")


@pytest.mark.parametrize(
    ("instant_value", "model_dump_expected"),
    valid_instant_test_inputs,
)
def test_instant_type_valid(
    instant_value: typing.Union[str, datetime], model_dump_expected: datetime
):
    """ """
    assert (
        MySimpleInstantModel(instant=instant_value).model_dump()["instant"]
        == model_dump_expected
    )
    assert json.loads(
        MySimpleInstantModel(instant=instant_value).model_dump_json()
    ) == {"instant": model_dump_expected.isoformat()}


@pytest.mark.parametrize(
    ("instant_value", "error_message"),
    [
        (
            "2016-09-07T12:35:14",  # missing timezone
            "Instant value string does not match spec regex",
        ),
        (
            "2016-09-07T12:35",  # missing minutes
            "Instant value string does not match spec regex",
        ),
        (
            datetime.now(),  # missing timezone info
            "Instant must be timezone aware",
        ),
        (
            datetime.now().date(),  # missing timezone info
            "Instant must be timezone aware",
        ),
    ],
)
def test_instant_type_invalid(
    instant_value: typing.Union[str, datetime], error_message: str
):
    """The time SHALL specified at least to the second and SHALL include a timezone offset. See https://hl7.org/fhir/datatypes.html#instant"""
    with pytest.raises(ValidationError, match=error_message):
        MySimpleInstantModel(instant=instant_value)


def test_fhir_type_quantity():
    """Ensure that Quantity is correctly handled"""
    from pydantic import BaseModel

    from tests.fixtures.resources.quantity import Quantity

    class MyModel(BaseModel):
        size: Quantity

    _ = MyModel(size={"value": 10.101, "unit": "kg"})

    assert float(_.size.value) == 10.101, "Should be 10.101"
    serialized = _.size.model_dump_json()
    assert (
        '"10.101"' not in serialized
    ), f"Decimal values should not have quotes {serialized}"
