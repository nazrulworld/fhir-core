import pytest
import json
import decimal
from pydantic import ValidationError, Field

from fhir_core.fhirabstractmodel import FHIRAbstractModel
from fhir_core.types import Decimal as FHIRDecimal


class DummyQuantity(FHIRAbstractModel):
    __resource_type__ = "DummyQuantity"

    value: FHIRDecimal = Field(..., alias="value", title="Decimal value")

    @classmethod
    def elements_sequence(cls):
        return ["value"]


def test_fhir_core_decimal_serialization_issue_230():
    v = "19"

    obj = DummyQuantity(value=v)

    # ensure proper Decimal coercion
    assert obj.value == decimal.Decimal(v)
    assert isinstance(obj.value, decimal.Decimal)

    # dict output
    data = obj.model_dump()
    assert data["value"] == 19
    assert isinstance(data["value"], int)

    # json output
    data = json.loads(obj.model_dump_json())
    assert data["value"] == 19
    assert isinstance(data["value"], int)

    # float case
    v = "19.0"
    obj = DummyQuantity(value=v)
    assert obj.value == decimal.Decimal(v)

    data = obj.model_dump()
    assert data["value"] == 19.0
    assert isinstance(data["value"], float)

    v = "19.5"
    obj = DummyQuantity(value=v)
    assert obj.value == decimal.Decimal(v)

    data = obj.model_dump()
    assert data["value"] == 19.5
    assert isinstance(data["value"], float)

    # invalid formats (FHIR validation)
    v = "1."
    with pytest.raises(ValidationError):
        DummyQuantity(value=v)

    v = "01"
    with pytest.raises(ValidationError):
        DummyQuantity(value=v)
