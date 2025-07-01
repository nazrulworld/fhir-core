import typing

import pytest
from lxml import etree
from pydantic import Field, ValidationError

from fhir_core.fhirabstractmodel import FHIRAbstractModel
from fhir_core.types import Base64BinaryType
from tests.fixtures import (
    STATIC_PATH_JSON_EXAMPLES,
    STATIC_PATH_XML_EXAMPLES,
    STATIC_PATH_YAML_EXAMPLES,
)
from tests.fixtures.resources import fhirtypes
from tests.fixtures.resources.domainresource import DomainResource
from tests.fixtures.resources.fhirtypes import FHIRPrimitiveExtensionType
from tests.fixtures.resources.resource import Resource

__author__ = "Md Nazrul Islam"
__email__ = "email2nazrul@gmail.com"


def test_has_resource_base():
    """ """

    class MyNewResource(Resource):
        __resource_type__ = "MyNewResource"

    model = MyNewResource()
    assert model.has_resource_base() is True


def test_get_alias_mapping():
    """ """
    from tests.fixtures.resources.address import Address

    mappings = Address.get_alias_mapping()
    assert len(mappings) == 12


def test_primitive_fields():
    """ """

    class MyPrimitivesValueFieldsModel(DomainResource):
        __resource_type__ = "MyPrimitivesValueFieldsModel"

        name: fhirtypes.StringType = Field(
            None,
            alias="name",
            title="Full Name",
            json_schema_extra={"element_property": True, "element_required": True},
        )
        name__ext: FHIRPrimitiveExtensionType = Field(
            None, alias="_name", title="Extension field for ``type``."
        )
        postCode: fhirtypes.IntegerType = Field(
            None,
            alias="post-code",
            title="Postcode",
            json_schema_extra={"element_property": True},
        )
        active: fhirtypes.BooleanType = Field(
            None,
            alias="active",
            title="Active",
            json_schema_extra={"element_property": True},
        )

        @classmethod
        def elements_sequence(cls):
            return DomainResource.elements_sequence() + ["name", "post-code", "active"]

        def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
            """This method should be overridden in each subclass.
            [("type", "type__ext")]"""
            return [("name", "name__ext")]

    obj = MyPrimitivesValueFieldsModel(
        name="Kim Larson", postCode=1230, active=True, meta={"id": "001"}
    )

    serialized_data = obj.model_dump()
    assert serialized_data["post-code"] == 1230

    with pytest.raises(ValidationError) as exception_info:
        MyPrimitivesValueFieldsModel(postCode=1230, active=True, meta={"id": "001"})

    assert "Value for the field 'name' is required" in str(exception_info.value)

    # test with extension
    obj = MyPrimitivesValueFieldsModel(
        postCode=1230,
        active=True,
        meta={"id": "001"},
        name__ext={"extension": [{"valueString": "different name"}]},
    )
    assert obj.model_dump()["_name"]["extension"][0]["valueString"] == "different name"
    json_str = obj.model_dump_json()
    MyPrimitivesValueFieldsModel.model_validate_json(json_str)

    # Test with comments
    obj = MyPrimitivesValueFieldsModel(
        postCode=1230,
        active=True,
        meta={"id": "001"},
        name__ext={
            "extension": [{"valueString": "different name"}],
            "fhir_comments": "This is experiemental",
        },
    )
    # need proper handling of exclude comments
    serialized_data = obj.model_dump(exclude_comments=True)


def test_model_dump_serialization():
    """ """
    from tests.fixtures.resources.account import Account

    filename = STATIC_PATH_JSON_EXAMPLES / "account-example.json"
    obj = Account.model_validate_json(filename.read_bytes())
    serialized_data = obj.model_dump()
    assert Account.model_validate(serialized_data).model_dump() == serialized_data
    assert (
        Account.model_validate_json(obj.model_dump_json()).model_dump()
        == serialized_data
    )


def test_general_resource_validation():
    """ """
    from tests.fixtures.resources.activitydefinition import ActivityDefinition

    filename = (
        STATIC_PATH_JSON_EXAMPLES / "activitydefinition-medicationorder-example.json"
    )
    obj = ActivityDefinition.model_validate_json(filename.read_bytes())
    serialized_data = obj.model_dump()
    assert (
        ActivityDefinition.model_validate(serialized_data).model_dump()
        == serialized_data
    )
    assert (
        ActivityDefinition.model_validate_json(obj.model_dump_json()).model_dump()
        == serialized_data
    )


def test_base64binary_validation():
    """ """

    class Base64BinaryModel(FHIRAbstractModel):
        base64BinaryListTypeOptionalList: typing.Optional[
            typing.List[Base64BinaryType]
        ] = Field(None, alias="base64BinaryListTypeOptionalList")
        base64Binary: Base64BinaryType = Field(None, alias="base64Binary")

        @classmethod
        def elements_sequence(cls):
            return ["base64BinaryListTypeOptionalList", "base64Binary"]

    obj = Base64BinaryModel(
        base64BinaryListTypeOptionalList=[b"aGVs"], base64Binary=b"aGVs\n"
    )
    obj.model_dump()
    assert (
        Base64BinaryModel.model_validate(obj.model_dump()).base64Binary
        == obj.base64Binary
    )

    from tests.fixtures.resources.auditevent import AuditEvent

    filename = STATIC_PATH_JSON_EXAMPLES / "audit-event-example-search.json"
    obj = AuditEvent.model_validate_json(filename.read_bytes())
    serialized_data = obj.model_dump()
    assert AuditEvent.model_validate(serialized_data).model_dump() == serialized_data
    assert (
        AuditEvent.model_validate_json(obj.model_dump_json()).model_dump()
        == serialized_data
    )


def test_model_from_yaml():
    """ """
    from tests.fixtures.resources.activitydefinition import ActivityDefinition

    filename = (
        STATIC_PATH_YAML_EXAMPLES / "activitydefinition-medicationorder-example.yaml"
    )
    obj = ActivityDefinition.model_validate_yaml(filename.read_bytes())
    obj2 = ActivityDefinition.model_validate_json(
        (
            STATIC_PATH_JSON_EXAMPLES
            / "activitydefinition-medicationorder-example.json"
        ).read_bytes()
    )
    assert obj.model_dump() == obj2.model_dump()


def test_model_dump_yaml():
    """ """
    from tests.fixtures.resources.activitydefinition import ActivityDefinition

    filename = (
        STATIC_PATH_YAML_EXAMPLES / "activitydefinition-medicationorder-example.yaml"
    )

    obj = ActivityDefinition.model_validate_json(
        (
            STATIC_PATH_JSON_EXAMPLES
            / "activitydefinition-medicationorder-example.json"
        ).read_bytes()
    )
    assert obj.model_dump_yaml() == filename.read_text()


def test_model_attachment_max_size():
    """ """
    import sys

    from tests.fixtures.resources.attachment import Attachment

    filename = STATIC_PATH_JSON_EXAMPLES / "attachment-example.json"

    attachment = Attachment.model_validate_json(filename.read_bytes())
    assert attachment.size == sys.maxsize, "Attachment.size should be sys.maxsize"


def test_model_from_xml():
    """ """
    from tests.fixtures.resources.activitydefinition import ActivityDefinition

    filename = (
        STATIC_PATH_XML_EXAMPLES
        / "activitydefinition-medicationorder-example(citalopramPrescription).xml"
    )
    obj = ActivityDefinition.model_validate_xml(filename.read_bytes())

    obj2 = ActivityDefinition.model_validate_json(
        (
            STATIC_PATH_JSON_EXAMPLES
            / "activitydefinition-medicationorder-example(citalopramPrescription).json"
        ).read_bytes()
    )
    assert obj.model_dump() == obj2.model_dump()


def test_model_dump_xml():
    """ """
    from tests.fixtures.resources.activitydefinition import ActivityDefinition

    filename = (
        STATIC_PATH_XML_EXAMPLES
        / "activitydefinition-medicationorder-example(citalopramPrescription).xml"
    )

    obj = ActivityDefinition.model_validate_json(
        (
            STATIC_PATH_JSON_EXAMPLES
            / "activitydefinition-medicationorder-example(citalopramPrescription).json"
        ).read_bytes()
    )
    activitydefinition_el_1 = etree.fromstring(filename.read_bytes())
    activitydefinition_el_2 = etree.fromstring(obj.model_dump_xml())
    assert len(activitydefinition_el_1) == len(activitydefinition_el_2)
    # assert etree.tostring(activitydefinition_el_1) == etree.tostring(activitydefinition_el_2)


def test_model_serialize_with_summary_fields():
    """ """
    from tests.fixtures.resources.account import Account

    filename = STATIC_PATH_JSON_EXAMPLES / "account-example.json"
    account_obj = Account.model_validate_json(filename.read_bytes())
    non_summary_fields = [
        f
        for f in Account.elements_sequence()
        if f not in Account.summary_elements_sequence()
    ]
    account_dict = account_obj.model_dump(summary_only=True)
    for field in non_summary_fields:
        assert field not in account_dict.keys()

    assert len(account_obj.model_dump(summary_only=False).keys()) > len(
        account_dict.keys()
    )


def test_model_json_serialize_with_summary_fields():
    """ """
    from tests.fixtures.resources.account import Account

    filename = STATIC_PATH_JSON_EXAMPLES / "account-example.json"
    account_obj = Account.model_validate_json(filename.read_bytes())

    assert len(account_obj.model_dump_json(summary_only=False)) > len(
        account_obj.model_dump_json(summary_only=True)
    )


def test_model_yaml_serialize_with_summary_fields():
    """ """
    from tests.fixtures.resources.account import Account

    filename = STATIC_PATH_JSON_EXAMPLES / "account-example.json"
    account_obj = Account.model_validate_json(filename.read_bytes())

    assert len(account_obj.model_dump_yaml(summary_only=False)) > len(
        account_obj.model_dump_yaml(summary_only=True)
    )

def test_model_xml_serialize_with_summary_fields():
    """ """
    from tests.fixtures.resources.account import Account

    filename = STATIC_PATH_JSON_EXAMPLES / "account-example.json"
    account_obj = Account.model_validate_json(filename.read_bytes())

    assert len(account_obj.model_dump_xml(summary_only=False)) > len(
        account_obj.model_dump_xml(summary_only=True)
    )
