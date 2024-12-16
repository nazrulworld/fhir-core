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

    assert (
        utils.is_primitive_type(
            FhirPrimitiveTypesModel.model_fields["stringListTypeOptional2"]
        )
        is True
    )


def test_non_primitive_type():
    from tests.fixtures.resources.activitydefinition import ActivityDefinition

    assert (
        utils.is_primitive_type(
            ActivityDefinition.model_fields["observationResultRequirement__ext"]
        )
        is False
    )


def test_primitive_fhir_type_name():
    """ """
    from tests.fixtures.resources.activitydefinition import ActivityDefinition
    from tests.fixtures.resources.identifier import Identifier

    assert utils.get_fhir_type_name(Identifier.model_fields["use"]) == "code"
    assert utils.get_fhir_type_name(Identifier.model_fields["value"]) == "string"

    assert (
        utils.get_fhir_type_name(ActivityDefinition.model_fields["approvalDate"])
        == "date"
    )
    assert (
        utils.get_fhir_type_name(ActivityDefinition.model_fields["asNeededBoolean"])
        == "boolean"
    )

    from tests.fixtures.resources.narrative import Narrative

    assert utils.get_fhir_type_name(Narrative.model_fields["div"]) == "xhtml"


def test_fhir_complex_data_type_name():
    """ """
    from tests.fixtures.resources.activitydefinition import ActivityDefinition

    assert (
        utils.get_fhir_type_name(ActivityDefinition.model_fields["author"])
        == "ContactDetail"
    )
    assert (
        utils.get_fhir_type_name(ActivityDefinition.model_fields["code"])
        == "CodeableConcept"
    )


def test_fhir_resource_type_name():
    """ """
    from tests.fixtures.resources.activitydefinition import ActivityDefinition
    from tests.fixtures.resources.element import Element

    assert (
        utils.get_fhir_type_name(ActivityDefinition.model_fields["dynamicValue"])
        == "ActivityDefinitionDynamicValue"
    )

    assert utils.get_fhir_type_name(Element.model_fields["extension"]) == "Extension"


def test_is_list_type():
    from tests.fixtures.resources.activitydefinition import ActivityDefinition
    from tests.fixtures.resources.element import Element

    assert utils.is_list_type(ActivityDefinition.model_fields["dosage"]) is True
    assert utils.is_list_type(ActivityDefinition.model_fields["doNotPerform"]) is False
    assert utils.is_list_type(Element.model_fields["extension"]) is True
