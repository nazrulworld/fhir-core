from fhir_core.yaml_utils import yaml_dumps, yaml_loads
from tests.fixtures import STATIC_PATH
from tests.fixtures.resources.account import Account
from tests.fixtures.resources.activitydefinition import ActivityDefinition
from tests.fixtures.resources.auditevent import AuditEvent

__author__ = "Md Nazrul Islam"
__email__ = "email2nazrul@gmail.com"


def test_account_loads_and_dumps():
    """"""
    account_model = Account.model_validate_json(
        (STATIC_PATH / "account-example.json").read_bytes()
    )
    yaml_str = yaml_dumps(account_model.model_dump())
    account_model2 = Account.model_validate(yaml_loads(yaml_str))
    assert account_model.model_dump() == account_model2.model_dump()


def test_audit_event_loads_and_dumps():
    """ """
    audit_model = AuditEvent.model_validate_json(
        (STATIC_PATH / "audit-event-example-search.json").read_bytes()
    )
    yaml_str = yaml_dumps(audit_model.model_dump())
    audit_model2 = AuditEvent.model_validate(yaml_loads(yaml_str))
    assert audit_model.model_dump() == audit_model2.model_dump()


def test_activitydefinition_loads_and_dumps():
    """ """
    activitydefinition_model = ActivityDefinition.model_validate_json(
        (STATIC_PATH / "activitydefinition-medicationorder-example.json").read_bytes()
    )
    yaml_str = yaml_dumps(activitydefinition_model.model_dump())
    activitydefinition_model2 = ActivityDefinition.model_validate(yaml_loads(yaml_str))
    assert (
        activitydefinition_model.model_dump() == activitydefinition_model2.model_dump()
    )
