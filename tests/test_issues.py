import pytest
from lxml import etree
from pydantic import Field

from fhir_core.fhirabstractmodel import FHIRAbstractModel
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
    """Encounter.class missing when serializing to XML.
    https://github.com/nazrulworld/fhir-core/issues/16
    """
    from tests.fixtures.resources.codeableconcept import CodeableConcept
    from tests.fixtures.resources.coding import Coding
    from tests.fixtures.resources.encounter import Encounter

    encounter = Encounter(
        status="active",
        class_fhir=[
            CodeableConcept(
                coding=[
                    Coding(
                        system="http://terminology.hl7.org/CodeSystem/v3-ActCode",
                        code="AMB",
                    ),
                ]
            ),
        ],
    )
    el = etree.fromstring(encounter.model_dump_xml())
    class_el = el.xpath("//fhir:class", namespaces={"fhir": "http://hl7.org/fhir"})
    assert len(class_el) == 1


def test_fhir_resource_issue_202():
    """https://github.com/nazrulworld/fhir.resources/issues/202"""
    from fhir_core.types import create_fhir_type
    from tests.fixtures.resources.R5.age import Age as R5_Age

    AgeType = create_fhir_type("AgeType", "tests.fixtures.resources.age.Age")
    AgeType_R5 = create_fhir_type("AgeType", "tests.fixtures.resources.R5.age.Age")

    assert AgeType._prefix == ""
    assert AgeType_R5._prefix == "R5."
    from fhir_core.constraints import FHIR_TYPES_MAPS

    assert FHIR_TYPES_MAPS["AgeType"] == "tests.fixtures.resources.age.Age"
    assert FHIR_TYPES_MAPS["R5.AgeType"] == "tests.fixtures.resources.R5.age.Age"

    class PatientCustom(FHIRAbstractModel):
        __resource_type__ = "Patient"
        age: AgeType_R5 = Field(..., alias="age", title="Patient age")

        @classmethod
        def elements_sequence(cls):
            """returning all element names from
            ``Age`` according to specification,
            with preserving the original sequence order.
            """
            return ["age"]

    pat = PatientCustom(age=R5_Age(value=10, unit="y"))
    # NOTE: Serializer change now preserves integer form for whole-number Decimals
    # (e.g. 10 instead of 10.0). This removes artificial floating-point precision
    # that was previously introduced during model_dump_json() serialization.
    # Both representations are valid JSON, but this aligns better with FHIR numeric semantics.
    assert pat.model_dump_json() == '{"age":{"value":10,"unit":"y"}}'
