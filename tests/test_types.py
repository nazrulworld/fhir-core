import decimal
import typing
import uuid

import pytest
from pydantic import BaseModel, Field
from pydantic_core import ValidationError
from typing_extensions import Annotated

from fhir_core import types as fhirtypes
from fhir_core.fhirabstractmodel import FHIRAbstractModel

__author__ = "Md Nazrul Islam"
__email__ = "email2nazrul@gmail.com"


class MyFhirPatientModel(FHIRAbstractModel):
    __resource_type__ = "MyFhirPatientModel"
    name: fhirtypes.StringType = Field(..., title="Name")


MyFhirPatientModelType = fhirtypes.create_fhir_type(
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
        name: fhirtypes.StringType = Field(..., alias="name", title="My Name")

    model = MySimpleStringModel(name="Joe Bussen")
    assert model.name == "Joe Bussen"

    with pytest.raises(ValidationError) as exc_info:
        # empty string should not be allowed
        MySimpleStringModel(name="")

    assert exc_info.type is ValidationError

    StringType = Annotated[str, fhirtypes.String(allow_empty_str=True)]

    class MySimpleStringModel2(BaseModel):
        name: StringType = Field(..., alias="name", title="My Name")

    model = MySimpleStringModel2(name="")
    assert model.name == ""

    class MySimpleStringModel3(BaseModel):
        names: typing.List[fhirtypes.StringType] = Field(
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
        isTrue: fhirtypes.BooleanType = Field(..., alias="isTrue", title="Is True")

    assert MySimpleBooleanModel(isTrue="true").isTrue is True
    assert MySimpleBooleanModel(isTrue="false").isTrue is False
    assert MySimpleBooleanModel(isTrue=True).isTrue is True


def test_code_type():
    """ """


def test_uuid():
    """ """

    class MySimpleUUIDModel(BaseModel):
        myUUID: fhirtypes.UuidType = Field(..., alias="myUUID", title="UUID")

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
        point: fhirtypes.DecimalType = Field(
            ..., alias="point", title="My Decimal Point"
        )

    model = MySimpleDecimalModel(point="0.14009")
    assert isinstance(model.point, decimal.Decimal)


def test_date_type():
    """ """

    class MySimpleDateModel(BaseModel):
        birthday: fhirtypes.DateType = Field(..., alias="birthday", title="Birthday")

    # Test with only year
    model = MySimpleDateModel(birthday="2016")
    isinstance(model.birthday, str)
    # test with year and month
    model = MySimpleDateModel(birthday="2016-09")
    isinstance(model.birthday, str)


def test_uri_type():
    """ """

    class MySimpleDateModel(BaseModel):
        minRules: fhirtypes.UriType = Field(..., alias="minRules", title="Min Rules")

    assert MySimpleDateModel(minRules="None").model_dump()["minRules"] == "None"
