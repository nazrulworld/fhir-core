import decimal
import importlib
import typing
import uuid

import pytest
from pydantic import BaseModel, Field
from pydantic_core import ValidationError
from typing_extensions import Annotated

from fhir_core import types as fhir_types
from fhir_core.fhirabstractmodel import FHIRAbstractModel
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


def test_fhir_type_quantity():

    from pydantic import BaseModel
    from tests.fixtures.resources.quantity import Quantity

    class MyModel(BaseModel):
        size: Quantity

    _ = MyModel(size={"value": 10.101, "unit": "kg"})
    assert float(_.size.value) == 10.101, "Should be 10.101"
    serialized = _.model_dump_json()
    assert '"10.101"' not in serialized, f"Decimal values should not have quotes {serialized}"
