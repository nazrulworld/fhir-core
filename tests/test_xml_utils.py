import platform

import lxml.etree  # type: ignore

from fhir_core import xml_utils
from tests.fixtures.resources.patient import Patient

from .fixtures import (
    STATIC_PATH_JSON_EXAMPLES,
    STATIC_PATH_XML_EXAMPLES,
    STATIC_PATH_XML_SCHEMA,
    FhirPrimitiveTypesModel,
    should_ignore_xml_schema_test,
)

__author__ = "Md Nazrul Islam"
__email__ = "email2nazrul@gmail.com>"


def test_xml_represent():
    """ """
    model = FhirPrimitiveTypesModel(
        booleanTypeRequired=False,
        stringTypeRequired="My String",
        stringListTypeRequired=["line"],
        uuidTypeRequired="0f617818-ee6a-4d11-86ff-cf5924038f27",
        dateTypeRequired="1970-01-01",
        base64BinaryTypeRequired="QUxMLUlOLU9ORQ==",
        urlTypeNotRequired="https://schemas.xmlsoap.org/soap/encoding/",
    )
    assert (
        xml_utils.xml_represent(
            model.__class__.model_fields["booleanTypeRequired"],
            model.booleanTypeRequired,
        )
        == "false"
    )
    assert (
        xml_utils.xml_represent(
            model.__class__.model_fields["base64BinaryTypeRequired"],
            model.base64BinaryTypeRequired,
        ).strip()
        == "QUxMLUlOLU9ORQ=="
    )

    assert (
        xml_utils.xml_represent(
            model.__class__.model_fields["uuidTypeRequired"], model.uuidTypeRequired
        )
        == "urn:uuid:0f617818-ee6a-4d11-86ff-cf5924038f27"
    )
    assert (
        xml_utils.xml_represent(
            model.__class__.model_fields["urlTypeNotRequired"], model.urlTypeNotRequired
        )
        == "https://schemas.xmlsoap.org/soap/encoding/"
    )
    assert (
        xml_utils.xml_represent(
            model.__class__.model_fields["dateTypeRequired"], model.dateTypeRequired
        )
        == "1970-01-01"
    )


def test_xml_node_patient_resource():
    """ """
    patient_fhir = Patient.model_validate_json(
        (STATIC_PATH_JSON_EXAMPLES / "patient-example.json").read_bytes()
    )
    patient_node = xml_utils.Node.from_fhir_obj(patient_fhir)
    if should_ignore_xml_schema_test():
        return 1 == 1
    schema = lxml.etree.XMLSchema(file=str(STATIC_PATH_XML_SCHEMA / "patient.xsd"))
    xmlparser = lxml.etree.XMLParser(schema=schema)
    try:
        patient_node.validate(patient_node, xmlparser=xmlparser)
    except ValueError:
        raise AssertionError("code should not come here!")


def test_element_to_node():
    """ """
    if should_ignore_xml_schema_test():
        return 1 == 1
    schema = lxml.etree.XMLSchema(file=str(STATIC_PATH_XML_SCHEMA / "patient.xsd"))
    xmlparser = lxml.etree.XMLParser(schema=schema)
    element = lxml.etree.fromstring(
        (
            STATIC_PATH_XML_EXAMPLES / "patient-example-f001-pieter(f001).xml"
        ).read_bytes(),
        parser=xmlparser,
    )
    patient_node = xml_utils.Node.from_element(element)
    try:
        patient_node.validate(patient_node.to_xml(), xmlparser=xmlparser)
    except ValueError:
        raise AssertionError("Code should not come here!")


def test_model_obj_xml_file():
    """ """
    patient = xml_utils.xml_loads(
        Patient,
        (
            STATIC_PATH_XML_EXAMPLES
            / "patient-example-sex-and-gender(patient-example-sex-and-gender).xml"
        ).read_bytes(),
    )
    if should_ignore_xml_schema_test():
        return 1 == 1
    # with parser parameter
    schema = lxml.etree.XMLSchema(file=str(STATIC_PATH_XML_SCHEMA / "patient.xsd"))
    xmlparser = lxml.etree.XMLParser(schema=schema)
    patient2 = xml_utils.xml_loads(
        Patient,
        (
            STATIC_PATH_XML_EXAMPLES
            / "patient-example-sex-and-gender(patient-example-sex-and-gender).xml"
        ).read_bytes(),
        xmlparser,
    )
    patient3 = xml_utils.xml_loads(
        Patient,
        (
            STATIC_PATH_XML_EXAMPLES
            / "patient-example-sex-and-gender(patient-example-sex-and-gender).xml"
        ).read_bytes(),
    )
    assert patient == patient2
    patient3.text = None
    patient.text = None
    # patient.contained[0].text = None
    # patient3.contained[0].text = None
    assert patient3 == patient
