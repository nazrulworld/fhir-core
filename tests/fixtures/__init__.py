from __future__ import annotations as annotations_

import os
import pathlib
import typing
from os.path import dirname

from pydantic import BaseModel, Field

from fhir_core import types as fhir_types

__author__ = "Md Nazrul Islam"
__email__ = "email2nazrul@gmail.com"

TESTS_ROOT_PATH = pathlib.Path(dirname(os.path.abspath(__file__)))
STATIC_PATH = TESTS_ROOT_PATH.parent / "static"
STATIC_PATH_JSON = STATIC_PATH / "json"
STATIC_PATH_XML = STATIC_PATH / "xml"
STATIC_PATH_JSON_EXAMPLES = STATIC_PATH_JSON / "examples"
STATIC_PATH_XML_SCHEMA = STATIC_PATH_XML / "xsd"
STATIC_PATH_XML_EXAMPLES = STATIC_PATH_XML / "examples"
IS_TRAVIS = "TRAVIS" in os.environ


class FhirPrimitiveTypesModel(BaseModel):
    """ """

    booleanTypeRequired: fhir_types.BooleanType = Field(
        default=None, title="Boolean Type (required)"
    )
    booleanTypeOptional: fhir_types.BooleanType | None = Field(
        default=None, title="Boolean Type (optional)"
    )

    stringTypeRequired: fhir_types.StringType = Field(
        default=None, title="String Type (required)"
    )
    stringTypeOptional: fhir_types.StringType | None = Field(
        default=None, title="Integer Type (optional)"
    )
    stringListTypeRequired: typing.List[fhir_types.StringType] = Field(
        default=None, title="List of String Type (required)"
    )
    stringListTypeOptional: (
        typing.List[typing.Union[fhir_types.StringType, None]] | None
    ) = Field(default=None, title="List of String " "Type (optional)")

    stringListTypeOptional2: typing.List[fhir_types.StringType | None] | None = Field(
        default=None, title="List of String " "Type (optional)"
    )

    uuidTypeRequired: fhir_types.UuidType = Field(..., title="UUID Type (required)")

    uuidListTypeOptional: typing.List[fhir_types.UuidType] | None = Field(
        None, title="List of UUID " "Type (optional)"
    )

    dateTypeRequired: fhir_types.DateType = Field(
        default=None, title="Date Type (required)"
    )

    dateListTypeOptional: (
        typing.List[typing.Union[fhir_types.DateType, None]] | None
    ) = Field(default=None, title="List of Date " "Type (optional)")
    base64BinaryTypeRequired: fhir_types.Base64BinaryType = Field(
        default=None, title="Binary Type (required)"
    )
    urlTypeNotRequired: fhir_types.UrlType | None = Field(
        None, title="Url Type (not required)"
    )
    urlTypeNotRequiredList: typing.List[fhir_types.UrlType] | None = Field(
        default=None, title="Urls Type (not required)"
    )

    dateTypeNotRequired: fhir_types.DateType | None = Field(
        default=None, title="Date Type (not required)"
    )
    dateListNotRequired: typing.List[fhir_types.DateType] | None = Field(
        default=None, title="List of Date " "Type (not required)"
    )
    dateTimeNotRequired: fhir_types.DateTimeType | None = Field(
        default=None, title="DateTime Type (not required)"
    )
    dateTimeListNotRequired: typing.List[fhir_types.DateTimeType] | None = Field(
        default=None, title="List of DateTime " "Type (not required)"
    )
