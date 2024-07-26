from typing_extensions import Annotated as _Annotated
from typing_extensions import List

from fhir_core.types import *

__author__ = "Md Nazrul Islam"
__email__ = "email2nazrul@gmail.com"

AddressType = create_fhir_type(
    "AddressType", model_klass="tests.fixtures.resources.address.Address"
)
CodingType = create_fhir_type(
    "CodingType", model_klass="tests.fixtures.resources.coding.Coding"
)
PeriodType = create_fhir_type(
    "PeriodType", model_klass="tests.fixtures.resources.period.Period"
)
MetaType = create_fhir_type(
    "MetaType", model_klass="tests.fixtures.resources.meta.Meta"
)
ExtensionType = create_fhir_type(
    "ExtensionType", model_klass="tests.fixtures.resources.extension.Extension"
)
FHIRPrimitiveExtensionType = create_fhir_type(
    "FHIRPrimitiveExtensionType",
    model_klass="tests.fixtures.resources.fhirprimitiveextension.FHIRPrimitiveExtension",
)
ResourceType = create_fhir_type(
    "ResourceType", model_klass="tests.fixtures.resources.resource.Resource"
)
NarrativeType = create_fhir_type(
    "NarrativeType", model_klass="tests.fixtures.resources.narrative.Narrative"
)
QuantityType = create_fhir_type(
    "QuantityType", model_klass="tests.fixtures.resources.quantity.Quantity"
)
AgeType = create_fhir_type("AgeType", model_klass="tests.fixtures.resources.age.Age")
ReferenceType = create_fhir_type(
    "ReferenceType", model_klass="tests.fixtures.resources.reference.Reference"
)
IdentifierType = create_fhir_type(
    "IdentifierType", model_klass="tests.fixtures.resources.identifier.Identifier"
)
CodeableConceptType = create_fhir_type(
    "CodeableConceptType",
    model_klass="tests.fixtures.resources.codeableconcept.CodeableConcept",
)
AnnotationType = create_fhir_type(
    "AnnotationType", model_klass="tests.fixtures.resources.annotation.Annotation"
)
