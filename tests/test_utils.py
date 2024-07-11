from pydantic import BaseModel, Field

from fhir_core import types as fhirtypes
from fhir_core import utils
from tests.fixtures import FhirPrimitiveTypesModel

__author__ = "Md Nazrul Islam"
__email__ = "email2nazrul@gmail.com"


def test_check_primitive_type():
    """ """
    assert (
        utils.is_primitive_type(
            FhirPrimitiveTypesModel.model_fields["booleanTypeRequired"]
        )
        is True
    )

    assert (
        utils.is_primitive_type(
            FhirPrimitiveTypesModel.model_fields["booleanTypeOptional"]
        )
        is True
    )

    assert (
        utils.is_primitive_type(
            FhirPrimitiveTypesModel.model_fields["stringTypeRequired"]
        )
        is True
    )

    assert (
        utils.is_primitive_type(
            FhirPrimitiveTypesModel.model_fields["stringTypeOptional"]
        )
        is True
    )

    assert (
        utils.is_primitive_type(
            FhirPrimitiveTypesModel.model_fields["stringListTypeRequired"]
        )
        is True
    )

    assert (
        utils.is_primitive_type(
            FhirPrimitiveTypesModel.model_fields["stringListTypeOptional"]
        )
        is True
    )

    assert (
        utils.is_primitive_type(
            FhirPrimitiveTypesModel.model_fields["uuidTypeRequired"]
        )
        is True
    )

    assert (
        utils.is_primitive_type(
            FhirPrimitiveTypesModel.model_fields["uuidListTypeOptional"]
        )
        is True
    )

    assert (
        utils.is_primitive_type(
            FhirPrimitiveTypesModel.model_fields["dateTypeRequired"]
        )
        is True
    )

    assert (
        utils.is_primitive_type(
            FhirPrimitiveTypesModel.model_fields["dateListTypeOptional"]
        )
        is True
    )
