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

## NOTE:
# This test originally used `fhir.resources` (e.g., Observation) to validate
# decimal serialization behavior triggered via FHIRAbstractModel.
#
# However, `fhir-core` should not depend on `fhir.resources`, and adding it as a
# test dependency caused unintended side effects in the CI environment.
#
# The serialization logic being tested lives entirely in FHIRAbstractModel
# (within this repo), so the test has been rewritten using a minimal local
# subclass that follows the repo's FHIRAbstractModel test pattern
# (resource_type + Field + elements_sequence) to avoid cross-repo coupling.
#
# This original test is preserved for reference and may be reintroduced in
# `fhir.resources`, where full resource-level integration testing is more appropriate.

#import pytest
#import json
#from pydantic import ValidationError
#from decimal import Decimal
#from fhir.resources.observation import Observation

@pytest.mark.skip(reason="Depends on fhir.resources (cross-repo dependency); replaced by isolated FHIRAbstractModel test")
def test_fhir_resource_issue_230 () : 
    v="19"
    observation_dict = {
        "resourceType": "Observation",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "12345-6"}]},
        "component": [
            {
                "code": {"coding": [{"system": "http://loinc.org", "code": "12345-6"}]},
                "valueQuantity": {
                    "value": v,
                    "unit": "mg/dL",
                    "system": "http://unitsofmeasure.org",
                    "code": "mg/dL",
                },
            }
        ],
    }

    observation = Observation(**observation_dict)
    assert observation.component[0].valueQuantity.value == Decimal(v)
    assert isinstance(observation.component[0].valueQuantity.value, Decimal)
 
    data = json.loads(observation.model_dump_json())
    value = data["component"][0]["valueQuantity"]["value"]
    assert value ==19
    assert isinstance(value, int)
    
    data = observation.model_dump()
    value = data["component"][0]["valueQuantity"]["value"]
    assert value ==19
    assert isinstance(value, int)
  
    v="19.0"
    observation_dict["component"][0]["valueQuantity"]["value"] =v
    observation = Observation(**observation_dict)
    assert observation.component[0].valueQuantity.value == Decimal(v)
    
    data = json.loads(observation.model_dump_json())
    value = data["component"][0]["valueQuantity"]["value"]
    assert value ==19.0
    assert isinstance(value, float)
    
    data = observation.model_dump()
    value = data["component"][0]["valueQuantity"]["value"]
    assert value ==19.0
    assert isinstance(value, float)

    v="19.5"
    observation_dict["component"][0]["valueQuantity"]["value"] =v
    observation = Observation(**observation_dict)
    assert observation.component[0].valueQuantity.value == Decimal(v)
    
    data = json.loads(observation.model_dump_json())
    value = data["component"][0]["valueQuantity"]["value"]
    assert value ==19.5
    assert isinstance(value, float)
    
    data = observation.model_dump()
    value = data["component"][0]["valueQuantity"]["value"]
    assert value ==19.5
    assert isinstance(value, float)

    v="1."
    observation_dict["component"][0]["valueQuantity"]["value"] =v
    with pytest.raises (ValidationError):
        Observation(**observation_dict)
    
    v="01"
    observation_dict["component"][0]["valueQuantity"]["value"] =v
    with pytest.raises (ValidationError):
        Observation(**observation_dict)