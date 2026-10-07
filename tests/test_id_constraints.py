"""Regression tests for https://github.com/nazrulworld/fhir.resources/issues/173.

In v7, ``Id.configure_constraints(...)`` allowed relaxing the ``id`` regex
and length limit for dirty source data. In v8 the ``Id`` class moved to
fhir-core and the only documented escape hatch (patching
``fhir_core.constraints.TYPES_ID_MAX_LENGTH``) silently did nothing, because
``Id.max_length`` was bound at class definition time; the pattern could not
be relaxed at all.
"""

import pytest
from pydantic import BaseModel, ValidationError

import fhir_core.constraints as constraints
from fhir_core.types import IdType


@pytest.fixture
def restore_constraints():
    max_length = constraints.TYPES_ID_MAX_LENGTH
    pattern = constraints.TYPES_ID_PATTERN
    yield
    constraints.TYPES_ID_MAX_LENGTH = max_length
    constraints.TYPES_ID_PATTERN = pattern


def make_model():
    # NOTE: the model class (and therefore its pydantic core schema) must be
    # defined *after* patching the constraints module.

    class Model(BaseModel):
        id: IdType

    return Model


def test_id_defaults(restore_constraints):
    Model = make_model()
    assert Model(id="abc-123.456").id == "abc-123.456"
    with pytest.raises(ValidationError):
        Model(id="with_underscore")
    with pytest.raises(ValidationError):
        Model(id="a" * 256)
    with pytest.raises(ValidationError):
        Model(id="")


def test_id_max_length_patch_is_honored(restore_constraints):
    constraints.TYPES_ID_MAX_LENGTH = 1024 * 1024
    Model = make_model()
    assert Model(id="a" * 1000).id == "a" * 1000
    with pytest.raises(ValidationError):
        Model(id="a" * (1024 * 1024 + 1))


def test_id_pattern_patch_is_honored(restore_constraints):
    constraints.TYPES_ID_PATTERN = r"^[A-Za-z0-9\-_.]+$"
    Model = make_model()
    assert Model(id="with_underscore").id == "with_underscore"
    # other constraints still apply
    with pytest.raises(ValidationError):
        Model(id="with space")
    with pytest.raises(ValidationError):
        Model(id="a" * 256)


def test_id_constraints_can_be_disabled(restore_constraints):
    constraints.TYPES_ID_MAX_LENGTH = None
    constraints.TYPES_ID_PATTERN = None
    Model = make_model()
    assert Model(id="a" * 10000).id == "a" * 10000
    assert Model(id="anything goes!").id == "anything goes!"
