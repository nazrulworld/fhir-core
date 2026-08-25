import json
import re
import uuid

from pydantic import Field

from fhir_core.fhirabstractmodel import FHIRAbstractModel
from fhir_core.types import UuidType

# https://hl7.org/fhir/R5/datatypes.html#uuid
SPEC_PATTERN = re.compile(
    r"^urn:uuid:[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"
)


class DummyUuidHolder(FHIRAbstractModel):
    __resource_type__ = "DummyUuidHolder"

    valueUuid: UuidType = Field(..., alias="valueUuid", title="Uuid value")

    @classmethod
    def elements_sequence(cls):
        return ["valueUuid"]


def test_fhir_core_uuid_serialization_issue_180():
    """A FHIR uuid is a URI: it is written as urn:uuid:<uuid> or it does not
    match the specification."""
    canonical = "5f633a6a-398f-423c-a0d5-d254b51f487c"
    expected = "urn:uuid:" + canonical

    # every form the type accepts must come out as the same URI
    for accepted in (
        canonical,
        expected,
        "5f633a6a398f423ca0d5d254b51f487c",
        canonical.upper(),
        uuid.UUID(canonical),
    ):
        obj = DummyUuidHolder(valueUuid=accepted)
        # the python-side type is unchanged
        assert isinstance(obj.valueUuid, uuid.UUID)

        assert obj.model_dump()["valueUuid"] == expected
        data = json.loads(obj.model_dump_json())
        assert data["valueUuid"] == expected
        assert SPEC_PATTERN.match(data["valueUuid"])

    # the prefix is not doubled when the output is read back and written again
    obj = DummyUuidHolder(valueUuid=canonical)
    for _ in range(3):
        obj = DummyUuidHolder.model_validate_json(obj.model_dump_json())
        assert json.loads(obj.model_dump_json())["valueUuid"] == expected
