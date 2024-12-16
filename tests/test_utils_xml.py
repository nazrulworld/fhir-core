import lxml.etree  # type: ignore

from fhir_core import xml_utils
from tests.fixtures.resources.patient import Patient

from .fixtures import (
    STATIC_PATH,
    STATIC_PATH_JSON_EXAMPLES,
    STATIC_PATH_XML_EXAMPLES,
    STATIC_PATH_XML_SCHEMA,
)

__author__ = "Md Nazrul Islam"
__email__ = "email2nazrul@gmail.com>"


def offtest_xml_node_patient_resource():
    """Accept-Charset: utf-8
    Accept: application/fhir+xml;q=1.0, application/xml+fhir;q=0.9
    User-Agent: HAPI-FHIR/5.3.0 (FHIR Client; FHIR 4.0.1/R4; apache)
    Accept-Encoding: gzip
    Content-Type: application/fhir+xml; charset=UTF-8
    """
    patient_fhir = Patient.model_validate_json(
        (STATIC_PATH_JSON_EXAMPLES / "Patient-with-ext.json").read_bytes()
    )
    patient_node = xml_utils.Node.from_fhir_obj(patient_fhir)

    schema = lxml.etree.XMLSchema(file=str(STATIC_PATH_XML_SCHEMA / "patient.xsd"))
    xmlparser = lxml.etree.XMLParser(schema=schema)
    try:
        patient_node.validate(patient_node, xmlparser=xmlparser)
    except ValueError:
        raise AssertionError("code should not come here!")


def offtest_element_to_node():
    """ """
    schema = lxml.etree.XMLSchema(file=str(STATIC_PATH_XML_SCHEMA / "patient.xsd"))
    xmlparser = lxml.etree.XMLParser(schema=schema)
    element = lxml.etree.fromstring(
        (STATIC_PATH / "Patient-with-ext.xml").read_bytes(),
        parser=xmlparser,
    )
    patient_node = xml_utils.Node.from_element(element)
    try:
        patient_node.validate(patient_node.to_xml(), xmlparser=xmlparser)
    except ValueError:
        raise AssertionError("Code should not come here!")


def offtest_model_obj_xml_file():
    """ """
    patient = xml_utils.xml_loads(
        Patient, (STATIC_PATH_XML_EXAMPLES / "Patient-with-ext.xml").read_bytes()
    )
    # with parser parameter
    schema = lxml.etree.XMLSchema(file=str(STATIC_PATH_XML_SCHEMA / "patient.xsd"))
    xmlparser = lxml.etree.XMLParser(schema=schema)
    patient2 = xml_utils.xml_loads(
        Patient,
        (STATIC_PATH_XML_EXAMPLES / "Patient-with-ext.xml").read_bytes(),
        xmlparser,
    )
    patient3 = xml_utils.xml_loads(
        Patient, (STATIC_PATH_XML_EXAMPLES / "Patient-with-ext.xml").read_bytes()
    )
    assert patient == patient2
    patient3.text = None
    patient.text = None
    patient.contained[1].text = None
    patient3.contained[1].text = None
    assert patient3 == patient
