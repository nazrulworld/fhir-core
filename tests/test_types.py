import pytest
import typing
from pydantic import BaseModel, Field
from pydantic_core import ValidationError
from fhir_core import types as fhirtypes
__author__ = "Md Nazrul Islam"
__email__ = "email2nazrul@gmail.com"


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

    StringType = typing.Annotated[str, fhirtypes.String(allow_empty_str=True)]

    class MySimpleStringModel2(BaseModel):
        name: StringType = Field(..., alias="name", title="My Name")

    model = MySimpleStringModel2(name="")
    assert model.name == ""

    class MySimpleStringModel3(BaseModel):
        names: typing.List[fhirtypes.StringType] = Field(..., alias="names", title="My Name")

    model = MySimpleStringModel3(names=["Joe", "Bussen"])
    assert model.names[1] == "Bussen"

    with pytest.raises(ValidationError) as exc_info:
        # empty string should not be allowed
        MySimpleStringModel3(names=["Joe", None])
    assert 'input_type=NoneType' in str(exc_info)

    class MySimpleStringModel4(BaseModel):
        names: typing.List[typing.Union[StringType, None]] = Field(..., alias="names", title="My Name")

    model = MySimpleStringModel4(names=["Joe", "", None])
    assert model.names[2] is None


