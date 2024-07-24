from fhir_core.types import *

__author__ = "Md Nazrul Islam"
__email__ = "email2nazrul@gmail.com"

AddressType = FhirBase(model_klass="tests.fixtures.resources.address.Address")
CodingType = FhirBase(model_klass="tests.fixtures.resources.coding.Coding")
PeriodType = FhirBase(model_klass="tests.fixtures.resources.period.Period")
MetaType = FhirBase(model_klass="tests.fixtures.resources.meta.Meta")
ExtensionType = FhirBase(model_klass="tests.fixtures.resources.extension.Extension")
FHIRPrimitiveExtensionType = FhirBase(
    model_klass="tests.fixtures.resources.fhirprimitiveextension.FHIRPrimitiveExtension"
)
ResourceType = FhirBase(model_klass="tests.fixtures.resources.resource.Resource")
NarrativeType = FhirBase(model_klass="tests.fixtures.resources.narrative.Narrative")
