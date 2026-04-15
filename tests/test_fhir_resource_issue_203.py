import pytest
import json
from pydantic import ValidationError
from decimal import Decimal
from fhir.resources.observation import Observation

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