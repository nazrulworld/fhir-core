import pytest

from tests.fixtures import (
    STATIC_PATH_JSON_EXAMPLES,
    STATIC_PATH_XML,
    STATIC_PATH_XML_SCHEMA,
    should_ignore_xml_schema_test,
)

__author__ = "Md Nazrul Islam"
__email__ = "email2nazrul@gmail.com"


def test_issue_external_175():
    """https://github.com/nazrulworld/fhir.resources/issues/175
    Library fails when an array replaces an object in Patient resource
    """
    from pydantic_core._pydantic_core import ValidationError

    from tests.fixtures.resources.patient import Patient

    try:
        Patient.model_validate_json(
            (
                STATIC_PATH_JSON_EXAMPLES / "patient-issue-175-wrong-meta-value.json"
            ).read_bytes()
        )
    except AttributeError as e:
        pytest.fail("It seems the problem is not solved!", e)
    except ValidationError as e:
        assert (
            "Value is expected from the instance of Meta, but got type <class 'list'>"
            in str(e)
        )


def test_issue_12():
    """Missing xmlparser argument for FHIRAbstractModel.model_validate_xml
    @url: https://github.com/nazrulworld/fhir-core/issues/12
    """
    from lxml import etree

    from tests.fixtures.resources.patient import Patient

    if should_ignore_xml_schema_test():
        return 1 == 1
    schema = etree.XMLSchema(file=str(STATIC_PATH_XML_SCHEMA / "patient.xsd"))
    xmlparser = etree.XMLParser(schema=schema)
    try:
        Patient.model_validate_xml(
            (STATIC_PATH_XML / "examples" / "patient-example-a(pat1).xml").read_bytes(),
            xmlparser=xmlparser,
        )
    except ValueError:
        raise AssertionError("code should not come here!")


def test_issue_16():
    """Serialize a FHIR resource with a non-matching alias for a field name"""
    from fhir_core import xml_utils

    from tests.fixtures.resources.encounter import Encounter

    encounter_fhir = xml_utils.xml_loads(
        Encounter,
        (
            STATIC_PATH_XML / "examples" / "encounter-example-f001-heart(f001).xml"
        ).read_bytes(),
    )

    encounter_node = xml_utils.Node.from_fhir_obj(encounter_fhir)
    encounter_byt = encounter_node.to_string()

    assert b"<class>" in encounter_byt
