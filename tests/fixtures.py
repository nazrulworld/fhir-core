import os
import pathlib
import typing
from os.path import dirname
from pydantic import BaseModel, Field
from fhir_core import types as fhirtypes

__author__ = "Md Nazrul Islam"
__email__ = "email2nazrul@gmail.com"

TESTS_ROOT_PATH = pathlib.Path(dirname(os.path.abspath(__file__)))
STATIC_PATH = TESTS_ROOT_PATH / "static"
IS_TRAVIS = "TRAVIS" in os.environ


class FhirPrimitiveTypesModel(BaseModel):
    """ """
    booleanTypeRequired: fhirtypes.BooleanType = Field(..., title="Boolean Type (required)")
    booleanTypeOptional: fhirtypes.BooleanType = Field(None, title="Boolean Type (optional)")

    stringTypeRequired: fhirtypes.StringType = Field(..., title="String Type (required)")
    stringTypeOptional: fhirtypes.StringType = Field(None, title="Integer Type (optional)")
    stringListTypeRequired: typing.List[fhirtypes.StringType] = Field(..., title="List of String Type (required)")
    stringListTypeOptional: typing.List[typing.Union[fhirtypes.StringType, None]] = Field(..., title="List of String "
                                                                                                     "Type (optional)")


