from __future__ import annotations as _annotations

from fhir_core.types import (
    Base64BinaryType,
    BooleanType,
    CanonicalType,
    CodeType,
    DateTimeType,
    DateType,
    DecimalType,
    IdType,
    InstantType,
    Integer64Type,
    IntegerType,
    MarkdownType,
    OidType,
    PositiveIntType,
    StringType,
    TimeType,
    UnsignedIntType,
    UriType,
    UrlType,
    UuidType,
    XhtmlType,
    create_fhir_element_or_resource_type,
    create_fhir_type,
)

__author__ = "Md Nazrul Islam"
__email__ = "email2nazrul@gmail.com"


FHIRPrimitiveExtensionType = create_fhir_type(
    "FHIRPrimitiveExtensionType",
    "tests.fixtures.resources.fhirprimitiveextension.FHIRPrimitiveExtension",
)
AccountType = create_fhir_type(
    "AccountType", "tests.fixtures.resources.account.Account"
)

AccountBalanceType = create_fhir_type(
    "AccountBalanceType", "tests.fixtures.resources.account.AccountBalance"
)

AccountCoverageType = create_fhir_type(
    "AccountCoverageType", "tests.fixtures.resources.account.AccountCoverage"
)

AccountDiagnosisType = create_fhir_type(
    "AccountDiagnosisType", "tests.fixtures.resources.account.AccountDiagnosis"
)

AccountGuarantorType = create_fhir_type(
    "AccountGuarantorType", "tests.fixtures.resources.account.AccountGuarantor"
)

AccountProcedureType = create_fhir_type(
    "AccountProcedureType", "tests.fixtures.resources.account.AccountProcedure"
)

AccountRelatedAccountType = create_fhir_type(
    "AccountRelatedAccountType",
    "tests.fixtures.resources.account.AccountRelatedAccount",
)

ActivityDefinitionType = create_fhir_type(
    "ActivityDefinitionType",
    "tests.fixtures.resources.activitydefinition.ActivityDefinition",
)

ActivityDefinitionDynamicValueType = create_fhir_type(
    "ActivityDefinitionDynamicValueType",
    "tests.fixtures.resources.activitydefinition.ActivityDefinitionDynamicValue",
)

ActivityDefinitionParticipantType = create_fhir_type(
    "ActivityDefinitionParticipantType",
    "tests.fixtures.resources.activitydefinition.ActivityDefinitionParticipant",
)

ActorDefinitionType = create_fhir_type(
    "ActorDefinitionType", "tests.fixtures.resources.actordefinition.ActorDefinition"
)

AddressType = create_fhir_type(
    "AddressType", "tests.fixtures.resources.address.Address"
)

AdministrableProductDefinitionType = create_fhir_type(
    "AdministrableProductDefinitionType",
    "tests.fixtures.resources.administrableproductdefinition.AdministrableProductDefinition",
)

AdministrableProductDefinitionPropertyType = create_fhir_type(
    "AdministrableProductDefinitionPropertyType",
    "tests.fixtures.resources.administrableproductdefinition.AdministrableProductDefinitionProperty",
)

AdministrableProductDefinitionRouteOfAdministrationType = create_fhir_type(
    "AdministrableProductDefinitionRouteOfAdministrationType",
    "tests.fixtures.resources.administrableproductdefinition.AdministrableProductDefinitionRouteOfAdministration",
)

AdministrableProductDefinitionRouteOfAdministrationTargetSpeciesType = create_fhir_type(
    "AdministrableProductDefinitionRouteOfAdministrationTargetSpeciesType",
    "tests.fixtures.resources.administrableproductdefinition.AdministrableProductDefinitionRouteOfAdministrationTargetSpecies",
)

AdministrableProductDefinitionRouteOfAdministrationTargetSpeciesWithdrawalPeriodType = create_fhir_type(
    "AdministrableProductDefinitionRouteOfAdministrationTargetSpeciesWithdrawalPeriodType",
    "tests.fixtures.resources.administrableproductdefinition.AdministrableProductDefinitionRouteOfAdministrationTargetSpeciesWithdrawalPeriod",
)

AdverseEventType = create_fhir_type(
    "AdverseEventType", "tests.fixtures.resources.adverseevent.AdverseEvent"
)

AdverseEventContributingFactorType = create_fhir_type(
    "AdverseEventContributingFactorType",
    "tests.fixtures.resources.adverseevent.AdverseEventContributingFactor",
)

AdverseEventMitigatingActionType = create_fhir_type(
    "AdverseEventMitigatingActionType",
    "tests.fixtures.resources.adverseevent.AdverseEventMitigatingAction",
)

AdverseEventParticipantType = create_fhir_type(
    "AdverseEventParticipantType",
    "tests.fixtures.resources.adverseevent.AdverseEventParticipant",
)

AdverseEventPreventiveActionType = create_fhir_type(
    "AdverseEventPreventiveActionType",
    "tests.fixtures.resources.adverseevent.AdverseEventPreventiveAction",
)

AdverseEventSupportingInfoType = create_fhir_type(
    "AdverseEventSupportingInfoType",
    "tests.fixtures.resources.adverseevent.AdverseEventSupportingInfo",
)

AdverseEventSuspectEntityType = create_fhir_type(
    "AdverseEventSuspectEntityType",
    "tests.fixtures.resources.adverseevent.AdverseEventSuspectEntity",
)

AdverseEventSuspectEntityCausalityType = create_fhir_type(
    "AdverseEventSuspectEntityCausalityType",
    "tests.fixtures.resources.adverseevent.AdverseEventSuspectEntityCausality",
)

AgeType = create_fhir_type("AgeType", "tests.fixtures.resources.age.Age")

AllergyIntoleranceType = create_fhir_type(
    "AllergyIntoleranceType",
    "tests.fixtures.resources.allergyintolerance.AllergyIntolerance",
)

AllergyIntoleranceParticipantType = create_fhir_type(
    "AllergyIntoleranceParticipantType",
    "tests.fixtures.resources.allergyintolerance.AllergyIntoleranceParticipant",
)

AllergyIntoleranceReactionType = create_fhir_type(
    "AllergyIntoleranceReactionType",
    "tests.fixtures.resources.allergyintolerance.AllergyIntoleranceReaction",
)

AnnotationType = create_fhir_type(
    "AnnotationType", "tests.fixtures.resources.annotation.Annotation"
)

AppointmentType = create_fhir_type(
    "AppointmentType", "tests.fixtures.resources.appointment.Appointment"
)

AppointmentParticipantType = create_fhir_type(
    "AppointmentParticipantType",
    "tests.fixtures.resources.appointment.AppointmentParticipant",
)

AppointmentRecurrenceTemplateType = create_fhir_type(
    "AppointmentRecurrenceTemplateType",
    "tests.fixtures.resources.appointment.AppointmentRecurrenceTemplate",
)

AppointmentRecurrenceTemplateMonthlyTemplateType = create_fhir_type(
    "AppointmentRecurrenceTemplateMonthlyTemplateType",
    "tests.fixtures.resources.appointment.AppointmentRecurrenceTemplateMonthlyTemplate",
)

AppointmentRecurrenceTemplateWeeklyTemplateType = create_fhir_type(
    "AppointmentRecurrenceTemplateWeeklyTemplateType",
    "tests.fixtures.resources.appointment.AppointmentRecurrenceTemplateWeeklyTemplate",
)

AppointmentRecurrenceTemplateYearlyTemplateType = create_fhir_type(
    "AppointmentRecurrenceTemplateYearlyTemplateType",
    "tests.fixtures.resources.appointment.AppointmentRecurrenceTemplateYearlyTemplate",
)

AppointmentResponseType = create_fhir_type(
    "AppointmentResponseType",
    "tests.fixtures.resources.appointmentresponse.AppointmentResponse",
)

ArtifactAssessmentType = create_fhir_type(
    "ArtifactAssessmentType",
    "tests.fixtures.resources.artifactassessment.ArtifactAssessment",
)

ArtifactAssessmentContentType = create_fhir_type(
    "ArtifactAssessmentContentType",
    "tests.fixtures.resources.artifactassessment.ArtifactAssessmentContent",
)

AttachmentType = create_fhir_type(
    "AttachmentType", "tests.fixtures.resources.attachment.Attachment"
)

AuditEventType = create_fhir_type(
    "AuditEventType", "tests.fixtures.resources.auditevent.AuditEvent"
)

AuditEventAgentType = create_fhir_type(
    "AuditEventAgentType", "tests.fixtures.resources.auditevent.AuditEventAgent"
)

AuditEventEntityType = create_fhir_type(
    "AuditEventEntityType", "tests.fixtures.resources.auditevent.AuditEventEntity"
)

AuditEventEntityDetailType = create_fhir_type(
    "AuditEventEntityDetailType",
    "tests.fixtures.resources.auditevent.AuditEventEntityDetail",
)

AuditEventOutcomeType = create_fhir_type(
    "AuditEventOutcomeType", "tests.fixtures.resources.auditevent.AuditEventOutcome"
)

AuditEventSourceType = create_fhir_type(
    "AuditEventSourceType", "tests.fixtures.resources.auditevent.AuditEventSource"
)

AvailabilityType = create_fhir_type(
    "AvailabilityType", "tests.fixtures.resources.availability.Availability"
)

AvailabilityAvailableTimeType = create_fhir_type(
    "AvailabilityAvailableTimeType",
    "tests.fixtures.resources.availability.AvailabilityAvailableTime",
)

AvailabilityNotAvailableTimeType = create_fhir_type(
    "AvailabilityNotAvailableTimeType",
    "tests.fixtures.resources.availability.AvailabilityNotAvailableTime",
)

BackboneElementType = create_fhir_type(
    "BackboneElementType", "tests.fixtures.resources.backboneelement.BackboneElement"
)

BackboneTypeType = create_fhir_type(
    "BackboneTypeType", "tests.fixtures.resources.backbonetype.BackboneType"
)

BaseType = create_fhir_type("BaseType", "tests.fixtures.resources.base.Base")

BasicType = create_fhir_type("BasicType", "tests.fixtures.resources.basic.Basic")

BinaryType = create_fhir_type("BinaryType", "tests.fixtures.resources.binary.Binary")

BiologicallyDerivedProductType = create_fhir_type(
    "BiologicallyDerivedProductType",
    "tests.fixtures.resources.biologicallyderivedproduct.BiologicallyDerivedProduct",
)

BiologicallyDerivedProductCollectionType = create_fhir_type(
    "BiologicallyDerivedProductCollectionType",
    "tests.fixtures.resources.biologicallyderivedproduct.BiologicallyDerivedProductCollection",
)

BiologicallyDerivedProductDispenseType = create_fhir_type(
    "BiologicallyDerivedProductDispenseType",
    "tests.fixtures.resources.biologicallyderivedproductdispense.BiologicallyDerivedProductDispense",
)

BiologicallyDerivedProductDispensePerformerType = create_fhir_type(
    "BiologicallyDerivedProductDispensePerformerType",
    "tests.fixtures.resources.biologicallyderivedproductdispense.BiologicallyDerivedProductDispensePerformer",
)

BiologicallyDerivedProductPropertyType = create_fhir_type(
    "BiologicallyDerivedProductPropertyType",
    "tests.fixtures.resources.biologicallyderivedproduct.BiologicallyDerivedProductProperty",
)

BodyStructureType = create_fhir_type(
    "BodyStructureType", "tests.fixtures.resources.bodystructure.BodyStructure"
)

BodyStructureIncludedStructureType = create_fhir_type(
    "BodyStructureIncludedStructureType",
    "tests.fixtures.resources.bodystructure.BodyStructureIncludedStructure",
)

BodyStructureIncludedStructureBodyLandmarkOrientationType = create_fhir_type(
    "BodyStructureIncludedStructureBodyLandmarkOrientationType",
    "tests.fixtures.resources.bodystructure.BodyStructureIncludedStructureBodyLandmarkOrientation",
)

BodyStructureIncludedStructureBodyLandmarkOrientationDistanceFromLandmarkType = create_fhir_type(
    "BodyStructureIncludedStructureBodyLandmarkOrientationDistanceFromLandmarkType",
    "tests.fixtures.resources.bodystructure.BodyStructureIncludedStructureBodyLandmarkOrientationDistanceFromLandmark",
)

BundleType = create_fhir_type("BundleType", "tests.fixtures.resources.bundle.Bundle")

BundleEntryType = create_fhir_type(
    "BundleEntryType", "tests.fixtures.resources.bundle.BundleEntry"
)

BundleEntryRequestType = create_fhir_type(
    "BundleEntryRequestType", "tests.fixtures.resources.bundle.BundleEntryRequest"
)

BundleEntryResponseType = create_fhir_type(
    "BundleEntryResponseType", "tests.fixtures.resources.bundle.BundleEntryResponse"
)

BundleEntrySearchType = create_fhir_type(
    "BundleEntrySearchType", "tests.fixtures.resources.bundle.BundleEntrySearch"
)

BundleLinkType = create_fhir_type(
    "BundleLinkType", "tests.fixtures.resources.bundle.BundleLink"
)

CanonicalResourceType = create_fhir_type(
    "CanonicalResourceType",
    "tests.fixtures.resources.canonicalresource.CanonicalResource",
)

CapabilityStatementType = create_fhir_type(
    "CapabilityStatementType",
    "tests.fixtures.resources.capabilitystatement.CapabilityStatement",
)

CapabilityStatementDocumentType = create_fhir_type(
    "CapabilityStatementDocumentType",
    "tests.fixtures.resources.capabilitystatement.CapabilityStatementDocument",
)

CapabilityStatementImplementationType = create_fhir_type(
    "CapabilityStatementImplementationType",
    "tests.fixtures.resources.capabilitystatement.CapabilityStatementImplementation",
)

CapabilityStatementMessagingType = create_fhir_type(
    "CapabilityStatementMessagingType",
    "tests.fixtures.resources.capabilitystatement.CapabilityStatementMessaging",
)

CapabilityStatementMessagingEndpointType = create_fhir_type(
    "CapabilityStatementMessagingEndpointType",
    "tests.fixtures.resources.capabilitystatement.CapabilityStatementMessagingEndpoint",
)

CapabilityStatementMessagingSupportedMessageType = create_fhir_type(
    "CapabilityStatementMessagingSupportedMessageType",
    "tests.fixtures.resources.capabilitystatement.CapabilityStatementMessagingSupportedMessage",
)

CapabilityStatementRestType = create_fhir_type(
    "CapabilityStatementRestType",
    "tests.fixtures.resources.capabilitystatement.CapabilityStatementRest",
)

CapabilityStatementRestInteractionType = create_fhir_type(
    "CapabilityStatementRestInteractionType",
    "tests.fixtures.resources.capabilitystatement.CapabilityStatementRestInteraction",
)

CapabilityStatementRestResourceType = create_fhir_type(
    "CapabilityStatementRestResourceType",
    "tests.fixtures.resources.capabilitystatement.CapabilityStatementRestResource",
)

CapabilityStatementRestResourceInteractionType = create_fhir_type(
    "CapabilityStatementRestResourceInteractionType",
    "tests.fixtures.resources.capabilitystatement.CapabilityStatementRestResourceInteraction",
)

CapabilityStatementRestResourceOperationType = create_fhir_type(
    "CapabilityStatementRestResourceOperationType",
    "tests.fixtures.resources.capabilitystatement.CapabilityStatementRestResourceOperation",
)

CapabilityStatementRestResourceSearchParamType = create_fhir_type(
    "CapabilityStatementRestResourceSearchParamType",
    "tests.fixtures.resources.capabilitystatement.CapabilityStatementRestResourceSearchParam",
)

CapabilityStatementRestSecurityType = create_fhir_type(
    "CapabilityStatementRestSecurityType",
    "tests.fixtures.resources.capabilitystatement.CapabilityStatementRestSecurity",
)

CapabilityStatementSoftwareType = create_fhir_type(
    "CapabilityStatementSoftwareType",
    "tests.fixtures.resources.capabilitystatement.CapabilityStatementSoftware",
)

CarePlanType = create_fhir_type(
    "CarePlanType", "tests.fixtures.resources.careplan.CarePlan"
)

CarePlanActivityType = create_fhir_type(
    "CarePlanActivityType", "tests.fixtures.resources.careplan.CarePlanActivity"
)

CareTeamType = create_fhir_type(
    "CareTeamType", "tests.fixtures.resources.careteam.CareTeam"
)

CareTeamParticipantType = create_fhir_type(
    "CareTeamParticipantType", "tests.fixtures.resources.careteam.CareTeamParticipant"
)

ChargeItemType = create_fhir_type(
    "ChargeItemType", "tests.fixtures.resources.chargeitem.ChargeItem"
)

ChargeItemDefinitionType = create_fhir_type(
    "ChargeItemDefinitionType",
    "tests.fixtures.resources.chargeitemdefinition.ChargeItemDefinition",
)

ChargeItemDefinitionApplicabilityType = create_fhir_type(
    "ChargeItemDefinitionApplicabilityType",
    "tests.fixtures.resources.chargeitemdefinition.ChargeItemDefinitionApplicability",
)

ChargeItemDefinitionPropertyGroupType = create_fhir_type(
    "ChargeItemDefinitionPropertyGroupType",
    "tests.fixtures.resources.chargeitemdefinition.ChargeItemDefinitionPropertyGroup",
)

ChargeItemPerformerType = create_fhir_type(
    "ChargeItemPerformerType", "tests.fixtures.resources.chargeitem.ChargeItemPerformer"
)

CitationType = create_fhir_type(
    "CitationType", "tests.fixtures.resources.citation.Citation"
)

CitationCitedArtifactType = create_fhir_type(
    "CitationCitedArtifactType",
    "tests.fixtures.resources.citation.CitationCitedArtifact",
)

CitationCitedArtifactAbstractType = create_fhir_type(
    "CitationCitedArtifactAbstractType",
    "tests.fixtures.resources.citation.CitationCitedArtifactAbstract",
)

CitationCitedArtifactClassificationType = create_fhir_type(
    "CitationCitedArtifactClassificationType",
    "tests.fixtures.resources.citation.CitationCitedArtifactClassification",
)

CitationCitedArtifactContributorshipType = create_fhir_type(
    "CitationCitedArtifactContributorshipType",
    "tests.fixtures.resources.citation.CitationCitedArtifactContributorship",
)

CitationCitedArtifactContributorshipEntryType = create_fhir_type(
    "CitationCitedArtifactContributorshipEntryType",
    "tests.fixtures.resources.citation.CitationCitedArtifactContributorshipEntry",
)

CitationCitedArtifactContributorshipEntryContributionInstanceType = create_fhir_type(
    "CitationCitedArtifactContributorshipEntryContributionInstanceType",
    "tests.fixtures.resources.citation.CitationCitedArtifactContributorshipEntryContributionInstance",
)

CitationCitedArtifactContributorshipSummaryType = create_fhir_type(
    "CitationCitedArtifactContributorshipSummaryType",
    "tests.fixtures.resources.citation.CitationCitedArtifactContributorshipSummary",
)

CitationCitedArtifactPartType = create_fhir_type(
    "CitationCitedArtifactPartType",
    "tests.fixtures.resources.citation.CitationCitedArtifactPart",
)

CitationCitedArtifactPublicationFormType = create_fhir_type(
    "CitationCitedArtifactPublicationFormType",
    "tests.fixtures.resources.citation.CitationCitedArtifactPublicationForm",
)

CitationCitedArtifactPublicationFormPublishedInType = create_fhir_type(
    "CitationCitedArtifactPublicationFormPublishedInType",
    "tests.fixtures.resources.citation.CitationCitedArtifactPublicationFormPublishedIn",
)

CitationCitedArtifactRelatesToType = create_fhir_type(
    "CitationCitedArtifactRelatesToType",
    "tests.fixtures.resources.citation.CitationCitedArtifactRelatesTo",
)

CitationCitedArtifactStatusDateType = create_fhir_type(
    "CitationCitedArtifactStatusDateType",
    "tests.fixtures.resources.citation.CitationCitedArtifactStatusDate",
)

CitationCitedArtifactTitleType = create_fhir_type(
    "CitationCitedArtifactTitleType",
    "tests.fixtures.resources.citation.CitationCitedArtifactTitle",
)

CitationCitedArtifactVersionType = create_fhir_type(
    "CitationCitedArtifactVersionType",
    "tests.fixtures.resources.citation.CitationCitedArtifactVersion",
)

CitationCitedArtifactWebLocationType = create_fhir_type(
    "CitationCitedArtifactWebLocationType",
    "tests.fixtures.resources.citation.CitationCitedArtifactWebLocation",
)

CitationClassificationType = create_fhir_type(
    "CitationClassificationType",
    "tests.fixtures.resources.citation.CitationClassification",
)

CitationStatusDateType = create_fhir_type(
    "CitationStatusDateType", "tests.fixtures.resources.citation.CitationStatusDate"
)

CitationSummaryType = create_fhir_type(
    "CitationSummaryType", "tests.fixtures.resources.citation.CitationSummary"
)

ClaimType = create_fhir_type("ClaimType", "tests.fixtures.resources.claim.Claim")

ClaimAccidentType = create_fhir_type(
    "ClaimAccidentType", "tests.fixtures.resources.claim.ClaimAccident"
)

ClaimCareTeamType = create_fhir_type(
    "ClaimCareTeamType", "tests.fixtures.resources.claim.ClaimCareTeam"
)

ClaimDiagnosisType = create_fhir_type(
    "ClaimDiagnosisType", "tests.fixtures.resources.claim.ClaimDiagnosis"
)

ClaimEventType = create_fhir_type(
    "ClaimEventType", "tests.fixtures.resources.claim.ClaimEvent"
)

ClaimInsuranceType = create_fhir_type(
    "ClaimInsuranceType", "tests.fixtures.resources.claim.ClaimInsurance"
)

ClaimItemType = create_fhir_type(
    "ClaimItemType", "tests.fixtures.resources.claim.ClaimItem"
)

ClaimItemBodySiteType = create_fhir_type(
    "ClaimItemBodySiteType", "tests.fixtures.resources.claim.ClaimItemBodySite"
)

ClaimItemDetailType = create_fhir_type(
    "ClaimItemDetailType", "tests.fixtures.resources.claim.ClaimItemDetail"
)

ClaimItemDetailSubDetailType = create_fhir_type(
    "ClaimItemDetailSubDetailType",
    "tests.fixtures.resources.claim.ClaimItemDetailSubDetail",
)

ClaimPayeeType = create_fhir_type(
    "ClaimPayeeType", "tests.fixtures.resources.claim.ClaimPayee"
)

ClaimProcedureType = create_fhir_type(
    "ClaimProcedureType", "tests.fixtures.resources.claim.ClaimProcedure"
)

ClaimRelatedType = create_fhir_type(
    "ClaimRelatedType", "tests.fixtures.resources.claim.ClaimRelated"
)

ClaimResponseType = create_fhir_type(
    "ClaimResponseType", "tests.fixtures.resources.claimresponse.ClaimResponse"
)

ClaimResponseAddItemType = create_fhir_type(
    "ClaimResponseAddItemType",
    "tests.fixtures.resources.claimresponse.ClaimResponseAddItem",
)

ClaimResponseAddItemBodySiteType = create_fhir_type(
    "ClaimResponseAddItemBodySiteType",
    "tests.fixtures.resources.claimresponse.ClaimResponseAddItemBodySite",
)

ClaimResponseAddItemDetailType = create_fhir_type(
    "ClaimResponseAddItemDetailType",
    "tests.fixtures.resources.claimresponse.ClaimResponseAddItemDetail",
)

ClaimResponseAddItemDetailSubDetailType = create_fhir_type(
    "ClaimResponseAddItemDetailSubDetailType",
    "tests.fixtures.resources.claimresponse.ClaimResponseAddItemDetailSubDetail",
)

ClaimResponseErrorType = create_fhir_type(
    "ClaimResponseErrorType",
    "tests.fixtures.resources.claimresponse.ClaimResponseError",
)

ClaimResponseEventType = create_fhir_type(
    "ClaimResponseEventType",
    "tests.fixtures.resources.claimresponse.ClaimResponseEvent",
)

ClaimResponseInsuranceType = create_fhir_type(
    "ClaimResponseInsuranceType",
    "tests.fixtures.resources.claimresponse.ClaimResponseInsurance",
)

ClaimResponseItemType = create_fhir_type(
    "ClaimResponseItemType", "tests.fixtures.resources.claimresponse.ClaimResponseItem"
)

ClaimResponseItemAdjudicationType = create_fhir_type(
    "ClaimResponseItemAdjudicationType",
    "tests.fixtures.resources.claimresponse.ClaimResponseItemAdjudication",
)

ClaimResponseItemDetailType = create_fhir_type(
    "ClaimResponseItemDetailType",
    "tests.fixtures.resources.claimresponse.ClaimResponseItemDetail",
)

ClaimResponseItemDetailSubDetailType = create_fhir_type(
    "ClaimResponseItemDetailSubDetailType",
    "tests.fixtures.resources.claimresponse.ClaimResponseItemDetailSubDetail",
)

ClaimResponseItemReviewOutcomeType = create_fhir_type(
    "ClaimResponseItemReviewOutcomeType",
    "tests.fixtures.resources.claimresponse.ClaimResponseItemReviewOutcome",
)

ClaimResponsePaymentType = create_fhir_type(
    "ClaimResponsePaymentType",
    "tests.fixtures.resources.claimresponse.ClaimResponsePayment",
)

ClaimResponseProcessNoteType = create_fhir_type(
    "ClaimResponseProcessNoteType",
    "tests.fixtures.resources.claimresponse.ClaimResponseProcessNote",
)

ClaimResponseTotalType = create_fhir_type(
    "ClaimResponseTotalType",
    "tests.fixtures.resources.claimresponse.ClaimResponseTotal",
)

ClaimSupportingInfoType = create_fhir_type(
    "ClaimSupportingInfoType", "tests.fixtures.resources.claim.ClaimSupportingInfo"
)

ClinicalImpressionType = create_fhir_type(
    "ClinicalImpressionType",
    "tests.fixtures.resources.clinicalimpression.ClinicalImpression",
)

ClinicalImpressionFindingType = create_fhir_type(
    "ClinicalImpressionFindingType",
    "tests.fixtures.resources.clinicalimpression.ClinicalImpressionFinding",
)

ClinicalUseDefinitionType = create_fhir_type(
    "ClinicalUseDefinitionType",
    "tests.fixtures.resources.clinicalusedefinition.ClinicalUseDefinition",
)

ClinicalUseDefinitionContraindicationType = create_fhir_type(
    "ClinicalUseDefinitionContraindicationType",
    "tests.fixtures.resources.clinicalusedefinition.ClinicalUseDefinitionContraindication",
)

ClinicalUseDefinitionContraindicationOtherTherapyType = create_fhir_type(
    "ClinicalUseDefinitionContraindicationOtherTherapyType",
    "tests.fixtures.resources.clinicalusedefinition.ClinicalUseDefinitionContraindicationOtherTherapy",
)

ClinicalUseDefinitionIndicationType = create_fhir_type(
    "ClinicalUseDefinitionIndicationType",
    "tests.fixtures.resources.clinicalusedefinition.ClinicalUseDefinitionIndication",
)

ClinicalUseDefinitionInteractionType = create_fhir_type(
    "ClinicalUseDefinitionInteractionType",
    "tests.fixtures.resources.clinicalusedefinition.ClinicalUseDefinitionInteraction",
)

ClinicalUseDefinitionInteractionInteractantType = create_fhir_type(
    "ClinicalUseDefinitionInteractionInteractantType",
    "tests.fixtures.resources.clinicalusedefinition.ClinicalUseDefinitionInteractionInteractant",
)

ClinicalUseDefinitionUndesirableEffectType = create_fhir_type(
    "ClinicalUseDefinitionUndesirableEffectType",
    "tests.fixtures.resources.clinicalusedefinition.ClinicalUseDefinitionUndesirableEffect",
)

ClinicalUseDefinitionWarningType = create_fhir_type(
    "ClinicalUseDefinitionWarningType",
    "tests.fixtures.resources.clinicalusedefinition.ClinicalUseDefinitionWarning",
)

CodeSystemType = create_fhir_type(
    "CodeSystemType", "tests.fixtures.resources.codesystem.CodeSystem"
)

CodeSystemConceptType = create_fhir_type(
    "CodeSystemConceptType", "tests.fixtures.resources.codesystem.CodeSystemConcept"
)

CodeSystemConceptDesignationType = create_fhir_type(
    "CodeSystemConceptDesignationType",
    "tests.fixtures.resources.codesystem.CodeSystemConceptDesignation",
)

CodeSystemConceptPropertyType = create_fhir_type(
    "CodeSystemConceptPropertyType",
    "tests.fixtures.resources.codesystem.CodeSystemConceptProperty",
)

CodeSystemFilterType = create_fhir_type(
    "CodeSystemFilterType", "tests.fixtures.resources.codesystem.CodeSystemFilter"
)

CodeSystemPropertyType = create_fhir_type(
    "CodeSystemPropertyType", "tests.fixtures.resources.codesystem.CodeSystemProperty"
)

CodeableConceptType = create_fhir_type(
    "CodeableConceptType", "tests.fixtures.resources.codeableconcept.CodeableConcept"
)

CodeableReferenceType = create_fhir_type(
    "CodeableReferenceType",
    "tests.fixtures.resources.codeablereference.CodeableReference",
)

CodingType = create_fhir_type("CodingType", "tests.fixtures.resources.coding.Coding")

CommunicationType = create_fhir_type(
    "CommunicationType", "tests.fixtures.resources.communication.Communication"
)

CommunicationPayloadType = create_fhir_type(
    "CommunicationPayloadType",
    "tests.fixtures.resources.communication.CommunicationPayload",
)

CommunicationRequestType = create_fhir_type(
    "CommunicationRequestType",
    "tests.fixtures.resources.communicationrequest.CommunicationRequest",
)

CommunicationRequestPayloadType = create_fhir_type(
    "CommunicationRequestPayloadType",
    "tests.fixtures.resources.communicationrequest.CommunicationRequestPayload",
)

CompartmentDefinitionType = create_fhir_type(
    "CompartmentDefinitionType",
    "tests.fixtures.resources.compartmentdefinition.CompartmentDefinition",
)

CompartmentDefinitionResourceType = create_fhir_type(
    "CompartmentDefinitionResourceType",
    "tests.fixtures.resources.compartmentdefinition.CompartmentDefinitionResource",
)

CompositionType = create_fhir_type(
    "CompositionType", "tests.fixtures.resources.composition.Composition"
)

CompositionAttesterType = create_fhir_type(
    "CompositionAttesterType",
    "tests.fixtures.resources.composition.CompositionAttester",
)

CompositionEventType = create_fhir_type(
    "CompositionEventType", "tests.fixtures.resources.composition.CompositionEvent"
)

CompositionSectionType = create_fhir_type(
    "CompositionSectionType", "tests.fixtures.resources.composition.CompositionSection"
)

ConceptMapType = create_fhir_type(
    "ConceptMapType", "tests.fixtures.resources.conceptmap.ConceptMap"
)

ConceptMapAdditionalAttributeType = create_fhir_type(
    "ConceptMapAdditionalAttributeType",
    "tests.fixtures.resources.conceptmap.ConceptMapAdditionalAttribute",
)

ConceptMapGroupType = create_fhir_type(
    "ConceptMapGroupType", "tests.fixtures.resources.conceptmap.ConceptMapGroup"
)

ConceptMapGroupElementType = create_fhir_type(
    "ConceptMapGroupElementType",
    "tests.fixtures.resources.conceptmap.ConceptMapGroupElement",
)

ConceptMapGroupElementTargetType = create_fhir_type(
    "ConceptMapGroupElementTargetType",
    "tests.fixtures.resources.conceptmap.ConceptMapGroupElementTarget",
)

ConceptMapGroupElementTargetDependsOnType = create_fhir_type(
    "ConceptMapGroupElementTargetDependsOnType",
    "tests.fixtures.resources.conceptmap.ConceptMapGroupElementTargetDependsOn",
)

ConceptMapGroupElementTargetPropertyType = create_fhir_type(
    "ConceptMapGroupElementTargetPropertyType",
    "tests.fixtures.resources.conceptmap.ConceptMapGroupElementTargetProperty",
)

ConceptMapGroupUnmappedType = create_fhir_type(
    "ConceptMapGroupUnmappedType",
    "tests.fixtures.resources.conceptmap.ConceptMapGroupUnmapped",
)

ConceptMapPropertyType = create_fhir_type(
    "ConceptMapPropertyType", "tests.fixtures.resources.conceptmap.ConceptMapProperty"
)

ConditionType = create_fhir_type(
    "ConditionType", "tests.fixtures.resources.condition.Condition"
)

ConditionDefinitionType = create_fhir_type(
    "ConditionDefinitionType",
    "tests.fixtures.resources.conditiondefinition.ConditionDefinition",
)

ConditionDefinitionMedicationType = create_fhir_type(
    "ConditionDefinitionMedicationType",
    "tests.fixtures.resources.conditiondefinition.ConditionDefinitionMedication",
)

ConditionDefinitionObservationType = create_fhir_type(
    "ConditionDefinitionObservationType",
    "tests.fixtures.resources.conditiondefinition.ConditionDefinitionObservation",
)

ConditionDefinitionPlanType = create_fhir_type(
    "ConditionDefinitionPlanType",
    "tests.fixtures.resources.conditiondefinition.ConditionDefinitionPlan",
)

ConditionDefinitionPreconditionType = create_fhir_type(
    "ConditionDefinitionPreconditionType",
    "tests.fixtures.resources.conditiondefinition.ConditionDefinitionPrecondition",
)

ConditionDefinitionQuestionnaireType = create_fhir_type(
    "ConditionDefinitionQuestionnaireType",
    "tests.fixtures.resources.conditiondefinition.ConditionDefinitionQuestionnaire",
)

ConditionParticipantType = create_fhir_type(
    "ConditionParticipantType",
    "tests.fixtures.resources.condition.ConditionParticipant",
)

ConditionStageType = create_fhir_type(
    "ConditionStageType", "tests.fixtures.resources.condition.ConditionStage"
)

ConsentType = create_fhir_type(
    "ConsentType", "tests.fixtures.resources.consent.Consent"
)

ConsentPolicyBasisType = create_fhir_type(
    "ConsentPolicyBasisType", "tests.fixtures.resources.consent.ConsentPolicyBasis"
)

ConsentProvisionType = create_fhir_type(
    "ConsentProvisionType", "tests.fixtures.resources.consent.ConsentProvision"
)

ConsentProvisionActorType = create_fhir_type(
    "ConsentProvisionActorType",
    "tests.fixtures.resources.consent.ConsentProvisionActor",
)

ConsentProvisionDataType = create_fhir_type(
    "ConsentProvisionDataType", "tests.fixtures.resources.consent.ConsentProvisionData"
)

ConsentVerificationType = create_fhir_type(
    "ConsentVerificationType", "tests.fixtures.resources.consent.ConsentVerification"
)

ContactDetailType = create_fhir_type(
    "ContactDetailType", "tests.fixtures.resources.contactdetail.ContactDetail"
)

ContactPointType = create_fhir_type(
    "ContactPointType", "tests.fixtures.resources.contactpoint.ContactPoint"
)

ContractType = create_fhir_type(
    "ContractType", "tests.fixtures.resources.contract.Contract"
)

ContractContentDefinitionType = create_fhir_type(
    "ContractContentDefinitionType",
    "tests.fixtures.resources.contract.ContractContentDefinition",
)

ContractFriendlyType = create_fhir_type(
    "ContractFriendlyType", "tests.fixtures.resources.contract.ContractFriendly"
)

ContractLegalType = create_fhir_type(
    "ContractLegalType", "tests.fixtures.resources.contract.ContractLegal"
)

ContractRuleType = create_fhir_type(
    "ContractRuleType", "tests.fixtures.resources.contract.ContractRule"
)

ContractSignerType = create_fhir_type(
    "ContractSignerType", "tests.fixtures.resources.contract.ContractSigner"
)

ContractTermType = create_fhir_type(
    "ContractTermType", "tests.fixtures.resources.contract.ContractTerm"
)

ContractTermActionType = create_fhir_type(
    "ContractTermActionType", "tests.fixtures.resources.contract.ContractTermAction"
)

ContractTermActionSubjectType = create_fhir_type(
    "ContractTermActionSubjectType",
    "tests.fixtures.resources.contract.ContractTermActionSubject",
)

ContractTermAssetType = create_fhir_type(
    "ContractTermAssetType", "tests.fixtures.resources.contract.ContractTermAsset"
)

ContractTermAssetContextType = create_fhir_type(
    "ContractTermAssetContextType",
    "tests.fixtures.resources.contract.ContractTermAssetContext",
)

ContractTermAssetValuedItemType = create_fhir_type(
    "ContractTermAssetValuedItemType",
    "tests.fixtures.resources.contract.ContractTermAssetValuedItem",
)

ContractTermOfferType = create_fhir_type(
    "ContractTermOfferType", "tests.fixtures.resources.contract.ContractTermOffer"
)

ContractTermOfferAnswerType = create_fhir_type(
    "ContractTermOfferAnswerType",
    "tests.fixtures.resources.contract.ContractTermOfferAnswer",
)

ContractTermOfferPartyType = create_fhir_type(
    "ContractTermOfferPartyType",
    "tests.fixtures.resources.contract.ContractTermOfferParty",
)

ContractTermSecurityLabelType = create_fhir_type(
    "ContractTermSecurityLabelType",
    "tests.fixtures.resources.contract.ContractTermSecurityLabel",
)

ContributorType = create_fhir_type(
    "ContributorType", "tests.fixtures.resources.contributor.Contributor"
)

CountType = create_fhir_type("CountType", "tests.fixtures.resources.count.Count")

CoverageType = create_fhir_type(
    "CoverageType", "tests.fixtures.resources.coverage.Coverage"
)

CoverageClassType = create_fhir_type(
    "CoverageClassType", "tests.fixtures.resources.coverage.CoverageClass"
)

CoverageCostToBeneficiaryType = create_fhir_type(
    "CoverageCostToBeneficiaryType",
    "tests.fixtures.resources.coverage.CoverageCostToBeneficiary",
)

CoverageCostToBeneficiaryExceptionType = create_fhir_type(
    "CoverageCostToBeneficiaryExceptionType",
    "tests.fixtures.resources.coverage.CoverageCostToBeneficiaryException",
)

CoverageEligibilityRequestType = create_fhir_type(
    "CoverageEligibilityRequestType",
    "tests.fixtures.resources.coverageeligibilityrequest.CoverageEligibilityRequest",
)

CoverageEligibilityRequestEventType = create_fhir_type(
    "CoverageEligibilityRequestEventType",
    "tests.fixtures.resources.coverageeligibilityrequest.CoverageEligibilityRequestEvent",
)

CoverageEligibilityRequestInsuranceType = create_fhir_type(
    "CoverageEligibilityRequestInsuranceType",
    "tests.fixtures.resources.coverageeligibilityrequest.CoverageEligibilityRequestInsurance",
)

CoverageEligibilityRequestItemType = create_fhir_type(
    "CoverageEligibilityRequestItemType",
    "tests.fixtures.resources.coverageeligibilityrequest.CoverageEligibilityRequestItem",
)

CoverageEligibilityRequestItemDiagnosisType = create_fhir_type(
    "CoverageEligibilityRequestItemDiagnosisType",
    "tests.fixtures.resources.coverageeligibilityrequest.CoverageEligibilityRequestItemDiagnosis",
)

CoverageEligibilityRequestSupportingInfoType = create_fhir_type(
    "CoverageEligibilityRequestSupportingInfoType",
    "tests.fixtures.resources.coverageeligibilityrequest.CoverageEligibilityRequestSupportingInfo",
)

CoverageEligibilityResponseType = create_fhir_type(
    "CoverageEligibilityResponseType",
    "tests.fixtures.resources.coverageeligibilityresponse.CoverageEligibilityResponse",
)

CoverageEligibilityResponseErrorType = create_fhir_type(
    "CoverageEligibilityResponseErrorType",
    "tests.fixtures.resources.coverageeligibilityresponse.CoverageEligibilityResponseError",
)

CoverageEligibilityResponseEventType = create_fhir_type(
    "CoverageEligibilityResponseEventType",
    "tests.fixtures.resources.coverageeligibilityresponse.CoverageEligibilityResponseEvent",
)

CoverageEligibilityResponseInsuranceType = create_fhir_type(
    "CoverageEligibilityResponseInsuranceType",
    "tests.fixtures.resources.coverageeligibilityresponse.CoverageEligibilityResponseInsurance",
)

CoverageEligibilityResponseInsuranceItemType = create_fhir_type(
    "CoverageEligibilityResponseInsuranceItemType",
    "tests.fixtures.resources.coverageeligibilityresponse.CoverageEligibilityResponseInsuranceItem",
)

CoverageEligibilityResponseInsuranceItemBenefitType = create_fhir_type(
    "CoverageEligibilityResponseInsuranceItemBenefitType",
    "tests.fixtures.resources.coverageeligibilityresponse.CoverageEligibilityResponseInsuranceItemBenefit",
)

CoveragePaymentByType = create_fhir_type(
    "CoveragePaymentByType", "tests.fixtures.resources.coverage.CoveragePaymentBy"
)

DataRequirementType = create_fhir_type(
    "DataRequirementType", "tests.fixtures.resources.datarequirement.DataRequirement"
)

DataRequirementCodeFilterType = create_fhir_type(
    "DataRequirementCodeFilterType",
    "tests.fixtures.resources.datarequirement.DataRequirementCodeFilter",
)

DataRequirementDateFilterType = create_fhir_type(
    "DataRequirementDateFilterType",
    "tests.fixtures.resources.datarequirement.DataRequirementDateFilter",
)

DataRequirementSortType = create_fhir_type(
    "DataRequirementSortType",
    "tests.fixtures.resources.datarequirement.DataRequirementSort",
)

DataRequirementValueFilterType = create_fhir_type(
    "DataRequirementValueFilterType",
    "tests.fixtures.resources.datarequirement.DataRequirementValueFilter",
)

DataTypeType = create_fhir_type(
    "DataTypeType", "tests.fixtures.resources.datatype.DataType"
)

DetectedIssueType = create_fhir_type(
    "DetectedIssueType", "tests.fixtures.resources.detectedissue.DetectedIssue"
)

DetectedIssueEvidenceType = create_fhir_type(
    "DetectedIssueEvidenceType",
    "tests.fixtures.resources.detectedissue.DetectedIssueEvidence",
)

DetectedIssueMitigationType = create_fhir_type(
    "DetectedIssueMitigationType",
    "tests.fixtures.resources.detectedissue.DetectedIssueMitigation",
)

DeviceType = create_fhir_type("DeviceType", "tests.fixtures.resources.device.Device")

DeviceAssociationType = create_fhir_type(
    "DeviceAssociationType",
    "tests.fixtures.resources.deviceassociation.DeviceAssociation",
)

DeviceAssociationOperationType = create_fhir_type(
    "DeviceAssociationOperationType",
    "tests.fixtures.resources.deviceassociation.DeviceAssociationOperation",
)

DeviceConformsToType = create_fhir_type(
    "DeviceConformsToType", "tests.fixtures.resources.device.DeviceConformsTo"
)

DeviceDefinitionType = create_fhir_type(
    "DeviceDefinitionType", "tests.fixtures.resources.devicedefinition.DeviceDefinition"
)

DeviceDefinitionChargeItemType = create_fhir_type(
    "DeviceDefinitionChargeItemType",
    "tests.fixtures.resources.devicedefinition.DeviceDefinitionChargeItem",
)

DeviceDefinitionClassificationType = create_fhir_type(
    "DeviceDefinitionClassificationType",
    "tests.fixtures.resources.devicedefinition.DeviceDefinitionClassification",
)

DeviceDefinitionConformsToType = create_fhir_type(
    "DeviceDefinitionConformsToType",
    "tests.fixtures.resources.devicedefinition.DeviceDefinitionConformsTo",
)

DeviceDefinitionCorrectiveActionType = create_fhir_type(
    "DeviceDefinitionCorrectiveActionType",
    "tests.fixtures.resources.devicedefinition.DeviceDefinitionCorrectiveAction",
)

DeviceDefinitionDeviceNameType = create_fhir_type(
    "DeviceDefinitionDeviceNameType",
    "tests.fixtures.resources.devicedefinition.DeviceDefinitionDeviceName",
)

DeviceDefinitionGuidelineType = create_fhir_type(
    "DeviceDefinitionGuidelineType",
    "tests.fixtures.resources.devicedefinition.DeviceDefinitionGuideline",
)

DeviceDefinitionHasPartType = create_fhir_type(
    "DeviceDefinitionHasPartType",
    "tests.fixtures.resources.devicedefinition.DeviceDefinitionHasPart",
)

DeviceDefinitionLinkType = create_fhir_type(
    "DeviceDefinitionLinkType",
    "tests.fixtures.resources.devicedefinition.DeviceDefinitionLink",
)

DeviceDefinitionMaterialType = create_fhir_type(
    "DeviceDefinitionMaterialType",
    "tests.fixtures.resources.devicedefinition.DeviceDefinitionMaterial",
)

DeviceDefinitionPackagingType = create_fhir_type(
    "DeviceDefinitionPackagingType",
    "tests.fixtures.resources.devicedefinition.DeviceDefinitionPackaging",
)

DeviceDefinitionPackagingDistributorType = create_fhir_type(
    "DeviceDefinitionPackagingDistributorType",
    "tests.fixtures.resources.devicedefinition.DeviceDefinitionPackagingDistributor",
)

DeviceDefinitionPropertyType = create_fhir_type(
    "DeviceDefinitionPropertyType",
    "tests.fixtures.resources.devicedefinition.DeviceDefinitionProperty",
)

DeviceDefinitionRegulatoryIdentifierType = create_fhir_type(
    "DeviceDefinitionRegulatoryIdentifierType",
    "tests.fixtures.resources.devicedefinition.DeviceDefinitionRegulatoryIdentifier",
)

DeviceDefinitionUdiDeviceIdentifierType = create_fhir_type(
    "DeviceDefinitionUdiDeviceIdentifierType",
    "tests.fixtures.resources.devicedefinition.DeviceDefinitionUdiDeviceIdentifier",
)

DeviceDefinitionUdiDeviceIdentifierMarketDistributionType = create_fhir_type(
    "DeviceDefinitionUdiDeviceIdentifierMarketDistributionType",
    "tests.fixtures.resources.devicedefinition.DeviceDefinitionUdiDeviceIdentifierMarketDistribution",
)

DeviceDefinitionVersionType = create_fhir_type(
    "DeviceDefinitionVersionType",
    "tests.fixtures.resources.devicedefinition.DeviceDefinitionVersion",
)

DeviceDispenseType = create_fhir_type(
    "DeviceDispenseType", "tests.fixtures.resources.devicedispense.DeviceDispense"
)

DeviceDispensePerformerType = create_fhir_type(
    "DeviceDispensePerformerType",
    "tests.fixtures.resources.devicedispense.DeviceDispensePerformer",
)

DeviceMetricType = create_fhir_type(
    "DeviceMetricType", "tests.fixtures.resources.devicemetric.DeviceMetric"
)

DeviceMetricCalibrationType = create_fhir_type(
    "DeviceMetricCalibrationType",
    "tests.fixtures.resources.devicemetric.DeviceMetricCalibration",
)

DeviceNameType = create_fhir_type(
    "DeviceNameType", "tests.fixtures.resources.device.DeviceName"
)

DevicePropertyType = create_fhir_type(
    "DevicePropertyType", "tests.fixtures.resources.device.DeviceProperty"
)

DeviceRequestType = create_fhir_type(
    "DeviceRequestType", "tests.fixtures.resources.devicerequest.DeviceRequest"
)

DeviceRequestParameterType = create_fhir_type(
    "DeviceRequestParameterType",
    "tests.fixtures.resources.devicerequest.DeviceRequestParameter",
)

DeviceUdiCarrierType = create_fhir_type(
    "DeviceUdiCarrierType", "tests.fixtures.resources.device.DeviceUdiCarrier"
)

DeviceUsageType = create_fhir_type(
    "DeviceUsageType", "tests.fixtures.resources.deviceusage.DeviceUsage"
)

DeviceUsageAdherenceType = create_fhir_type(
    "DeviceUsageAdherenceType",
    "tests.fixtures.resources.deviceusage.DeviceUsageAdherence",
)

DeviceVersionType = create_fhir_type(
    "DeviceVersionType", "tests.fixtures.resources.device.DeviceVersion"
)

DiagnosticReportType = create_fhir_type(
    "DiagnosticReportType", "tests.fixtures.resources.diagnosticreport.DiagnosticReport"
)

DiagnosticReportMediaType = create_fhir_type(
    "DiagnosticReportMediaType",
    "tests.fixtures.resources.diagnosticreport.DiagnosticReportMedia",
)

DiagnosticReportSupportingInfoType = create_fhir_type(
    "DiagnosticReportSupportingInfoType",
    "tests.fixtures.resources.diagnosticreport.DiagnosticReportSupportingInfo",
)

DistanceType = create_fhir_type(
    "DistanceType", "tests.fixtures.resources.distance.Distance"
)

DocumentReferenceType = create_fhir_type(
    "DocumentReferenceType",
    "tests.fixtures.resources.documentreference.DocumentReference",
)

DocumentReferenceAttesterType = create_fhir_type(
    "DocumentReferenceAttesterType",
    "tests.fixtures.resources.documentreference.DocumentReferenceAttester",
)

DocumentReferenceContentType = create_fhir_type(
    "DocumentReferenceContentType",
    "tests.fixtures.resources.documentreference.DocumentReferenceContent",
)

DocumentReferenceContentProfileType = create_fhir_type(
    "DocumentReferenceContentProfileType",
    "tests.fixtures.resources.documentreference.DocumentReferenceContentProfile",
)

DocumentReferenceRelatesToType = create_fhir_type(
    "DocumentReferenceRelatesToType",
    "tests.fixtures.resources.documentreference.DocumentReferenceRelatesTo",
)

DomainResourceType = create_fhir_type(
    "DomainResourceType", "tests.fixtures.resources.domainresource.DomainResource"
)

DosageType = create_fhir_type("DosageType", "tests.fixtures.resources.dosage.Dosage")

DosageDoseAndRateType = create_fhir_type(
    "DosageDoseAndRateType", "tests.fixtures.resources.dosage.DosageDoseAndRate"
)

DurationType = create_fhir_type(
    "DurationType", "tests.fixtures.resources.duration.Duration"
)

ElementType = create_fhir_element_or_resource_type(
    "ElementType", "tests.fixtures.resources.element.Element"
)

ElementDefinitionType = create_fhir_type(
    "ElementDefinitionType",
    "tests.fixtures.resources.elementdefinition.ElementDefinition",
)

ElementDefinitionBaseType = create_fhir_type(
    "ElementDefinitionBaseType",
    "tests.fixtures.resources.elementdefinition.ElementDefinitionBase",
)

ElementDefinitionBindingType = create_fhir_type(
    "ElementDefinitionBindingType",
    "tests.fixtures.resources.elementdefinition.ElementDefinitionBinding",
)

ElementDefinitionBindingAdditionalType = create_fhir_type(
    "ElementDefinitionBindingAdditionalType",
    "tests.fixtures.resources.elementdefinition.ElementDefinitionBindingAdditional",
)

ElementDefinitionConstraintType = create_fhir_type(
    "ElementDefinitionConstraintType",
    "tests.fixtures.resources.elementdefinition.ElementDefinitionConstraint",
)

ElementDefinitionExampleType = create_fhir_type(
    "ElementDefinitionExampleType",
    "tests.fixtures.resources.elementdefinition.ElementDefinitionExample",
)

ElementDefinitionMappingType = create_fhir_type(
    "ElementDefinitionMappingType",
    "tests.fixtures.resources.elementdefinition.ElementDefinitionMapping",
)

ElementDefinitionSlicingType = create_fhir_type(
    "ElementDefinitionSlicingType",
    "tests.fixtures.resources.elementdefinition.ElementDefinitionSlicing",
)

ElementDefinitionSlicingDiscriminatorType = create_fhir_type(
    "ElementDefinitionSlicingDiscriminatorType",
    "tests.fixtures.resources.elementdefinition.ElementDefinitionSlicingDiscriminator",
)

ElementDefinitionTypeType = create_fhir_type(
    "ElementDefinitionTypeType",
    "tests.fixtures.resources.elementdefinition.ElementDefinitionType",
)

EncounterType = create_fhir_type(
    "EncounterType", "tests.fixtures.resources.encounter.Encounter"
)

EncounterAdmissionType = create_fhir_type(
    "EncounterAdmissionType", "tests.fixtures.resources.encounter.EncounterAdmission"
)

EncounterDiagnosisType = create_fhir_type(
    "EncounterDiagnosisType", "tests.fixtures.resources.encounter.EncounterDiagnosis"
)

EncounterHistoryType = create_fhir_type(
    "EncounterHistoryType", "tests.fixtures.resources.encounterhistory.EncounterHistory"
)

EncounterHistoryLocationType = create_fhir_type(
    "EncounterHistoryLocationType",
    "tests.fixtures.resources.encounterhistory.EncounterHistoryLocation",
)

EncounterLocationType = create_fhir_type(
    "EncounterLocationType", "tests.fixtures.resources.encounter.EncounterLocation"
)

EncounterParticipantType = create_fhir_type(
    "EncounterParticipantType",
    "tests.fixtures.resources.encounter.EncounterParticipant",
)

EncounterReasonType = create_fhir_type(
    "EncounterReasonType", "tests.fixtures.resources.encounter.EncounterReason"
)

EndpointType = create_fhir_type(
    "EndpointType", "tests.fixtures.resources.endpoint.Endpoint"
)

EndpointPayloadType = create_fhir_type(
    "EndpointPayloadType", "tests.fixtures.resources.endpoint.EndpointPayload"
)

EnrollmentRequestType = create_fhir_type(
    "EnrollmentRequestType",
    "tests.fixtures.resources.enrollmentrequest.EnrollmentRequest",
)

EnrollmentResponseType = create_fhir_type(
    "EnrollmentResponseType",
    "tests.fixtures.resources.enrollmentresponse.EnrollmentResponse",
)

EpisodeOfCareType = create_fhir_type(
    "EpisodeOfCareType", "tests.fixtures.resources.episodeofcare.EpisodeOfCare"
)

EpisodeOfCareDiagnosisType = create_fhir_type(
    "EpisodeOfCareDiagnosisType",
    "tests.fixtures.resources.episodeofcare.EpisodeOfCareDiagnosis",
)

EpisodeOfCareReasonType = create_fhir_type(
    "EpisodeOfCareReasonType",
    "tests.fixtures.resources.episodeofcare.EpisodeOfCareReason",
)

EpisodeOfCareStatusHistoryType = create_fhir_type(
    "EpisodeOfCareStatusHistoryType",
    "tests.fixtures.resources.episodeofcare.EpisodeOfCareStatusHistory",
)

EventDefinitionType = create_fhir_type(
    "EventDefinitionType", "tests.fixtures.resources.eventdefinition.EventDefinition"
)

EvidenceType = create_fhir_type(
    "EvidenceType", "tests.fixtures.resources.evidence.Evidence"
)

EvidenceCertaintyType = create_fhir_type(
    "EvidenceCertaintyType", "tests.fixtures.resources.evidence.EvidenceCertainty"
)

EvidenceReportType = create_fhir_type(
    "EvidenceReportType", "tests.fixtures.resources.evidencereport.EvidenceReport"
)

EvidenceReportRelatesToType = create_fhir_type(
    "EvidenceReportRelatesToType",
    "tests.fixtures.resources.evidencereport.EvidenceReportRelatesTo",
)

EvidenceReportRelatesToTargetType = create_fhir_type(
    "EvidenceReportRelatesToTargetType",
    "tests.fixtures.resources.evidencereport.EvidenceReportRelatesToTarget",
)

EvidenceReportSectionType = create_fhir_type(
    "EvidenceReportSectionType",
    "tests.fixtures.resources.evidencereport.EvidenceReportSection",
)

EvidenceReportSubjectType = create_fhir_type(
    "EvidenceReportSubjectType",
    "tests.fixtures.resources.evidencereport.EvidenceReportSubject",
)

EvidenceReportSubjectCharacteristicType = create_fhir_type(
    "EvidenceReportSubjectCharacteristicType",
    "tests.fixtures.resources.evidencereport.EvidenceReportSubjectCharacteristic",
)

EvidenceStatisticType = create_fhir_type(
    "EvidenceStatisticType", "tests.fixtures.resources.evidence.EvidenceStatistic"
)

EvidenceStatisticAttributeEstimateType = create_fhir_type(
    "EvidenceStatisticAttributeEstimateType",
    "tests.fixtures.resources.evidence.EvidenceStatisticAttributeEstimate",
)

EvidenceStatisticModelCharacteristicType = create_fhir_type(
    "EvidenceStatisticModelCharacteristicType",
    "tests.fixtures.resources.evidence.EvidenceStatisticModelCharacteristic",
)

EvidenceStatisticModelCharacteristicVariableType = create_fhir_type(
    "EvidenceStatisticModelCharacteristicVariableType",
    "tests.fixtures.resources.evidence.EvidenceStatisticModelCharacteristicVariable",
)

EvidenceStatisticSampleSizeType = create_fhir_type(
    "EvidenceStatisticSampleSizeType",
    "tests.fixtures.resources.evidence.EvidenceStatisticSampleSize",
)

EvidenceVariableType = create_fhir_type(
    "EvidenceVariableType", "tests.fixtures.resources.evidencevariable.EvidenceVariable"
)

EvidenceVariableCategoryType = create_fhir_type(
    "EvidenceVariableCategoryType",
    "tests.fixtures.resources.evidencevariable.EvidenceVariableCategory",
)

EvidenceVariableCharacteristicType = create_fhir_type(
    "EvidenceVariableCharacteristicType",
    "tests.fixtures.resources.evidencevariable.EvidenceVariableCharacteristic",
)

EvidenceVariableCharacteristicDefinitionByCombinationType = create_fhir_type(
    "EvidenceVariableCharacteristicDefinitionByCombinationType",
    "tests.fixtures.resources.evidencevariable.EvidenceVariableCharacteristicDefinitionByCombination",
)

EvidenceVariableCharacteristicDefinitionByTypeAndValueType = create_fhir_type(
    "EvidenceVariableCharacteristicDefinitionByTypeAndValueType",
    "tests.fixtures.resources.evidencevariable.EvidenceVariableCharacteristicDefinitionByTypeAndValue",
)

EvidenceVariableCharacteristicTimeFromEventType = create_fhir_type(
    "EvidenceVariableCharacteristicTimeFromEventType",
    "tests.fixtures.resources.evidencevariable.EvidenceVariableCharacteristicTimeFromEvent",
)

EvidenceVariableDefinitionType = create_fhir_type(
    "EvidenceVariableDefinitionType",
    "tests.fixtures.resources.evidence.EvidenceVariableDefinition",
)

ExampleScenarioType = create_fhir_type(
    "ExampleScenarioType", "tests.fixtures.resources.examplescenario.ExampleScenario"
)

ExampleScenarioActorType = create_fhir_type(
    "ExampleScenarioActorType",
    "tests.fixtures.resources.examplescenario.ExampleScenarioActor",
)

ExampleScenarioInstanceType = create_fhir_type(
    "ExampleScenarioInstanceType",
    "tests.fixtures.resources.examplescenario.ExampleScenarioInstance",
)

ExampleScenarioInstanceContainedInstanceType = create_fhir_type(
    "ExampleScenarioInstanceContainedInstanceType",
    "tests.fixtures.resources.examplescenario.ExampleScenarioInstanceContainedInstance",
)

ExampleScenarioInstanceVersionType = create_fhir_type(
    "ExampleScenarioInstanceVersionType",
    "tests.fixtures.resources.examplescenario.ExampleScenarioInstanceVersion",
)

ExampleScenarioProcessType = create_fhir_type(
    "ExampleScenarioProcessType",
    "tests.fixtures.resources.examplescenario.ExampleScenarioProcess",
)

ExampleScenarioProcessStepType = create_fhir_type(
    "ExampleScenarioProcessStepType",
    "tests.fixtures.resources.examplescenario.ExampleScenarioProcessStep",
)

ExampleScenarioProcessStepAlternativeType = create_fhir_type(
    "ExampleScenarioProcessStepAlternativeType",
    "tests.fixtures.resources.examplescenario.ExampleScenarioProcessStepAlternative",
)

ExampleScenarioProcessStepOperationType = create_fhir_type(
    "ExampleScenarioProcessStepOperationType",
    "tests.fixtures.resources.examplescenario.ExampleScenarioProcessStepOperation",
)

ExplanationOfBenefitType = create_fhir_type(
    "ExplanationOfBenefitType",
    "tests.fixtures.resources.explanationofbenefit.ExplanationOfBenefit",
)

ExplanationOfBenefitAccidentType = create_fhir_type(
    "ExplanationOfBenefitAccidentType",
    "tests.fixtures.resources.explanationofbenefit.ExplanationOfBenefitAccident",
)

ExplanationOfBenefitAddItemType = create_fhir_type(
    "ExplanationOfBenefitAddItemType",
    "tests.fixtures.resources.explanationofbenefit.ExplanationOfBenefitAddItem",
)

ExplanationOfBenefitAddItemBodySiteType = create_fhir_type(
    "ExplanationOfBenefitAddItemBodySiteType",
    "tests.fixtures.resources.explanationofbenefit.ExplanationOfBenefitAddItemBodySite",
)

ExplanationOfBenefitAddItemDetailType = create_fhir_type(
    "ExplanationOfBenefitAddItemDetailType",
    "tests.fixtures.resources.explanationofbenefit.ExplanationOfBenefitAddItemDetail",
)

ExplanationOfBenefitAddItemDetailSubDetailType = create_fhir_type(
    "ExplanationOfBenefitAddItemDetailSubDetailType",
    "tests.fixtures.resources.explanationofbenefit.ExplanationOfBenefitAddItemDetailSubDetail",
)

ExplanationOfBenefitBenefitBalanceType = create_fhir_type(
    "ExplanationOfBenefitBenefitBalanceType",
    "tests.fixtures.resources.explanationofbenefit.ExplanationOfBenefitBenefitBalance",
)

ExplanationOfBenefitBenefitBalanceFinancialType = create_fhir_type(
    "ExplanationOfBenefitBenefitBalanceFinancialType",
    "tests.fixtures.resources.explanationofbenefit.ExplanationOfBenefitBenefitBalanceFinancial",
)

ExplanationOfBenefitCareTeamType = create_fhir_type(
    "ExplanationOfBenefitCareTeamType",
    "tests.fixtures.resources.explanationofbenefit.ExplanationOfBenefitCareTeam",
)

ExplanationOfBenefitDiagnosisType = create_fhir_type(
    "ExplanationOfBenefitDiagnosisType",
    "tests.fixtures.resources.explanationofbenefit.ExplanationOfBenefitDiagnosis",
)

ExplanationOfBenefitEventType = create_fhir_type(
    "ExplanationOfBenefitEventType",
    "tests.fixtures.resources.explanationofbenefit.ExplanationOfBenefitEvent",
)

ExplanationOfBenefitInsuranceType = create_fhir_type(
    "ExplanationOfBenefitInsuranceType",
    "tests.fixtures.resources.explanationofbenefit.ExplanationOfBenefitInsurance",
)

ExplanationOfBenefitItemType = create_fhir_type(
    "ExplanationOfBenefitItemType",
    "tests.fixtures.resources.explanationofbenefit.ExplanationOfBenefitItem",
)

ExplanationOfBenefitItemAdjudicationType = create_fhir_type(
    "ExplanationOfBenefitItemAdjudicationType",
    "tests.fixtures.resources.explanationofbenefit.ExplanationOfBenefitItemAdjudication",
)

ExplanationOfBenefitItemBodySiteType = create_fhir_type(
    "ExplanationOfBenefitItemBodySiteType",
    "tests.fixtures.resources.explanationofbenefit.ExplanationOfBenefitItemBodySite",
)

ExplanationOfBenefitItemDetailType = create_fhir_type(
    "ExplanationOfBenefitItemDetailType",
    "tests.fixtures.resources.explanationofbenefit.ExplanationOfBenefitItemDetail",
)

ExplanationOfBenefitItemDetailSubDetailType = create_fhir_type(
    "ExplanationOfBenefitItemDetailSubDetailType",
    "tests.fixtures.resources.explanationofbenefit.ExplanationOfBenefitItemDetailSubDetail",
)

ExplanationOfBenefitItemReviewOutcomeType = create_fhir_type(
    "ExplanationOfBenefitItemReviewOutcomeType",
    "tests.fixtures.resources.explanationofbenefit.ExplanationOfBenefitItemReviewOutcome",
)

ExplanationOfBenefitPayeeType = create_fhir_type(
    "ExplanationOfBenefitPayeeType",
    "tests.fixtures.resources.explanationofbenefit.ExplanationOfBenefitPayee",
)

ExplanationOfBenefitPaymentType = create_fhir_type(
    "ExplanationOfBenefitPaymentType",
    "tests.fixtures.resources.explanationofbenefit.ExplanationOfBenefitPayment",
)

ExplanationOfBenefitProcedureType = create_fhir_type(
    "ExplanationOfBenefitProcedureType",
    "tests.fixtures.resources.explanationofbenefit.ExplanationOfBenefitProcedure",
)

ExplanationOfBenefitProcessNoteType = create_fhir_type(
    "ExplanationOfBenefitProcessNoteType",
    "tests.fixtures.resources.explanationofbenefit.ExplanationOfBenefitProcessNote",
)

ExplanationOfBenefitRelatedType = create_fhir_type(
    "ExplanationOfBenefitRelatedType",
    "tests.fixtures.resources.explanationofbenefit.ExplanationOfBenefitRelated",
)

ExplanationOfBenefitSupportingInfoType = create_fhir_type(
    "ExplanationOfBenefitSupportingInfoType",
    "tests.fixtures.resources.explanationofbenefit.ExplanationOfBenefitSupportingInfo",
)

ExplanationOfBenefitTotalType = create_fhir_type(
    "ExplanationOfBenefitTotalType",
    "tests.fixtures.resources.explanationofbenefit.ExplanationOfBenefitTotal",
)

ExpressionType = create_fhir_type(
    "ExpressionType", "tests.fixtures.resources.expression.Expression"
)

ExtendedContactDetailType = create_fhir_type(
    "ExtendedContactDetailType",
    "tests.fixtures.resources.extendedcontactdetail.ExtendedContactDetail",
)

ExtensionType = create_fhir_type(
    "ExtensionType", "tests.fixtures.resources.extension.Extension"
)

FamilyMemberHistoryType = create_fhir_type(
    "FamilyMemberHistoryType",
    "tests.fixtures.resources.familymemberhistory.FamilyMemberHistory",
)

FamilyMemberHistoryConditionType = create_fhir_type(
    "FamilyMemberHistoryConditionType",
    "tests.fixtures.resources.familymemberhistory.FamilyMemberHistoryCondition",
)

FamilyMemberHistoryParticipantType = create_fhir_type(
    "FamilyMemberHistoryParticipantType",
    "tests.fixtures.resources.familymemberhistory.FamilyMemberHistoryParticipant",
)

FamilyMemberHistoryProcedureType = create_fhir_type(
    "FamilyMemberHistoryProcedureType",
    "tests.fixtures.resources.familymemberhistory.FamilyMemberHistoryProcedure",
)

FlagType = create_fhir_type("FlagType", "tests.fixtures.resources.flag.Flag")

FormularyItemType = create_fhir_type(
    "FormularyItemType", "tests.fixtures.resources.formularyitem.FormularyItem"
)

GenomicStudyType = create_fhir_type(
    "GenomicStudyType", "tests.fixtures.resources.genomicstudy.GenomicStudy"
)

GenomicStudyAnalysisType = create_fhir_type(
    "GenomicStudyAnalysisType",
    "tests.fixtures.resources.genomicstudy.GenomicStudyAnalysis",
)

GenomicStudyAnalysisDeviceType = create_fhir_type(
    "GenomicStudyAnalysisDeviceType",
    "tests.fixtures.resources.genomicstudy.GenomicStudyAnalysisDevice",
)

GenomicStudyAnalysisInputType = create_fhir_type(
    "GenomicStudyAnalysisInputType",
    "tests.fixtures.resources.genomicstudy.GenomicStudyAnalysisInput",
)

GenomicStudyAnalysisOutputType = create_fhir_type(
    "GenomicStudyAnalysisOutputType",
    "tests.fixtures.resources.genomicstudy.GenomicStudyAnalysisOutput",
)

GenomicStudyAnalysisPerformerType = create_fhir_type(
    "GenomicStudyAnalysisPerformerType",
    "tests.fixtures.resources.genomicstudy.GenomicStudyAnalysisPerformer",
)

GoalType = create_fhir_type("GoalType", "tests.fixtures.resources.goal.Goal")

GoalTargetType = create_fhir_type(
    "GoalTargetType", "tests.fixtures.resources.goal.GoalTarget"
)

GraphDefinitionType = create_fhir_type(
    "GraphDefinitionType", "tests.fixtures.resources.graphdefinition.GraphDefinition"
)

GraphDefinitionLinkType = create_fhir_type(
    "GraphDefinitionLinkType",
    "tests.fixtures.resources.graphdefinition.GraphDefinitionLink",
)

GraphDefinitionLinkCompartmentType = create_fhir_type(
    "GraphDefinitionLinkCompartmentType",
    "tests.fixtures.resources.graphdefinition.GraphDefinitionLinkCompartment",
)

GraphDefinitionNodeType = create_fhir_type(
    "GraphDefinitionNodeType",
    "tests.fixtures.resources.graphdefinition.GraphDefinitionNode",
)

GroupType = create_fhir_type("GroupType", "tests.fixtures.resources.group.Group")

GroupCharacteristicType = create_fhir_type(
    "GroupCharacteristicType", "tests.fixtures.resources.group.GroupCharacteristic"
)

GroupMemberType = create_fhir_type(
    "GroupMemberType", "tests.fixtures.resources.group.GroupMember"
)

GuidanceResponseType = create_fhir_type(
    "GuidanceResponseType", "tests.fixtures.resources.guidanceresponse.GuidanceResponse"
)

HealthcareServiceType = create_fhir_type(
    "HealthcareServiceType",
    "tests.fixtures.resources.healthcareservice.HealthcareService",
)

HealthcareServiceEligibilityType = create_fhir_type(
    "HealthcareServiceEligibilityType",
    "tests.fixtures.resources.healthcareservice.HealthcareServiceEligibility",
)

HumanNameType = create_fhir_type(
    "HumanNameType", "tests.fixtures.resources.humanname.HumanName"
)

IdentifierType = create_fhir_type(
    "IdentifierType", "tests.fixtures.resources.identifier.Identifier"
)

ImagingSelectionType = create_fhir_type(
    "ImagingSelectionType", "tests.fixtures.resources.imagingselection.ImagingSelection"
)

ImagingSelectionInstanceType = create_fhir_type(
    "ImagingSelectionInstanceType",
    "tests.fixtures.resources.imagingselection.ImagingSelectionInstance",
)

ImagingSelectionInstanceImageRegion2DType = create_fhir_type(
    "ImagingSelectionInstanceImageRegion2DType",
    "tests.fixtures.resources.imagingselection.ImagingSelectionInstanceImageRegion2D",
)

ImagingSelectionInstanceImageRegion3DType = create_fhir_type(
    "ImagingSelectionInstanceImageRegion3DType",
    "tests.fixtures.resources.imagingselection.ImagingSelectionInstanceImageRegion3D",
)

ImagingSelectionPerformerType = create_fhir_type(
    "ImagingSelectionPerformerType",
    "tests.fixtures.resources.imagingselection.ImagingSelectionPerformer",
)

ImagingStudyType = create_fhir_type(
    "ImagingStudyType", "tests.fixtures.resources.imagingstudy.ImagingStudy"
)

ImagingStudySeriesType = create_fhir_type(
    "ImagingStudySeriesType", "tests.fixtures.resources.imagingstudy.ImagingStudySeries"
)

ImagingStudySeriesInstanceType = create_fhir_type(
    "ImagingStudySeriesInstanceType",
    "tests.fixtures.resources.imagingstudy.ImagingStudySeriesInstance",
)

ImagingStudySeriesPerformerType = create_fhir_type(
    "ImagingStudySeriesPerformerType",
    "tests.fixtures.resources.imagingstudy.ImagingStudySeriesPerformer",
)

ImmunizationType = create_fhir_type(
    "ImmunizationType", "tests.fixtures.resources.immunization.Immunization"
)

ImmunizationEvaluationType = create_fhir_type(
    "ImmunizationEvaluationType",
    "tests.fixtures.resources.immunizationevaluation.ImmunizationEvaluation",
)

ImmunizationPerformerType = create_fhir_type(
    "ImmunizationPerformerType",
    "tests.fixtures.resources.immunization.ImmunizationPerformer",
)

ImmunizationProgramEligibilityType = create_fhir_type(
    "ImmunizationProgramEligibilityType",
    "tests.fixtures.resources.immunization.ImmunizationProgramEligibility",
)

ImmunizationProtocolAppliedType = create_fhir_type(
    "ImmunizationProtocolAppliedType",
    "tests.fixtures.resources.immunization.ImmunizationProtocolApplied",
)

ImmunizationReactionType = create_fhir_type(
    "ImmunizationReactionType",
    "tests.fixtures.resources.immunization.ImmunizationReaction",
)

ImmunizationRecommendationType = create_fhir_type(
    "ImmunizationRecommendationType",
    "tests.fixtures.resources.immunizationrecommendation.ImmunizationRecommendation",
)

ImmunizationRecommendationRecommendationType = create_fhir_type(
    "ImmunizationRecommendationRecommendationType",
    "tests.fixtures.resources.immunizationrecommendation.ImmunizationRecommendationRecommendation",
)

ImmunizationRecommendationRecommendationDateCriterionType = create_fhir_type(
    "ImmunizationRecommendationRecommendationDateCriterionType",
    "tests.fixtures.resources.immunizationrecommendation.ImmunizationRecommendationRecommendationDateCriterion",
)

ImplementationGuideType = create_fhir_type(
    "ImplementationGuideType",
    "tests.fixtures.resources.implementationguide.ImplementationGuide",
)

ImplementationGuideDefinitionType = create_fhir_type(
    "ImplementationGuideDefinitionType",
    "tests.fixtures.resources.implementationguide.ImplementationGuideDefinition",
)

ImplementationGuideDefinitionGroupingType = create_fhir_type(
    "ImplementationGuideDefinitionGroupingType",
    "tests.fixtures.resources.implementationguide.ImplementationGuideDefinitionGrouping",
)

ImplementationGuideDefinitionPageType = create_fhir_type(
    "ImplementationGuideDefinitionPageType",
    "tests.fixtures.resources.implementationguide.ImplementationGuideDefinitionPage",
)

ImplementationGuideDefinitionParameterType = create_fhir_type(
    "ImplementationGuideDefinitionParameterType",
    "tests.fixtures.resources.implementationguide.ImplementationGuideDefinitionParameter",
)

ImplementationGuideDefinitionResourceType = create_fhir_type(
    "ImplementationGuideDefinitionResourceType",
    "tests.fixtures.resources.implementationguide.ImplementationGuideDefinitionResource",
)

ImplementationGuideDefinitionTemplateType = create_fhir_type(
    "ImplementationGuideDefinitionTemplateType",
    "tests.fixtures.resources.implementationguide.ImplementationGuideDefinitionTemplate",
)

ImplementationGuideDependsOnType = create_fhir_type(
    "ImplementationGuideDependsOnType",
    "tests.fixtures.resources.implementationguide.ImplementationGuideDependsOn",
)

ImplementationGuideGlobalType = create_fhir_type(
    "ImplementationGuideGlobalType",
    "tests.fixtures.resources.implementationguide.ImplementationGuideGlobal",
)

ImplementationGuideManifestType = create_fhir_type(
    "ImplementationGuideManifestType",
    "tests.fixtures.resources.implementationguide.ImplementationGuideManifest",
)

ImplementationGuideManifestPageType = create_fhir_type(
    "ImplementationGuideManifestPageType",
    "tests.fixtures.resources.implementationguide.ImplementationGuideManifestPage",
)

ImplementationGuideManifestResourceType = create_fhir_type(
    "ImplementationGuideManifestResourceType",
    "tests.fixtures.resources.implementationguide.ImplementationGuideManifestResource",
)

IngredientType = create_fhir_type(
    "IngredientType", "tests.fixtures.resources.ingredient.Ingredient"
)

IngredientManufacturerType = create_fhir_type(
    "IngredientManufacturerType",
    "tests.fixtures.resources.ingredient.IngredientManufacturer",
)

IngredientSubstanceType = create_fhir_type(
    "IngredientSubstanceType", "tests.fixtures.resources.ingredient.IngredientSubstance"
)

IngredientSubstanceStrengthType = create_fhir_type(
    "IngredientSubstanceStrengthType",
    "tests.fixtures.resources.ingredient.IngredientSubstanceStrength",
)

IngredientSubstanceStrengthReferenceStrengthType = create_fhir_type(
    "IngredientSubstanceStrengthReferenceStrengthType",
    "tests.fixtures.resources.ingredient.IngredientSubstanceStrengthReferenceStrength",
)

InsurancePlanType = create_fhir_type(
    "InsurancePlanType", "tests.fixtures.resources.insuranceplan.InsurancePlan"
)

InsurancePlanCoverageType = create_fhir_type(
    "InsurancePlanCoverageType",
    "tests.fixtures.resources.insuranceplan.InsurancePlanCoverage",
)

InsurancePlanCoverageBenefitType = create_fhir_type(
    "InsurancePlanCoverageBenefitType",
    "tests.fixtures.resources.insuranceplan.InsurancePlanCoverageBenefit",
)

InsurancePlanCoverageBenefitLimitType = create_fhir_type(
    "InsurancePlanCoverageBenefitLimitType",
    "tests.fixtures.resources.insuranceplan.InsurancePlanCoverageBenefitLimit",
)

InsurancePlanPlanType = create_fhir_type(
    "InsurancePlanPlanType", "tests.fixtures.resources.insuranceplan.InsurancePlanPlan"
)

InsurancePlanPlanGeneralCostType = create_fhir_type(
    "InsurancePlanPlanGeneralCostType",
    "tests.fixtures.resources.insuranceplan.InsurancePlanPlanGeneralCost",
)

InsurancePlanPlanSpecificCostType = create_fhir_type(
    "InsurancePlanPlanSpecificCostType",
    "tests.fixtures.resources.insuranceplan.InsurancePlanPlanSpecificCost",
)

InsurancePlanPlanSpecificCostBenefitType = create_fhir_type(
    "InsurancePlanPlanSpecificCostBenefitType",
    "tests.fixtures.resources.insuranceplan.InsurancePlanPlanSpecificCostBenefit",
)

InsurancePlanPlanSpecificCostBenefitCostType = create_fhir_type(
    "InsurancePlanPlanSpecificCostBenefitCostType",
    "tests.fixtures.resources.insuranceplan.InsurancePlanPlanSpecificCostBenefitCost",
)

InventoryItemType = create_fhir_type(
    "InventoryItemType", "tests.fixtures.resources.inventoryitem.InventoryItem"
)

InventoryItemAssociationType = create_fhir_type(
    "InventoryItemAssociationType",
    "tests.fixtures.resources.inventoryitem.InventoryItemAssociation",
)

InventoryItemCharacteristicType = create_fhir_type(
    "InventoryItemCharacteristicType",
    "tests.fixtures.resources.inventoryitem.InventoryItemCharacteristic",
)

InventoryItemDescriptionType = create_fhir_type(
    "InventoryItemDescriptionType",
    "tests.fixtures.resources.inventoryitem.InventoryItemDescription",
)

InventoryItemInstanceType = create_fhir_type(
    "InventoryItemInstanceType",
    "tests.fixtures.resources.inventoryitem.InventoryItemInstance",
)

InventoryItemNameType = create_fhir_type(
    "InventoryItemNameType", "tests.fixtures.resources.inventoryitem.InventoryItemName"
)

InventoryItemResponsibleOrganizationType = create_fhir_type(
    "InventoryItemResponsibleOrganizationType",
    "tests.fixtures.resources.inventoryitem.InventoryItemResponsibleOrganization",
)

InventoryReportType = create_fhir_type(
    "InventoryReportType", "tests.fixtures.resources.inventoryreport.InventoryReport"
)

InventoryReportInventoryListingType = create_fhir_type(
    "InventoryReportInventoryListingType",
    "tests.fixtures.resources.inventoryreport.InventoryReportInventoryListing",
)

InventoryReportInventoryListingItemType = create_fhir_type(
    "InventoryReportInventoryListingItemType",
    "tests.fixtures.resources.inventoryreport.InventoryReportInventoryListingItem",
)

InvoiceType = create_fhir_type(
    "InvoiceType", "tests.fixtures.resources.invoice.Invoice"
)

InvoiceLineItemType = create_fhir_type(
    "InvoiceLineItemType", "tests.fixtures.resources.invoice.InvoiceLineItem"
)

InvoiceParticipantType = create_fhir_type(
    "InvoiceParticipantType", "tests.fixtures.resources.invoice.InvoiceParticipant"
)

LibraryType = create_fhir_type(
    "LibraryType", "tests.fixtures.resources.library.Library"
)

LinkageType = create_fhir_type(
    "LinkageType", "tests.fixtures.resources.linkage.Linkage"
)

LinkageItemType = create_fhir_type(
    "LinkageItemType", "tests.fixtures.resources.linkage.LinkageItem"
)

ListType = create_fhir_type("ListType", "tests.fixtures.resources.list.List")

ListEntryType = create_fhir_type(
    "ListEntryType", "tests.fixtures.resources.list.ListEntry"
)

LocationType = create_fhir_type(
    "LocationType", "tests.fixtures.resources.location.Location"
)

LocationPositionType = create_fhir_type(
    "LocationPositionType", "tests.fixtures.resources.location.LocationPosition"
)

ManufacturedItemDefinitionType = create_fhir_type(
    "ManufacturedItemDefinitionType",
    "tests.fixtures.resources.manufactureditemdefinition.ManufacturedItemDefinition",
)

ManufacturedItemDefinitionComponentType = create_fhir_type(
    "ManufacturedItemDefinitionComponentType",
    "tests.fixtures.resources.manufactureditemdefinition.ManufacturedItemDefinitionComponent",
)

ManufacturedItemDefinitionComponentConstituentType = create_fhir_type(
    "ManufacturedItemDefinitionComponentConstituentType",
    "tests.fixtures.resources.manufactureditemdefinition.ManufacturedItemDefinitionComponentConstituent",
)

ManufacturedItemDefinitionPropertyType = create_fhir_type(
    "ManufacturedItemDefinitionPropertyType",
    "tests.fixtures.resources.manufactureditemdefinition.ManufacturedItemDefinitionProperty",
)

MarketingStatusType = create_fhir_type(
    "MarketingStatusType", "tests.fixtures.resources.marketingstatus.MarketingStatus"
)

MeasureType = create_fhir_type(
    "MeasureType", "tests.fixtures.resources.measure.Measure"
)

MeasureGroupType = create_fhir_type(
    "MeasureGroupType", "tests.fixtures.resources.measure.MeasureGroup"
)

MeasureGroupPopulationType = create_fhir_type(
    "MeasureGroupPopulationType",
    "tests.fixtures.resources.measure.MeasureGroupPopulation",
)

MeasureGroupStratifierType = create_fhir_type(
    "MeasureGroupStratifierType",
    "tests.fixtures.resources.measure.MeasureGroupStratifier",
)

MeasureGroupStratifierComponentType = create_fhir_type(
    "MeasureGroupStratifierComponentType",
    "tests.fixtures.resources.measure.MeasureGroupStratifierComponent",
)

MeasureReportType = create_fhir_type(
    "MeasureReportType", "tests.fixtures.resources.measurereport.MeasureReport"
)

MeasureReportGroupType = create_fhir_type(
    "MeasureReportGroupType",
    "tests.fixtures.resources.measurereport.MeasureReportGroup",
)

MeasureReportGroupPopulationType = create_fhir_type(
    "MeasureReportGroupPopulationType",
    "tests.fixtures.resources.measurereport.MeasureReportGroupPopulation",
)

MeasureReportGroupStratifierType = create_fhir_type(
    "MeasureReportGroupStratifierType",
    "tests.fixtures.resources.measurereport.MeasureReportGroupStratifier",
)

MeasureReportGroupStratifierStratumType = create_fhir_type(
    "MeasureReportGroupStratifierStratumType",
    "tests.fixtures.resources.measurereport.MeasureReportGroupStratifierStratum",
)

MeasureReportGroupStratifierStratumComponentType = create_fhir_type(
    "MeasureReportGroupStratifierStratumComponentType",
    "tests.fixtures.resources.measurereport.MeasureReportGroupStratifierStratumComponent",
)

MeasureReportGroupStratifierStratumPopulationType = create_fhir_type(
    "MeasureReportGroupStratifierStratumPopulationType",
    "tests.fixtures.resources.measurereport.MeasureReportGroupStratifierStratumPopulation",
)

MeasureSupplementalDataType = create_fhir_type(
    "MeasureSupplementalDataType",
    "tests.fixtures.resources.measure.MeasureSupplementalData",
)

MeasureTermType = create_fhir_type(
    "MeasureTermType", "tests.fixtures.resources.measure.MeasureTerm"
)

MedicationType = create_fhir_type(
    "MedicationType", "tests.fixtures.resources.medication.Medication"
)

MedicationAdministrationType = create_fhir_type(
    "MedicationAdministrationType",
    "tests.fixtures.resources.medicationadministration.MedicationAdministration",
)

MedicationAdministrationDosageType = create_fhir_type(
    "MedicationAdministrationDosageType",
    "tests.fixtures.resources.medicationadministration.MedicationAdministrationDosage",
)

MedicationAdministrationPerformerType = create_fhir_type(
    "MedicationAdministrationPerformerType",
    "tests.fixtures.resources.medicationadministration.MedicationAdministrationPerformer",
)

MedicationBatchType = create_fhir_type(
    "MedicationBatchType", "tests.fixtures.resources.medication.MedicationBatch"
)

MedicationDispenseType = create_fhir_type(
    "MedicationDispenseType",
    "tests.fixtures.resources.medicationdispense.MedicationDispense",
)

MedicationDispensePerformerType = create_fhir_type(
    "MedicationDispensePerformerType",
    "tests.fixtures.resources.medicationdispense.MedicationDispensePerformer",
)

MedicationDispenseSubstitutionType = create_fhir_type(
    "MedicationDispenseSubstitutionType",
    "tests.fixtures.resources.medicationdispense.MedicationDispenseSubstitution",
)

MedicationIngredientType = create_fhir_type(
    "MedicationIngredientType",
    "tests.fixtures.resources.medication.MedicationIngredient",
)

MedicationKnowledgeType = create_fhir_type(
    "MedicationKnowledgeType",
    "tests.fixtures.resources.medicationknowledge.MedicationKnowledge",
)

MedicationKnowledgeCostType = create_fhir_type(
    "MedicationKnowledgeCostType",
    "tests.fixtures.resources.medicationknowledge.MedicationKnowledgeCost",
)

MedicationKnowledgeDefinitionalType = create_fhir_type(
    "MedicationKnowledgeDefinitionalType",
    "tests.fixtures.resources.medicationknowledge.MedicationKnowledgeDefinitional",
)

MedicationKnowledgeDefinitionalDrugCharacteristicType = create_fhir_type(
    "MedicationKnowledgeDefinitionalDrugCharacteristicType",
    "tests.fixtures.resources.medicationknowledge.MedicationKnowledgeDefinitionalDrugCharacteristic",
)

MedicationKnowledgeDefinitionalIngredientType = create_fhir_type(
    "MedicationKnowledgeDefinitionalIngredientType",
    "tests.fixtures.resources.medicationknowledge.MedicationKnowledgeDefinitionalIngredient",
)

MedicationKnowledgeIndicationGuidelineType = create_fhir_type(
    "MedicationKnowledgeIndicationGuidelineType",
    "tests.fixtures.resources.medicationknowledge.MedicationKnowledgeIndicationGuideline",
)

MedicationKnowledgeIndicationGuidelineDosingGuidelineType = create_fhir_type(
    "MedicationKnowledgeIndicationGuidelineDosingGuidelineType",
    "tests.fixtures.resources.medicationknowledge.MedicationKnowledgeIndicationGuidelineDosingGuideline",
)

MedicationKnowledgeIndicationGuidelineDosingGuidelineDosageType = create_fhir_type(
    "MedicationKnowledgeIndicationGuidelineDosingGuidelineDosageType",
    "tests.fixtures.resources.medicationknowledge.MedicationKnowledgeIndicationGuidelineDosingGuidelineDosage",
)

MedicationKnowledgeIndicationGuidelineDosingGuidelinePatientCharacteristicType = create_fhir_type(
    "MedicationKnowledgeIndicationGuidelineDosingGuidelinePatientCharacteristicType",
    "tests.fixtures.resources.medicationknowledge.MedicationKnowledgeIndicationGuidelineDosingGuidelinePatientCharacteristic",
)

MedicationKnowledgeMedicineClassificationType = create_fhir_type(
    "MedicationKnowledgeMedicineClassificationType",
    "tests.fixtures.resources.medicationknowledge.MedicationKnowledgeMedicineClassification",
)

MedicationKnowledgeMonitoringProgramType = create_fhir_type(
    "MedicationKnowledgeMonitoringProgramType",
    "tests.fixtures.resources.medicationknowledge.MedicationKnowledgeMonitoringProgram",
)

MedicationKnowledgeMonographType = create_fhir_type(
    "MedicationKnowledgeMonographType",
    "tests.fixtures.resources.medicationknowledge.MedicationKnowledgeMonograph",
)

MedicationKnowledgePackagingType = create_fhir_type(
    "MedicationKnowledgePackagingType",
    "tests.fixtures.resources.medicationknowledge.MedicationKnowledgePackaging",
)

MedicationKnowledgeRegulatoryType = create_fhir_type(
    "MedicationKnowledgeRegulatoryType",
    "tests.fixtures.resources.medicationknowledge.MedicationKnowledgeRegulatory",
)

MedicationKnowledgeRegulatoryMaxDispenseType = create_fhir_type(
    "MedicationKnowledgeRegulatoryMaxDispenseType",
    "tests.fixtures.resources.medicationknowledge.MedicationKnowledgeRegulatoryMaxDispense",
)

MedicationKnowledgeRegulatorySubstitutionType = create_fhir_type(
    "MedicationKnowledgeRegulatorySubstitutionType",
    "tests.fixtures.resources.medicationknowledge.MedicationKnowledgeRegulatorySubstitution",
)

MedicationKnowledgeRelatedMedicationKnowledgeType = create_fhir_type(
    "MedicationKnowledgeRelatedMedicationKnowledgeType",
    "tests.fixtures.resources.medicationknowledge.MedicationKnowledgeRelatedMedicationKnowledge",
)

MedicationKnowledgeStorageGuidelineType = create_fhir_type(
    "MedicationKnowledgeStorageGuidelineType",
    "tests.fixtures.resources.medicationknowledge.MedicationKnowledgeStorageGuideline",
)

MedicationKnowledgeStorageGuidelineEnvironmentalSettingType = create_fhir_type(
    "MedicationKnowledgeStorageGuidelineEnvironmentalSettingType",
    "tests.fixtures.resources.medicationknowledge.MedicationKnowledgeStorageGuidelineEnvironmentalSetting",
)

MedicationRequestType = create_fhir_type(
    "MedicationRequestType",
    "tests.fixtures.resources.medicationrequest.MedicationRequest",
)

MedicationRequestDispenseRequestType = create_fhir_type(
    "MedicationRequestDispenseRequestType",
    "tests.fixtures.resources.medicationrequest.MedicationRequestDispenseRequest",
)

MedicationRequestDispenseRequestInitialFillType = create_fhir_type(
    "MedicationRequestDispenseRequestInitialFillType",
    "tests.fixtures.resources.medicationrequest.MedicationRequestDispenseRequestInitialFill",
)

MedicationRequestSubstitutionType = create_fhir_type(
    "MedicationRequestSubstitutionType",
    "tests.fixtures.resources.medicationrequest.MedicationRequestSubstitution",
)

MedicationStatementType = create_fhir_type(
    "MedicationStatementType",
    "tests.fixtures.resources.medicationstatement.MedicationStatement",
)

MedicationStatementAdherenceType = create_fhir_type(
    "MedicationStatementAdherenceType",
    "tests.fixtures.resources.medicationstatement.MedicationStatementAdherence",
)

MedicinalProductDefinitionType = create_fhir_type(
    "MedicinalProductDefinitionType",
    "tests.fixtures.resources.medicinalproductdefinition.MedicinalProductDefinition",
)

MedicinalProductDefinitionCharacteristicType = create_fhir_type(
    "MedicinalProductDefinitionCharacteristicType",
    "tests.fixtures.resources.medicinalproductdefinition.MedicinalProductDefinitionCharacteristic",
)

MedicinalProductDefinitionContactType = create_fhir_type(
    "MedicinalProductDefinitionContactType",
    "tests.fixtures.resources.medicinalproductdefinition.MedicinalProductDefinitionContact",
)

MedicinalProductDefinitionCrossReferenceType = create_fhir_type(
    "MedicinalProductDefinitionCrossReferenceType",
    "tests.fixtures.resources.medicinalproductdefinition.MedicinalProductDefinitionCrossReference",
)

MedicinalProductDefinitionNameType = create_fhir_type(
    "MedicinalProductDefinitionNameType",
    "tests.fixtures.resources.medicinalproductdefinition.MedicinalProductDefinitionName",
)

MedicinalProductDefinitionNamePartType = create_fhir_type(
    "MedicinalProductDefinitionNamePartType",
    "tests.fixtures.resources.medicinalproductdefinition.MedicinalProductDefinitionNamePart",
)

MedicinalProductDefinitionNameUsageType = create_fhir_type(
    "MedicinalProductDefinitionNameUsageType",
    "tests.fixtures.resources.medicinalproductdefinition.MedicinalProductDefinitionNameUsage",
)

MedicinalProductDefinitionOperationType = create_fhir_type(
    "MedicinalProductDefinitionOperationType",
    "tests.fixtures.resources.medicinalproductdefinition.MedicinalProductDefinitionOperation",
)

MessageDefinitionType = create_fhir_type(
    "MessageDefinitionType",
    "tests.fixtures.resources.messagedefinition.MessageDefinition",
)

MessageDefinitionAllowedResponseType = create_fhir_type(
    "MessageDefinitionAllowedResponseType",
    "tests.fixtures.resources.messagedefinition.MessageDefinitionAllowedResponse",
)

MessageDefinitionFocusType = create_fhir_type(
    "MessageDefinitionFocusType",
    "tests.fixtures.resources.messagedefinition.MessageDefinitionFocus",
)

MessageHeaderType = create_fhir_type(
    "MessageHeaderType", "tests.fixtures.resources.messageheader.MessageHeader"
)

MessageHeaderDestinationType = create_fhir_type(
    "MessageHeaderDestinationType",
    "tests.fixtures.resources.messageheader.MessageHeaderDestination",
)

MessageHeaderResponseType = create_fhir_type(
    "MessageHeaderResponseType",
    "tests.fixtures.resources.messageheader.MessageHeaderResponse",
)

MessageHeaderSourceType = create_fhir_type(
    "MessageHeaderSourceType",
    "tests.fixtures.resources.messageheader.MessageHeaderSource",
)

MetaType = create_fhir_type("MetaType", "tests.fixtures.resources.meta.Meta")

MetadataResourceType = create_fhir_type(
    "MetadataResourceType", "tests.fixtures.resources.metadataresource.MetadataResource"
)

MolecularSequenceType = create_fhir_type(
    "MolecularSequenceType",
    "tests.fixtures.resources.molecularsequence.MolecularSequence",
)

MolecularSequenceRelativeType = create_fhir_type(
    "MolecularSequenceRelativeType",
    "tests.fixtures.resources.molecularsequence.MolecularSequenceRelative",
)

MolecularSequenceRelativeEditType = create_fhir_type(
    "MolecularSequenceRelativeEditType",
    "tests.fixtures.resources.molecularsequence.MolecularSequenceRelativeEdit",
)

MolecularSequenceRelativeStartingSequenceType = create_fhir_type(
    "MolecularSequenceRelativeStartingSequenceType",
    "tests.fixtures.resources.molecularsequence.MolecularSequenceRelativeStartingSequence",
)

MonetaryComponentType = create_fhir_type(
    "MonetaryComponentType",
    "tests.fixtures.resources.monetarycomponent.MonetaryComponent",
)

MoneyType = create_fhir_type("MoneyType", "tests.fixtures.resources.money.Money")

NamingSystemType = create_fhir_type(
    "NamingSystemType", "tests.fixtures.resources.namingsystem.NamingSystem"
)

NamingSystemUniqueIdType = create_fhir_type(
    "NamingSystemUniqueIdType",
    "tests.fixtures.resources.namingsystem.NamingSystemUniqueId",
)

NarrativeType = create_fhir_type(
    "NarrativeType", "tests.fixtures.resources.narrative.Narrative"
)

NutritionIntakeType = create_fhir_type(
    "NutritionIntakeType", "tests.fixtures.resources.nutritionintake.NutritionIntake"
)

NutritionIntakeConsumedItemType = create_fhir_type(
    "NutritionIntakeConsumedItemType",
    "tests.fixtures.resources.nutritionintake.NutritionIntakeConsumedItem",
)

NutritionIntakeIngredientLabelType = create_fhir_type(
    "NutritionIntakeIngredientLabelType",
    "tests.fixtures.resources.nutritionintake.NutritionIntakeIngredientLabel",
)

NutritionIntakePerformerType = create_fhir_type(
    "NutritionIntakePerformerType",
    "tests.fixtures.resources.nutritionintake.NutritionIntakePerformer",
)

NutritionOrderType = create_fhir_type(
    "NutritionOrderType", "tests.fixtures.resources.nutritionorder.NutritionOrder"
)

NutritionOrderEnteralFormulaType = create_fhir_type(
    "NutritionOrderEnteralFormulaType",
    "tests.fixtures.resources.nutritionorder.NutritionOrderEnteralFormula",
)

NutritionOrderEnteralFormulaAdditiveType = create_fhir_type(
    "NutritionOrderEnteralFormulaAdditiveType",
    "tests.fixtures.resources.nutritionorder.NutritionOrderEnteralFormulaAdditive",
)

NutritionOrderEnteralFormulaAdministrationType = create_fhir_type(
    "NutritionOrderEnteralFormulaAdministrationType",
    "tests.fixtures.resources.nutritionorder.NutritionOrderEnteralFormulaAdministration",
)

NutritionOrderEnteralFormulaAdministrationScheduleType = create_fhir_type(
    "NutritionOrderEnteralFormulaAdministrationScheduleType",
    "tests.fixtures.resources.nutritionorder.NutritionOrderEnteralFormulaAdministrationSchedule",
)

NutritionOrderOralDietType = create_fhir_type(
    "NutritionOrderOralDietType",
    "tests.fixtures.resources.nutritionorder.NutritionOrderOralDiet",
)

NutritionOrderOralDietNutrientType = create_fhir_type(
    "NutritionOrderOralDietNutrientType",
    "tests.fixtures.resources.nutritionorder.NutritionOrderOralDietNutrient",
)

NutritionOrderOralDietScheduleType = create_fhir_type(
    "NutritionOrderOralDietScheduleType",
    "tests.fixtures.resources.nutritionorder.NutritionOrderOralDietSchedule",
)

NutritionOrderOralDietTextureType = create_fhir_type(
    "NutritionOrderOralDietTextureType",
    "tests.fixtures.resources.nutritionorder.NutritionOrderOralDietTexture",
)

NutritionOrderSupplementType = create_fhir_type(
    "NutritionOrderSupplementType",
    "tests.fixtures.resources.nutritionorder.NutritionOrderSupplement",
)

NutritionOrderSupplementScheduleType = create_fhir_type(
    "NutritionOrderSupplementScheduleType",
    "tests.fixtures.resources.nutritionorder.NutritionOrderSupplementSchedule",
)

NutritionProductType = create_fhir_type(
    "NutritionProductType", "tests.fixtures.resources.nutritionproduct.NutritionProduct"
)

NutritionProductCharacteristicType = create_fhir_type(
    "NutritionProductCharacteristicType",
    "tests.fixtures.resources.nutritionproduct.NutritionProductCharacteristic",
)

NutritionProductIngredientType = create_fhir_type(
    "NutritionProductIngredientType",
    "tests.fixtures.resources.nutritionproduct.NutritionProductIngredient",
)

NutritionProductInstanceType = create_fhir_type(
    "NutritionProductInstanceType",
    "tests.fixtures.resources.nutritionproduct.NutritionProductInstance",
)

NutritionProductNutrientType = create_fhir_type(
    "NutritionProductNutrientType",
    "tests.fixtures.resources.nutritionproduct.NutritionProductNutrient",
)

ObservationType = create_fhir_type(
    "ObservationType", "tests.fixtures.resources.observation.Observation"
)

ObservationComponentType = create_fhir_type(
    "ObservationComponentType",
    "tests.fixtures.resources.observation.ObservationComponent",
)

ObservationDefinitionType = create_fhir_type(
    "ObservationDefinitionType",
    "tests.fixtures.resources.observationdefinition.ObservationDefinition",
)

ObservationDefinitionComponentType = create_fhir_type(
    "ObservationDefinitionComponentType",
    "tests.fixtures.resources.observationdefinition.ObservationDefinitionComponent",
)

ObservationDefinitionQualifiedValueType = create_fhir_type(
    "ObservationDefinitionQualifiedValueType",
    "tests.fixtures.resources.observationdefinition.ObservationDefinitionQualifiedValue",
)

ObservationReferenceRangeType = create_fhir_type(
    "ObservationReferenceRangeType",
    "tests.fixtures.resources.observation.ObservationReferenceRange",
)

ObservationTriggeredByType = create_fhir_type(
    "ObservationTriggeredByType",
    "tests.fixtures.resources.observation.ObservationTriggeredBy",
)

OperationDefinitionType = create_fhir_type(
    "OperationDefinitionType",
    "tests.fixtures.resources.operationdefinition.OperationDefinition",
)

OperationDefinitionOverloadType = create_fhir_type(
    "OperationDefinitionOverloadType",
    "tests.fixtures.resources.operationdefinition.OperationDefinitionOverload",
)

OperationDefinitionParameterType = create_fhir_type(
    "OperationDefinitionParameterType",
    "tests.fixtures.resources.operationdefinition.OperationDefinitionParameter",
)

OperationDefinitionParameterBindingType = create_fhir_type(
    "OperationDefinitionParameterBindingType",
    "tests.fixtures.resources.operationdefinition.OperationDefinitionParameterBinding",
)

OperationDefinitionParameterReferencedFromType = create_fhir_type(
    "OperationDefinitionParameterReferencedFromType",
    "tests.fixtures.resources.operationdefinition.OperationDefinitionParameterReferencedFrom",
)

OperationOutcomeType = create_fhir_type(
    "OperationOutcomeType", "tests.fixtures.resources.operationoutcome.OperationOutcome"
)

OperationOutcomeIssueType = create_fhir_type(
    "OperationOutcomeIssueType",
    "tests.fixtures.resources.operationoutcome.OperationOutcomeIssue",
)

OrganizationType = create_fhir_type(
    "OrganizationType", "tests.fixtures.resources.organization.Organization"
)

OrganizationAffiliationType = create_fhir_type(
    "OrganizationAffiliationType",
    "tests.fixtures.resources.organizationaffiliation.OrganizationAffiliation",
)

OrganizationQualificationType = create_fhir_type(
    "OrganizationQualificationType",
    "tests.fixtures.resources.organization.OrganizationQualification",
)

PackagedProductDefinitionType = create_fhir_type(
    "PackagedProductDefinitionType",
    "tests.fixtures.resources.packagedproductdefinition.PackagedProductDefinition",
)

PackagedProductDefinitionLegalStatusOfSupplyType = create_fhir_type(
    "PackagedProductDefinitionLegalStatusOfSupplyType",
    "tests.fixtures.resources.packagedproductdefinition.PackagedProductDefinitionLegalStatusOfSupply",
)

PackagedProductDefinitionPackagingType = create_fhir_type(
    "PackagedProductDefinitionPackagingType",
    "tests.fixtures.resources.packagedproductdefinition.PackagedProductDefinitionPackaging",
)

PackagedProductDefinitionPackagingContainedItemType = create_fhir_type(
    "PackagedProductDefinitionPackagingContainedItemType",
    "tests.fixtures.resources.packagedproductdefinition.PackagedProductDefinitionPackagingContainedItem",
)

PackagedProductDefinitionPackagingPropertyType = create_fhir_type(
    "PackagedProductDefinitionPackagingPropertyType",
    "tests.fixtures.resources.packagedproductdefinition.PackagedProductDefinitionPackagingProperty",
)

ParameterDefinitionType = create_fhir_type(
    "ParameterDefinitionType",
    "tests.fixtures.resources.parameterdefinition.ParameterDefinition",
)

ParametersType = create_fhir_type(
    "ParametersType", "tests.fixtures.resources.parameters.Parameters"
)

ParametersParameterType = create_fhir_type(
    "ParametersParameterType", "tests.fixtures.resources.parameters.ParametersParameter"
)

PatientType = create_fhir_type(
    "PatientType", "tests.fixtures.resources.patient.Patient"
)

PatientCommunicationType = create_fhir_type(
    "PatientCommunicationType", "tests.fixtures.resources.patient.PatientCommunication"
)

PatientContactType = create_fhir_type(
    "PatientContactType", "tests.fixtures.resources.patient.PatientContact"
)

PatientLinkType = create_fhir_type(
    "PatientLinkType", "tests.fixtures.resources.patient.PatientLink"
)

PaymentNoticeType = create_fhir_type(
    "PaymentNoticeType", "tests.fixtures.resources.paymentnotice.PaymentNotice"
)

PaymentReconciliationType = create_fhir_type(
    "PaymentReconciliationType",
    "tests.fixtures.resources.paymentreconciliation.PaymentReconciliation",
)

PaymentReconciliationAllocationType = create_fhir_type(
    "PaymentReconciliationAllocationType",
    "tests.fixtures.resources.paymentreconciliation.PaymentReconciliationAllocation",
)

PaymentReconciliationProcessNoteType = create_fhir_type(
    "PaymentReconciliationProcessNoteType",
    "tests.fixtures.resources.paymentreconciliation.PaymentReconciliationProcessNote",
)

PeriodType = create_fhir_type("PeriodType", "tests.fixtures.resources.period.Period")

PermissionType = create_fhir_type(
    "PermissionType", "tests.fixtures.resources.permission.Permission"
)

PermissionJustificationType = create_fhir_type(
    "PermissionJustificationType",
    "tests.fixtures.resources.permission.PermissionJustification",
)

PermissionRuleType = create_fhir_type(
    "PermissionRuleType", "tests.fixtures.resources.permission.PermissionRule"
)

PermissionRuleActivityType = create_fhir_type(
    "PermissionRuleActivityType",
    "tests.fixtures.resources.permission.PermissionRuleActivity",
)

PermissionRuleDataType = create_fhir_type(
    "PermissionRuleDataType", "tests.fixtures.resources.permission.PermissionRuleData"
)

PermissionRuleDataResourceType = create_fhir_type(
    "PermissionRuleDataResourceType",
    "tests.fixtures.resources.permission.PermissionRuleDataResource",
)

PersonType = create_fhir_type("PersonType", "tests.fixtures.resources.person.Person")

PersonCommunicationType = create_fhir_type(
    "PersonCommunicationType", "tests.fixtures.resources.person.PersonCommunication"
)

PersonLinkType = create_fhir_type(
    "PersonLinkType", "tests.fixtures.resources.person.PersonLink"
)

PlanDefinitionType = create_fhir_type(
    "PlanDefinitionType", "tests.fixtures.resources.plandefinition.PlanDefinition"
)

PlanDefinitionActionType = create_fhir_type(
    "PlanDefinitionActionType",
    "tests.fixtures.resources.plandefinition.PlanDefinitionAction",
)

PlanDefinitionActionConditionType = create_fhir_type(
    "PlanDefinitionActionConditionType",
    "tests.fixtures.resources.plandefinition.PlanDefinitionActionCondition",
)

PlanDefinitionActionDynamicValueType = create_fhir_type(
    "PlanDefinitionActionDynamicValueType",
    "tests.fixtures.resources.plandefinition.PlanDefinitionActionDynamicValue",
)

PlanDefinitionActionInputType = create_fhir_type(
    "PlanDefinitionActionInputType",
    "tests.fixtures.resources.plandefinition.PlanDefinitionActionInput",
)

PlanDefinitionActionOutputType = create_fhir_type(
    "PlanDefinitionActionOutputType",
    "tests.fixtures.resources.plandefinition.PlanDefinitionActionOutput",
)

PlanDefinitionActionParticipantType = create_fhir_type(
    "PlanDefinitionActionParticipantType",
    "tests.fixtures.resources.plandefinition.PlanDefinitionActionParticipant",
)

PlanDefinitionActionRelatedActionType = create_fhir_type(
    "PlanDefinitionActionRelatedActionType",
    "tests.fixtures.resources.plandefinition.PlanDefinitionActionRelatedAction",
)

PlanDefinitionActorType = create_fhir_type(
    "PlanDefinitionActorType",
    "tests.fixtures.resources.plandefinition.PlanDefinitionActor",
)

PlanDefinitionActorOptionType = create_fhir_type(
    "PlanDefinitionActorOptionType",
    "tests.fixtures.resources.plandefinition.PlanDefinitionActorOption",
)

PlanDefinitionGoalType = create_fhir_type(
    "PlanDefinitionGoalType",
    "tests.fixtures.resources.plandefinition.PlanDefinitionGoal",
)

PlanDefinitionGoalTargetType = create_fhir_type(
    "PlanDefinitionGoalTargetType",
    "tests.fixtures.resources.plandefinition.PlanDefinitionGoalTarget",
)

PractitionerType = create_fhir_type(
    "PractitionerType", "tests.fixtures.resources.practitioner.Practitioner"
)

PractitionerCommunicationType = create_fhir_type(
    "PractitionerCommunicationType",
    "tests.fixtures.resources.practitioner.PractitionerCommunication",
)

PractitionerQualificationType = create_fhir_type(
    "PractitionerQualificationType",
    "tests.fixtures.resources.practitioner.PractitionerQualification",
)

PractitionerRoleType = create_fhir_type(
    "PractitionerRoleType", "tests.fixtures.resources.practitionerrole.PractitionerRole"
)

PrimitiveTypeType = create_fhir_type(
    "PrimitiveTypeType", "tests.fixtures.resources.primitivetype.PrimitiveType"
)

ProcedureType = create_fhir_type(
    "ProcedureType", "tests.fixtures.resources.procedure.Procedure"
)

ProcedureFocalDeviceType = create_fhir_type(
    "ProcedureFocalDeviceType",
    "tests.fixtures.resources.procedure.ProcedureFocalDevice",
)

ProcedurePerformerType = create_fhir_type(
    "ProcedurePerformerType", "tests.fixtures.resources.procedure.ProcedurePerformer"
)

ProductShelfLifeType = create_fhir_type(
    "ProductShelfLifeType", "tests.fixtures.resources.productshelflife.ProductShelfLife"
)

ProvenanceType = create_fhir_type(
    "ProvenanceType", "tests.fixtures.resources.provenance.Provenance"
)

ProvenanceAgentType = create_fhir_type(
    "ProvenanceAgentType", "tests.fixtures.resources.provenance.ProvenanceAgent"
)

ProvenanceEntityType = create_fhir_type(
    "ProvenanceEntityType", "tests.fixtures.resources.provenance.ProvenanceEntity"
)

QuantityType = create_fhir_type(
    "QuantityType", "tests.fixtures.resources.quantity.Quantity"
)

QuestionnaireType = create_fhir_type(
    "QuestionnaireType", "tests.fixtures.resources.questionnaire.Questionnaire"
)

QuestionnaireItemType = create_fhir_type(
    "QuestionnaireItemType", "tests.fixtures.resources.questionnaire.QuestionnaireItem"
)

QuestionnaireItemAnswerOptionType = create_fhir_type(
    "QuestionnaireItemAnswerOptionType",
    "tests.fixtures.resources.questionnaire.QuestionnaireItemAnswerOption",
)

QuestionnaireItemEnableWhenType = create_fhir_type(
    "QuestionnaireItemEnableWhenType",
    "tests.fixtures.resources.questionnaire.QuestionnaireItemEnableWhen",
)

QuestionnaireItemInitialType = create_fhir_type(
    "QuestionnaireItemInitialType",
    "tests.fixtures.resources.questionnaire.QuestionnaireItemInitial",
)

QuestionnaireResponseType = create_fhir_type(
    "QuestionnaireResponseType",
    "tests.fixtures.resources.questionnaireresponse.QuestionnaireResponse",
)

QuestionnaireResponseItemType = create_fhir_type(
    "QuestionnaireResponseItemType",
    "tests.fixtures.resources.questionnaireresponse.QuestionnaireResponseItem",
)

QuestionnaireResponseItemAnswerType = create_fhir_type(
    "QuestionnaireResponseItemAnswerType",
    "tests.fixtures.resources.questionnaireresponse.QuestionnaireResponseItemAnswer",
)

RangeType = create_fhir_type("RangeType", "tests.fixtures.resources.range.Range")

RatioType = create_fhir_type("RatioType", "tests.fixtures.resources.ratio.Ratio")

RatioRangeType = create_fhir_type(
    "RatioRangeType", "tests.fixtures.resources.ratiorange.RatioRange"
)

ReferenceType = create_fhir_type(
    "ReferenceType", "tests.fixtures.resources.reference.Reference"
)

RegulatedAuthorizationType = create_fhir_type(
    "RegulatedAuthorizationType",
    "tests.fixtures.resources.regulatedauthorization.RegulatedAuthorization",
)

RegulatedAuthorizationCaseType = create_fhir_type(
    "RegulatedAuthorizationCaseType",
    "tests.fixtures.resources.regulatedauthorization.RegulatedAuthorizationCase",
)

RelatedArtifactType = create_fhir_type(
    "RelatedArtifactType", "tests.fixtures.resources.relatedartifact.RelatedArtifact"
)

RelatedPersonType = create_fhir_type(
    "RelatedPersonType", "tests.fixtures.resources.relatedperson.RelatedPerson"
)

RelatedPersonCommunicationType = create_fhir_type(
    "RelatedPersonCommunicationType",
    "tests.fixtures.resources.relatedperson.RelatedPersonCommunication",
)

RequestOrchestrationType = create_fhir_type(
    "RequestOrchestrationType",
    "tests.fixtures.resources.requestorchestration.RequestOrchestration",
)

RequestOrchestrationActionType = create_fhir_type(
    "RequestOrchestrationActionType",
    "tests.fixtures.resources.requestorchestration.RequestOrchestrationAction",
)

RequestOrchestrationActionConditionType = create_fhir_type(
    "RequestOrchestrationActionConditionType",
    "tests.fixtures.resources.requestorchestration.RequestOrchestrationActionCondition",
)

RequestOrchestrationActionDynamicValueType = create_fhir_type(
    "RequestOrchestrationActionDynamicValueType",
    "tests.fixtures.resources.requestorchestration.RequestOrchestrationActionDynamicValue",
)

RequestOrchestrationActionInputType = create_fhir_type(
    "RequestOrchestrationActionInputType",
    "tests.fixtures.resources.requestorchestration.RequestOrchestrationActionInput",
)

RequestOrchestrationActionOutputType = create_fhir_type(
    "RequestOrchestrationActionOutputType",
    "tests.fixtures.resources.requestorchestration.RequestOrchestrationActionOutput",
)

RequestOrchestrationActionParticipantType = create_fhir_type(
    "RequestOrchestrationActionParticipantType",
    "tests.fixtures.resources.requestorchestration.RequestOrchestrationActionParticipant",
)

RequestOrchestrationActionRelatedActionType = create_fhir_type(
    "RequestOrchestrationActionRelatedActionType",
    "tests.fixtures.resources.requestorchestration.RequestOrchestrationActionRelatedAction",
)

RequirementsType = create_fhir_type(
    "RequirementsType", "tests.fixtures.resources.requirements.Requirements"
)

RequirementsStatementType = create_fhir_type(
    "RequirementsStatementType",
    "tests.fixtures.resources.requirements.RequirementsStatement",
)

ResearchStudyType = create_fhir_type(
    "ResearchStudyType", "tests.fixtures.resources.researchstudy.ResearchStudy"
)

ResearchStudyAssociatedPartyType = create_fhir_type(
    "ResearchStudyAssociatedPartyType",
    "tests.fixtures.resources.researchstudy.ResearchStudyAssociatedParty",
)

ResearchStudyComparisonGroupType = create_fhir_type(
    "ResearchStudyComparisonGroupType",
    "tests.fixtures.resources.researchstudy.ResearchStudyComparisonGroup",
)

ResearchStudyLabelType = create_fhir_type(
    "ResearchStudyLabelType",
    "tests.fixtures.resources.researchstudy.ResearchStudyLabel",
)

ResearchStudyObjectiveType = create_fhir_type(
    "ResearchStudyObjectiveType",
    "tests.fixtures.resources.researchstudy.ResearchStudyObjective",
)

ResearchStudyOutcomeMeasureType = create_fhir_type(
    "ResearchStudyOutcomeMeasureType",
    "tests.fixtures.resources.researchstudy.ResearchStudyOutcomeMeasure",
)

ResearchStudyProgressStatusType = create_fhir_type(
    "ResearchStudyProgressStatusType",
    "tests.fixtures.resources.researchstudy.ResearchStudyProgressStatus",
)

ResearchStudyRecruitmentType = create_fhir_type(
    "ResearchStudyRecruitmentType",
    "tests.fixtures.resources.researchstudy.ResearchStudyRecruitment",
)

ResearchSubjectType = create_fhir_type(
    "ResearchSubjectType", "tests.fixtures.resources.researchsubject.ResearchSubject"
)

ResearchSubjectProgressType = create_fhir_type(
    "ResearchSubjectProgressType",
    "tests.fixtures.resources.researchsubject.ResearchSubjectProgress",
)

ResourceType = create_fhir_element_or_resource_type(
    "ResourceType", "tests.fixtures.resources.resource.Resource"
)

RiskAssessmentType = create_fhir_type(
    "RiskAssessmentType", "tests.fixtures.resources.riskassessment.RiskAssessment"
)

RiskAssessmentPredictionType = create_fhir_type(
    "RiskAssessmentPredictionType",
    "tests.fixtures.resources.riskassessment.RiskAssessmentPrediction",
)

SampledDataType = create_fhir_type(
    "SampledDataType", "tests.fixtures.resources.sampleddata.SampledData"
)

ScheduleType = create_fhir_type(
    "ScheduleType", "tests.fixtures.resources.schedule.Schedule"
)

SearchParameterType = create_fhir_type(
    "SearchParameterType", "tests.fixtures.resources.searchparameter.SearchParameter"
)

SearchParameterComponentType = create_fhir_type(
    "SearchParameterComponentType",
    "tests.fixtures.resources.searchparameter.SearchParameterComponent",
)

ServiceRequestType = create_fhir_type(
    "ServiceRequestType", "tests.fixtures.resources.servicerequest.ServiceRequest"
)

ServiceRequestOrderDetailType = create_fhir_type(
    "ServiceRequestOrderDetailType",
    "tests.fixtures.resources.servicerequest.ServiceRequestOrderDetail",
)

ServiceRequestOrderDetailParameterType = create_fhir_type(
    "ServiceRequestOrderDetailParameterType",
    "tests.fixtures.resources.servicerequest.ServiceRequestOrderDetailParameter",
)

ServiceRequestPatientInstructionType = create_fhir_type(
    "ServiceRequestPatientInstructionType",
    "tests.fixtures.resources.servicerequest.ServiceRequestPatientInstruction",
)

SignatureType = create_fhir_type(
    "SignatureType", "tests.fixtures.resources.signature.Signature"
)

SlotType = create_fhir_type("SlotType", "tests.fixtures.resources.slot.Slot")

SpecimenType = create_fhir_type(
    "SpecimenType", "tests.fixtures.resources.specimen.Specimen"
)

SpecimenCollectionType = create_fhir_type(
    "SpecimenCollectionType", "tests.fixtures.resources.specimen.SpecimenCollection"
)

SpecimenContainerType = create_fhir_type(
    "SpecimenContainerType", "tests.fixtures.resources.specimen.SpecimenContainer"
)

SpecimenDefinitionType = create_fhir_type(
    "SpecimenDefinitionType",
    "tests.fixtures.resources.specimendefinition.SpecimenDefinition",
)

SpecimenDefinitionTypeTestedType = create_fhir_type(
    "SpecimenDefinitionTypeTestedType",
    "tests.fixtures.resources.specimendefinition.SpecimenDefinitionTypeTested",
)

SpecimenDefinitionTypeTestedContainerType = create_fhir_type(
    "SpecimenDefinitionTypeTestedContainerType",
    "tests.fixtures.resources.specimendefinition.SpecimenDefinitionTypeTestedContainer",
)

SpecimenDefinitionTypeTestedContainerAdditiveType = create_fhir_type(
    "SpecimenDefinitionTypeTestedContainerAdditiveType",
    "tests.fixtures.resources.specimendefinition.SpecimenDefinitionTypeTestedContainerAdditive",
)

SpecimenDefinitionTypeTestedHandlingType = create_fhir_type(
    "SpecimenDefinitionTypeTestedHandlingType",
    "tests.fixtures.resources.specimendefinition.SpecimenDefinitionTypeTestedHandling",
)

SpecimenFeatureType = create_fhir_type(
    "SpecimenFeatureType", "tests.fixtures.resources.specimen.SpecimenFeature"
)

SpecimenProcessingType = create_fhir_type(
    "SpecimenProcessingType", "tests.fixtures.resources.specimen.SpecimenProcessing"
)

StructureDefinitionType = create_fhir_type(
    "StructureDefinitionType",
    "tests.fixtures.resources.structuredefinition.StructureDefinition",
)

StructureDefinitionContextType = create_fhir_type(
    "StructureDefinitionContextType",
    "tests.fixtures.resources.structuredefinition.StructureDefinitionContext",
)

StructureDefinitionDifferentialType = create_fhir_type(
    "StructureDefinitionDifferentialType",
    "tests.fixtures.resources.structuredefinition.StructureDefinitionDifferential",
)

StructureDefinitionMappingType = create_fhir_type(
    "StructureDefinitionMappingType",
    "tests.fixtures.resources.structuredefinition.StructureDefinitionMapping",
)

StructureDefinitionSnapshotType = create_fhir_type(
    "StructureDefinitionSnapshotType",
    "tests.fixtures.resources.structuredefinition.StructureDefinitionSnapshot",
)

StructureMapType = create_fhir_type(
    "StructureMapType", "tests.fixtures.resources.structuremap.StructureMap"
)

StructureMapConstType = create_fhir_type(
    "StructureMapConstType", "tests.fixtures.resources.structuremap.StructureMapConst"
)

StructureMapGroupType = create_fhir_type(
    "StructureMapGroupType", "tests.fixtures.resources.structuremap.StructureMapGroup"
)

StructureMapGroupInputType = create_fhir_type(
    "StructureMapGroupInputType",
    "tests.fixtures.resources.structuremap.StructureMapGroupInput",
)

StructureMapGroupRuleType = create_fhir_type(
    "StructureMapGroupRuleType",
    "tests.fixtures.resources.structuremap.StructureMapGroupRule",
)

StructureMapGroupRuleDependentType = create_fhir_type(
    "StructureMapGroupRuleDependentType",
    "tests.fixtures.resources.structuremap.StructureMapGroupRuleDependent",
)

StructureMapGroupRuleSourceType = create_fhir_type(
    "StructureMapGroupRuleSourceType",
    "tests.fixtures.resources.structuremap.StructureMapGroupRuleSource",
)

StructureMapGroupRuleTargetType = create_fhir_type(
    "StructureMapGroupRuleTargetType",
    "tests.fixtures.resources.structuremap.StructureMapGroupRuleTarget",
)

StructureMapGroupRuleTargetParameterType = create_fhir_type(
    "StructureMapGroupRuleTargetParameterType",
    "tests.fixtures.resources.structuremap.StructureMapGroupRuleTargetParameter",
)

StructureMapStructureType = create_fhir_type(
    "StructureMapStructureType",
    "tests.fixtures.resources.structuremap.StructureMapStructure",
)

SubscriptionType = create_fhir_type(
    "SubscriptionType", "tests.fixtures.resources.subscription.Subscription"
)

SubscriptionFilterByType = create_fhir_type(
    "SubscriptionFilterByType",
    "tests.fixtures.resources.subscription.SubscriptionFilterBy",
)

SubscriptionParameterType = create_fhir_type(
    "SubscriptionParameterType",
    "tests.fixtures.resources.subscription.SubscriptionParameter",
)

SubscriptionStatusType = create_fhir_type(
    "SubscriptionStatusType",
    "tests.fixtures.resources.subscriptionstatus.SubscriptionStatus",
)

SubscriptionStatusNotificationEventType = create_fhir_type(
    "SubscriptionStatusNotificationEventType",
    "tests.fixtures.resources.subscriptionstatus.SubscriptionStatusNotificationEvent",
)

SubscriptionTopicType = create_fhir_type(
    "SubscriptionTopicType",
    "tests.fixtures.resources.subscriptiontopic.SubscriptionTopic",
)

SubscriptionTopicCanFilterByType = create_fhir_type(
    "SubscriptionTopicCanFilterByType",
    "tests.fixtures.resources.subscriptiontopic.SubscriptionTopicCanFilterBy",
)

SubscriptionTopicEventTriggerType = create_fhir_type(
    "SubscriptionTopicEventTriggerType",
    "tests.fixtures.resources.subscriptiontopic.SubscriptionTopicEventTrigger",
)

SubscriptionTopicNotificationShapeType = create_fhir_type(
    "SubscriptionTopicNotificationShapeType",
    "tests.fixtures.resources.subscriptiontopic.SubscriptionTopicNotificationShape",
)

SubscriptionTopicResourceTriggerType = create_fhir_type(
    "SubscriptionTopicResourceTriggerType",
    "tests.fixtures.resources.subscriptiontopic.SubscriptionTopicResourceTrigger",
)

SubscriptionTopicResourceTriggerQueryCriteriaType = create_fhir_type(
    "SubscriptionTopicResourceTriggerQueryCriteriaType",
    "tests.fixtures.resources.subscriptiontopic.SubscriptionTopicResourceTriggerQueryCriteria",
)

SubstanceType = create_fhir_type(
    "SubstanceType", "tests.fixtures.resources.substance.Substance"
)

SubstanceDefinitionType = create_fhir_type(
    "SubstanceDefinitionType",
    "tests.fixtures.resources.substancedefinition.SubstanceDefinition",
)

SubstanceDefinitionCharacterizationType = create_fhir_type(
    "SubstanceDefinitionCharacterizationType",
    "tests.fixtures.resources.substancedefinition.SubstanceDefinitionCharacterization",
)

SubstanceDefinitionCodeType = create_fhir_type(
    "SubstanceDefinitionCodeType",
    "tests.fixtures.resources.substancedefinition.SubstanceDefinitionCode",
)

SubstanceDefinitionMoietyType = create_fhir_type(
    "SubstanceDefinitionMoietyType",
    "tests.fixtures.resources.substancedefinition.SubstanceDefinitionMoiety",
)

SubstanceDefinitionMolecularWeightType = create_fhir_type(
    "SubstanceDefinitionMolecularWeightType",
    "tests.fixtures.resources.substancedefinition.SubstanceDefinitionMolecularWeight",
)

SubstanceDefinitionNameType = create_fhir_type(
    "SubstanceDefinitionNameType",
    "tests.fixtures.resources.substancedefinition.SubstanceDefinitionName",
)

SubstanceDefinitionNameOfficialType = create_fhir_type(
    "SubstanceDefinitionNameOfficialType",
    "tests.fixtures.resources.substancedefinition.SubstanceDefinitionNameOfficial",
)

SubstanceDefinitionPropertyType = create_fhir_type(
    "SubstanceDefinitionPropertyType",
    "tests.fixtures.resources.substancedefinition.SubstanceDefinitionProperty",
)

SubstanceDefinitionRelationshipType = create_fhir_type(
    "SubstanceDefinitionRelationshipType",
    "tests.fixtures.resources.substancedefinition.SubstanceDefinitionRelationship",
)

SubstanceDefinitionSourceMaterialType = create_fhir_type(
    "SubstanceDefinitionSourceMaterialType",
    "tests.fixtures.resources.substancedefinition.SubstanceDefinitionSourceMaterial",
)

SubstanceDefinitionStructureType = create_fhir_type(
    "SubstanceDefinitionStructureType",
    "tests.fixtures.resources.substancedefinition.SubstanceDefinitionStructure",
)

SubstanceDefinitionStructureRepresentationType = create_fhir_type(
    "SubstanceDefinitionStructureRepresentationType",
    "tests.fixtures.resources.substancedefinition.SubstanceDefinitionStructureRepresentation",
)

SubstanceIngredientType = create_fhir_type(
    "SubstanceIngredientType", "tests.fixtures.resources.substance.SubstanceIngredient"
)

SubstanceNucleicAcidType = create_fhir_type(
    "SubstanceNucleicAcidType",
    "tests.fixtures.resources.substancenucleicacid.SubstanceNucleicAcid",
)

SubstanceNucleicAcidSubunitType = create_fhir_type(
    "SubstanceNucleicAcidSubunitType",
    "tests.fixtures.resources.substancenucleicacid.SubstanceNucleicAcidSubunit",
)

SubstanceNucleicAcidSubunitLinkageType = create_fhir_type(
    "SubstanceNucleicAcidSubunitLinkageType",
    "tests.fixtures.resources.substancenucleicacid.SubstanceNucleicAcidSubunitLinkage",
)

SubstanceNucleicAcidSubunitSugarType = create_fhir_type(
    "SubstanceNucleicAcidSubunitSugarType",
    "tests.fixtures.resources.substancenucleicacid.SubstanceNucleicAcidSubunitSugar",
)

SubstancePolymerType = create_fhir_type(
    "SubstancePolymerType", "tests.fixtures.resources.substancepolymer.SubstancePolymer"
)

SubstancePolymerMonomerSetType = create_fhir_type(
    "SubstancePolymerMonomerSetType",
    "tests.fixtures.resources.substancepolymer.SubstancePolymerMonomerSet",
)

SubstancePolymerMonomerSetStartingMaterialType = create_fhir_type(
    "SubstancePolymerMonomerSetStartingMaterialType",
    "tests.fixtures.resources.substancepolymer.SubstancePolymerMonomerSetStartingMaterial",
)

SubstancePolymerRepeatType = create_fhir_type(
    "SubstancePolymerRepeatType",
    "tests.fixtures.resources.substancepolymer.SubstancePolymerRepeat",
)

SubstancePolymerRepeatRepeatUnitType = create_fhir_type(
    "SubstancePolymerRepeatRepeatUnitType",
    "tests.fixtures.resources.substancepolymer.SubstancePolymerRepeatRepeatUnit",
)

SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisationType = create_fhir_type(
    "SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisationType",
    "tests.fixtures.resources.substancepolymer.SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisation",
)

SubstancePolymerRepeatRepeatUnitStructuralRepresentationType = create_fhir_type(
    "SubstancePolymerRepeatRepeatUnitStructuralRepresentationType",
    "tests.fixtures.resources.substancepolymer.SubstancePolymerRepeatRepeatUnitStructuralRepresentation",
)

SubstanceProteinType = create_fhir_type(
    "SubstanceProteinType", "tests.fixtures.resources.substanceprotein.SubstanceProtein"
)

SubstanceProteinSubunitType = create_fhir_type(
    "SubstanceProteinSubunitType",
    "tests.fixtures.resources.substanceprotein.SubstanceProteinSubunit",
)

SubstanceReferenceInformationType = create_fhir_type(
    "SubstanceReferenceInformationType",
    "tests.fixtures.resources.substancereferenceinformation.SubstanceReferenceInformation",
)

SubstanceReferenceInformationGeneType = create_fhir_type(
    "SubstanceReferenceInformationGeneType",
    "tests.fixtures.resources.substancereferenceinformation.SubstanceReferenceInformationGene",
)

SubstanceReferenceInformationGeneElementType = create_fhir_type(
    "SubstanceReferenceInformationGeneElementType",
    "tests.fixtures.resources.substancereferenceinformation.SubstanceReferenceInformationGeneElement",
)

SubstanceReferenceInformationTargetType = create_fhir_type(
    "SubstanceReferenceInformationTargetType",
    "tests.fixtures.resources.substancereferenceinformation.SubstanceReferenceInformationTarget",
)

SubstanceSourceMaterialType = create_fhir_type(
    "SubstanceSourceMaterialType",
    "tests.fixtures.resources.substancesourcematerial.SubstanceSourceMaterial",
)

SubstanceSourceMaterialFractionDescriptionType = create_fhir_type(
    "SubstanceSourceMaterialFractionDescriptionType",
    "tests.fixtures.resources.substancesourcematerial.SubstanceSourceMaterialFractionDescription",
)

SubstanceSourceMaterialOrganismType = create_fhir_type(
    "SubstanceSourceMaterialOrganismType",
    "tests.fixtures.resources.substancesourcematerial.SubstanceSourceMaterialOrganism",
)

SubstanceSourceMaterialOrganismAuthorType = create_fhir_type(
    "SubstanceSourceMaterialOrganismAuthorType",
    "tests.fixtures.resources.substancesourcematerial.SubstanceSourceMaterialOrganismAuthor",
)

SubstanceSourceMaterialOrganismHybridType = create_fhir_type(
    "SubstanceSourceMaterialOrganismHybridType",
    "tests.fixtures.resources.substancesourcematerial.SubstanceSourceMaterialOrganismHybrid",
)

SubstanceSourceMaterialOrganismOrganismGeneralType = create_fhir_type(
    "SubstanceSourceMaterialOrganismOrganismGeneralType",
    "tests.fixtures.resources.substancesourcematerial.SubstanceSourceMaterialOrganismOrganismGeneral",
)

SubstanceSourceMaterialPartDescriptionType = create_fhir_type(
    "SubstanceSourceMaterialPartDescriptionType",
    "tests.fixtures.resources.substancesourcematerial.SubstanceSourceMaterialPartDescription",
)

SupplyDeliveryType = create_fhir_type(
    "SupplyDeliveryType", "tests.fixtures.resources.supplydelivery.SupplyDelivery"
)

SupplyDeliverySuppliedItemType = create_fhir_type(
    "SupplyDeliverySuppliedItemType",
    "tests.fixtures.resources.supplydelivery.SupplyDeliverySuppliedItem",
)

SupplyRequestType = create_fhir_type(
    "SupplyRequestType", "tests.fixtures.resources.supplyrequest.SupplyRequest"
)

SupplyRequestParameterType = create_fhir_type(
    "SupplyRequestParameterType",
    "tests.fixtures.resources.supplyrequest.SupplyRequestParameter",
)

TaskType = create_fhir_type("TaskType", "tests.fixtures.resources.task.Task")

TaskInputType = create_fhir_type(
    "TaskInputType", "tests.fixtures.resources.task.TaskInput"
)

TaskOutputType = create_fhir_type(
    "TaskOutputType", "tests.fixtures.resources.task.TaskOutput"
)

TaskPerformerType = create_fhir_type(
    "TaskPerformerType", "tests.fixtures.resources.task.TaskPerformer"
)

TaskRestrictionType = create_fhir_type(
    "TaskRestrictionType", "tests.fixtures.resources.task.TaskRestriction"
)

TerminologyCapabilitiesType = create_fhir_type(
    "TerminologyCapabilitiesType",
    "tests.fixtures.resources.terminologycapabilities.TerminologyCapabilities",
)

TerminologyCapabilitiesClosureType = create_fhir_type(
    "TerminologyCapabilitiesClosureType",
    "tests.fixtures.resources.terminologycapabilities.TerminologyCapabilitiesClosure",
)

TerminologyCapabilitiesCodeSystemType = create_fhir_type(
    "TerminologyCapabilitiesCodeSystemType",
    "tests.fixtures.resources.terminologycapabilities.TerminologyCapabilitiesCodeSystem",
)

TerminologyCapabilitiesCodeSystemVersionType = create_fhir_type(
    "TerminologyCapabilitiesCodeSystemVersionType",
    "tests.fixtures.resources.terminologycapabilities.TerminologyCapabilitiesCodeSystemVersion",
)

TerminologyCapabilitiesCodeSystemVersionFilterType = create_fhir_type(
    "TerminologyCapabilitiesCodeSystemVersionFilterType",
    "tests.fixtures.resources.terminologycapabilities.TerminologyCapabilitiesCodeSystemVersionFilter",
)

TerminologyCapabilitiesExpansionType = create_fhir_type(
    "TerminologyCapabilitiesExpansionType",
    "tests.fixtures.resources.terminologycapabilities.TerminologyCapabilitiesExpansion",
)

TerminologyCapabilitiesExpansionParameterType = create_fhir_type(
    "TerminologyCapabilitiesExpansionParameterType",
    "tests.fixtures.resources.terminologycapabilities.TerminologyCapabilitiesExpansionParameter",
)

TerminologyCapabilitiesImplementationType = create_fhir_type(
    "TerminologyCapabilitiesImplementationType",
    "tests.fixtures.resources.terminologycapabilities.TerminologyCapabilitiesImplementation",
)

TerminologyCapabilitiesSoftwareType = create_fhir_type(
    "TerminologyCapabilitiesSoftwareType",
    "tests.fixtures.resources.terminologycapabilities.TerminologyCapabilitiesSoftware",
)

TerminologyCapabilitiesTranslationType = create_fhir_type(
    "TerminologyCapabilitiesTranslationType",
    "tests.fixtures.resources.terminologycapabilities.TerminologyCapabilitiesTranslation",
)

TerminologyCapabilitiesValidateCodeType = create_fhir_type(
    "TerminologyCapabilitiesValidateCodeType",
    "tests.fixtures.resources.terminologycapabilities.TerminologyCapabilitiesValidateCode",
)

TestPlanType = create_fhir_type(
    "TestPlanType", "tests.fixtures.resources.testplan.TestPlan"
)

TestPlanDependencyType = create_fhir_type(
    "TestPlanDependencyType", "tests.fixtures.resources.testplan.TestPlanDependency"
)

TestPlanTestCaseType = create_fhir_type(
    "TestPlanTestCaseType", "tests.fixtures.resources.testplan.TestPlanTestCase"
)

TestPlanTestCaseAssertionType = create_fhir_type(
    "TestPlanTestCaseAssertionType",
    "tests.fixtures.resources.testplan.TestPlanTestCaseAssertion",
)

TestPlanTestCaseDependencyType = create_fhir_type(
    "TestPlanTestCaseDependencyType",
    "tests.fixtures.resources.testplan.TestPlanTestCaseDependency",
)

TestPlanTestCaseTestDataType = create_fhir_type(
    "TestPlanTestCaseTestDataType",
    "tests.fixtures.resources.testplan.TestPlanTestCaseTestData",
)

TestPlanTestCaseTestRunType = create_fhir_type(
    "TestPlanTestCaseTestRunType",
    "tests.fixtures.resources.testplan.TestPlanTestCaseTestRun",
)

TestPlanTestCaseTestRunScriptType = create_fhir_type(
    "TestPlanTestCaseTestRunScriptType",
    "tests.fixtures.resources.testplan.TestPlanTestCaseTestRunScript",
)

TestReportType = create_fhir_type(
    "TestReportType", "tests.fixtures.resources.testreport.TestReport"
)

TestReportParticipantType = create_fhir_type(
    "TestReportParticipantType",
    "tests.fixtures.resources.testreport.TestReportParticipant",
)

TestReportSetupType = create_fhir_type(
    "TestReportSetupType", "tests.fixtures.resources.testreport.TestReportSetup"
)

TestReportSetupActionType = create_fhir_type(
    "TestReportSetupActionType",
    "tests.fixtures.resources.testreport.TestReportSetupAction",
)

TestReportSetupActionAssertType = create_fhir_type(
    "TestReportSetupActionAssertType",
    "tests.fixtures.resources.testreport.TestReportSetupActionAssert",
)

TestReportSetupActionAssertRequirementType = create_fhir_type(
    "TestReportSetupActionAssertRequirementType",
    "tests.fixtures.resources.testreport.TestReportSetupActionAssertRequirement",
)

TestReportSetupActionOperationType = create_fhir_type(
    "TestReportSetupActionOperationType",
    "tests.fixtures.resources.testreport.TestReportSetupActionOperation",
)

TestReportTeardownType = create_fhir_type(
    "TestReportTeardownType", "tests.fixtures.resources.testreport.TestReportTeardown"
)

TestReportTeardownActionType = create_fhir_type(
    "TestReportTeardownActionType",
    "tests.fixtures.resources.testreport.TestReportTeardownAction",
)

TestReportTestType = create_fhir_type(
    "TestReportTestType", "tests.fixtures.resources.testreport.TestReportTest"
)

TestReportTestActionType = create_fhir_type(
    "TestReportTestActionType",
    "tests.fixtures.resources.testreport.TestReportTestAction",
)

TestScriptType = create_fhir_type(
    "TestScriptType", "tests.fixtures.resources.testscript.TestScript"
)

TestScriptDestinationType = create_fhir_type(
    "TestScriptDestinationType",
    "tests.fixtures.resources.testscript.TestScriptDestination",
)

TestScriptFixtureType = create_fhir_type(
    "TestScriptFixtureType", "tests.fixtures.resources.testscript.TestScriptFixture"
)

TestScriptMetadataType = create_fhir_type(
    "TestScriptMetadataType", "tests.fixtures.resources.testscript.TestScriptMetadata"
)

TestScriptMetadataCapabilityType = create_fhir_type(
    "TestScriptMetadataCapabilityType",
    "tests.fixtures.resources.testscript.TestScriptMetadataCapability",
)

TestScriptMetadataLinkType = create_fhir_type(
    "TestScriptMetadataLinkType",
    "tests.fixtures.resources.testscript.TestScriptMetadataLink",
)

TestScriptOriginType = create_fhir_type(
    "TestScriptOriginType", "tests.fixtures.resources.testscript.TestScriptOrigin"
)

TestScriptScopeType = create_fhir_type(
    "TestScriptScopeType", "tests.fixtures.resources.testscript.TestScriptScope"
)

TestScriptSetupType = create_fhir_type(
    "TestScriptSetupType", "tests.fixtures.resources.testscript.TestScriptSetup"
)

TestScriptSetupActionType = create_fhir_type(
    "TestScriptSetupActionType",
    "tests.fixtures.resources.testscript.TestScriptSetupAction",
)

TestScriptSetupActionAssertType = create_fhir_type(
    "TestScriptSetupActionAssertType",
    "tests.fixtures.resources.testscript.TestScriptSetupActionAssert",
)

TestScriptSetupActionAssertRequirementType = create_fhir_type(
    "TestScriptSetupActionAssertRequirementType",
    "tests.fixtures.resources.testscript.TestScriptSetupActionAssertRequirement",
)

TestScriptSetupActionOperationType = create_fhir_type(
    "TestScriptSetupActionOperationType",
    "tests.fixtures.resources.testscript.TestScriptSetupActionOperation",
)

TestScriptSetupActionOperationRequestHeaderType = create_fhir_type(
    "TestScriptSetupActionOperationRequestHeaderType",
    "tests.fixtures.resources.testscript.TestScriptSetupActionOperationRequestHeader",
)

TestScriptTeardownType = create_fhir_type(
    "TestScriptTeardownType", "tests.fixtures.resources.testscript.TestScriptTeardown"
)

TestScriptTeardownActionType = create_fhir_type(
    "TestScriptTeardownActionType",
    "tests.fixtures.resources.testscript.TestScriptTeardownAction",
)

TestScriptTestType = create_fhir_type(
    "TestScriptTestType", "tests.fixtures.resources.testscript.TestScriptTest"
)

TestScriptTestActionType = create_fhir_type(
    "TestScriptTestActionType",
    "tests.fixtures.resources.testscript.TestScriptTestAction",
)

TestScriptVariableType = create_fhir_type(
    "TestScriptVariableType", "tests.fixtures.resources.testscript.TestScriptVariable"
)

TimingType = create_fhir_type("TimingType", "tests.fixtures.resources.timing.Timing")

TimingRepeatType = create_fhir_type(
    "TimingRepeatType", "tests.fixtures.resources.timing.TimingRepeat"
)

TransportType = create_fhir_type(
    "TransportType", "tests.fixtures.resources.transport.Transport"
)

TransportInputType = create_fhir_type(
    "TransportInputType", "tests.fixtures.resources.transport.TransportInput"
)

TransportOutputType = create_fhir_type(
    "TransportOutputType", "tests.fixtures.resources.transport.TransportOutput"
)

TransportRestrictionType = create_fhir_type(
    "TransportRestrictionType",
    "tests.fixtures.resources.transport.TransportRestriction",
)

TriggerDefinitionType = create_fhir_type(
    "TriggerDefinitionType",
    "tests.fixtures.resources.triggerdefinition.TriggerDefinition",
)

UsageContextType = create_fhir_type(
    "UsageContextType", "tests.fixtures.resources.usagecontext.UsageContext"
)

ValueSetType = create_fhir_type(
    "ValueSetType", "tests.fixtures.resources.valueset.ValueSet"
)

ValueSetComposeType = create_fhir_type(
    "ValueSetComposeType", "tests.fixtures.resources.valueset.ValueSetCompose"
)

ValueSetComposeIncludeType = create_fhir_type(
    "ValueSetComposeIncludeType",
    "tests.fixtures.resources.valueset.ValueSetComposeInclude",
)

ValueSetComposeIncludeConceptType = create_fhir_type(
    "ValueSetComposeIncludeConceptType",
    "tests.fixtures.resources.valueset.ValueSetComposeIncludeConcept",
)

ValueSetComposeIncludeConceptDesignationType = create_fhir_type(
    "ValueSetComposeIncludeConceptDesignationType",
    "tests.fixtures.resources.valueset.ValueSetComposeIncludeConceptDesignation",
)

ValueSetComposeIncludeFilterType = create_fhir_type(
    "ValueSetComposeIncludeFilterType",
    "tests.fixtures.resources.valueset.ValueSetComposeIncludeFilter",
)

ValueSetExpansionType = create_fhir_type(
    "ValueSetExpansionType", "tests.fixtures.resources.valueset.ValueSetExpansion"
)

ValueSetExpansionContainsType = create_fhir_type(
    "ValueSetExpansionContainsType",
    "tests.fixtures.resources.valueset.ValueSetExpansionContains",
)

ValueSetExpansionContainsPropertyType = create_fhir_type(
    "ValueSetExpansionContainsPropertyType",
    "tests.fixtures.resources.valueset.ValueSetExpansionContainsProperty",
)

ValueSetExpansionContainsPropertySubPropertyType = create_fhir_type(
    "ValueSetExpansionContainsPropertySubPropertyType",
    "tests.fixtures.resources.valueset.ValueSetExpansionContainsPropertySubProperty",
)

ValueSetExpansionParameterType = create_fhir_type(
    "ValueSetExpansionParameterType",
    "tests.fixtures.resources.valueset.ValueSetExpansionParameter",
)

ValueSetExpansionPropertyType = create_fhir_type(
    "ValueSetExpansionPropertyType",
    "tests.fixtures.resources.valueset.ValueSetExpansionProperty",
)

ValueSetScopeType = create_fhir_type(
    "ValueSetScopeType", "tests.fixtures.resources.valueset.ValueSetScope"
)

VerificationResultType = create_fhir_type(
    "VerificationResultType",
    "tests.fixtures.resources.verificationresult.VerificationResult",
)

VerificationResultAttestationType = create_fhir_type(
    "VerificationResultAttestationType",
    "tests.fixtures.resources.verificationresult.VerificationResultAttestation",
)

VerificationResultPrimarySourceType = create_fhir_type(
    "VerificationResultPrimarySourceType",
    "tests.fixtures.resources.verificationresult.VerificationResultPrimarySource",
)

VerificationResultValidatorType = create_fhir_type(
    "VerificationResultValidatorType",
    "tests.fixtures.resources.verificationresult.VerificationResultValidator",
)

VirtualServiceDetailType = create_fhir_type(
    "VirtualServiceDetailType",
    "tests.fixtures.resources.virtualservicedetail.VirtualServiceDetail",
)

VisionPrescriptionType = create_fhir_type(
    "VisionPrescriptionType",
    "tests.fixtures.resources.visionprescription.VisionPrescription",
)

VisionPrescriptionLensSpecificationType = create_fhir_type(
    "VisionPrescriptionLensSpecificationType",
    "tests.fixtures.resources.visionprescription.VisionPrescriptionLensSpecification",
)

VisionPrescriptionLensSpecificationPrismType = create_fhir_type(
    "VisionPrescriptionLensSpecificationPrismType",
    "tests.fixtures.resources.visionprescription.VisionPrescriptionLensSpecificationPrism",
)

__all__ = [
    "BooleanType",
    "StringType",
    "Base64BinaryType",
    "CodeType",
    "IdType",
    "IntegerType",
    "Integer64Type",
    "DecimalType",
    "UnsignedIntType",
    "PositiveIntType",
    "CanonicalType",
    "UriType",
    "OidType",
    "UuidType",
    "UrlType",
    "MarkdownType",
    "XhtmlType",
    "DateType",
    "DateTimeType",
    "InstantType",
    "TimeType",
    "FHIRPrimitiveExtensionType",
    "AccountType",
    "AccountBalanceType",
    "AccountCoverageType",
    "AccountDiagnosisType",
    "AccountGuarantorType",
    "AccountProcedureType",
    "AccountRelatedAccountType",
    "ActivityDefinitionType",
    "ActivityDefinitionDynamicValueType",
    "ActivityDefinitionParticipantType",
    "ActorDefinitionType",
    "AddressType",
    "AdministrableProductDefinitionType",
    "AdministrableProductDefinitionPropertyType",
    "AdministrableProductDefinitionRouteOfAdministrationType",
    "AdministrableProductDefinitionRouteOfAdministrationTargetSpeciesType",
    "AdministrableProductDefinitionRouteOfAdministrationTargetSpeciesWithdrawalPeriodType",
    "AdverseEventType",
    "AdverseEventContributingFactorType",
    "AdverseEventMitigatingActionType",
    "AdverseEventParticipantType",
    "AdverseEventPreventiveActionType",
    "AdverseEventSupportingInfoType",
    "AdverseEventSuspectEntityType",
    "AdverseEventSuspectEntityCausalityType",
    "AgeType",
    "AllergyIntoleranceType",
    "AllergyIntoleranceParticipantType",
    "AllergyIntoleranceReactionType",
    "AnnotationType",
    "AppointmentType",
    "AppointmentParticipantType",
    "AppointmentRecurrenceTemplateType",
    "AppointmentRecurrenceTemplateMonthlyTemplateType",
    "AppointmentRecurrenceTemplateWeeklyTemplateType",
    "AppointmentRecurrenceTemplateYearlyTemplateType",
    "AppointmentResponseType",
    "ArtifactAssessmentType",
    "ArtifactAssessmentContentType",
    "AttachmentType",
    "AuditEventType",
    "AuditEventAgentType",
    "AuditEventEntityType",
    "AuditEventEntityDetailType",
    "AuditEventOutcomeType",
    "AuditEventSourceType",
    "AvailabilityType",
    "AvailabilityAvailableTimeType",
    "AvailabilityNotAvailableTimeType",
    "BackboneElementType",
    "BackboneTypeType",
    "BaseType",
    "BasicType",
    "BinaryType",
    "BiologicallyDerivedProductType",
    "BiologicallyDerivedProductCollectionType",
    "BiologicallyDerivedProductDispenseType",
    "BiologicallyDerivedProductDispensePerformerType",
    "BiologicallyDerivedProductPropertyType",
    "BodyStructureType",
    "BodyStructureIncludedStructureType",
    "BodyStructureIncludedStructureBodyLandmarkOrientationType",
    "BodyStructureIncludedStructureBodyLandmarkOrientationDistanceFromLandmarkType",
    "BundleType",
    "BundleEntryType",
    "BundleEntryRequestType",
    "BundleEntryResponseType",
    "BundleEntrySearchType",
    "BundleLinkType",
    "CanonicalResourceType",
    "CapabilityStatementType",
    "CapabilityStatementDocumentType",
    "CapabilityStatementImplementationType",
    "CapabilityStatementMessagingType",
    "CapabilityStatementMessagingEndpointType",
    "CapabilityStatementMessagingSupportedMessageType",
    "CapabilityStatementRestType",
    "CapabilityStatementRestInteractionType",
    "CapabilityStatementRestResourceType",
    "CapabilityStatementRestResourceInteractionType",
    "CapabilityStatementRestResourceOperationType",
    "CapabilityStatementRestResourceSearchParamType",
    "CapabilityStatementRestSecurityType",
    "CapabilityStatementSoftwareType",
    "CarePlanType",
    "CarePlanActivityType",
    "CareTeamType",
    "CareTeamParticipantType",
    "ChargeItemType",
    "ChargeItemDefinitionType",
    "ChargeItemDefinitionApplicabilityType",
    "ChargeItemDefinitionPropertyGroupType",
    "ChargeItemPerformerType",
    "CitationType",
    "CitationCitedArtifactType",
    "CitationCitedArtifactAbstractType",
    "CitationCitedArtifactClassificationType",
    "CitationCitedArtifactContributorshipType",
    "CitationCitedArtifactContributorshipEntryType",
    "CitationCitedArtifactContributorshipEntryContributionInstanceType",
    "CitationCitedArtifactContributorshipSummaryType",
    "CitationCitedArtifactPartType",
    "CitationCitedArtifactPublicationFormType",
    "CitationCitedArtifactPublicationFormPublishedInType",
    "CitationCitedArtifactRelatesToType",
    "CitationCitedArtifactStatusDateType",
    "CitationCitedArtifactTitleType",
    "CitationCitedArtifactVersionType",
    "CitationCitedArtifactWebLocationType",
    "CitationClassificationType",
    "CitationStatusDateType",
    "CitationSummaryType",
    "ClaimType",
    "ClaimAccidentType",
    "ClaimCareTeamType",
    "ClaimDiagnosisType",
    "ClaimEventType",
    "ClaimInsuranceType",
    "ClaimItemType",
    "ClaimItemBodySiteType",
    "ClaimItemDetailType",
    "ClaimItemDetailSubDetailType",
    "ClaimPayeeType",
    "ClaimProcedureType",
    "ClaimRelatedType",
    "ClaimResponseType",
    "ClaimResponseAddItemType",
    "ClaimResponseAddItemBodySiteType",
    "ClaimResponseAddItemDetailType",
    "ClaimResponseAddItemDetailSubDetailType",
    "ClaimResponseErrorType",
    "ClaimResponseEventType",
    "ClaimResponseInsuranceType",
    "ClaimResponseItemType",
    "ClaimResponseItemAdjudicationType",
    "ClaimResponseItemDetailType",
    "ClaimResponseItemDetailSubDetailType",
    "ClaimResponseItemReviewOutcomeType",
    "ClaimResponsePaymentType",
    "ClaimResponseProcessNoteType",
    "ClaimResponseTotalType",
    "ClaimSupportingInfoType",
    "ClinicalImpressionType",
    "ClinicalImpressionFindingType",
    "ClinicalUseDefinitionType",
    "ClinicalUseDefinitionContraindicationType",
    "ClinicalUseDefinitionContraindicationOtherTherapyType",
    "ClinicalUseDefinitionIndicationType",
    "ClinicalUseDefinitionInteractionType",
    "ClinicalUseDefinitionInteractionInteractantType",
    "ClinicalUseDefinitionUndesirableEffectType",
    "ClinicalUseDefinitionWarningType",
    "CodeSystemType",
    "CodeSystemConceptType",
    "CodeSystemConceptDesignationType",
    "CodeSystemConceptPropertyType",
    "CodeSystemFilterType",
    "CodeSystemPropertyType",
    "CodeableConceptType",
    "CodeableReferenceType",
    "CodingType",
    "CommunicationType",
    "CommunicationPayloadType",
    "CommunicationRequestType",
    "CommunicationRequestPayloadType",
    "CompartmentDefinitionType",
    "CompartmentDefinitionResourceType",
    "CompositionType",
    "CompositionAttesterType",
    "CompositionEventType",
    "CompositionSectionType",
    "ConceptMapType",
    "ConceptMapAdditionalAttributeType",
    "ConceptMapGroupType",
    "ConceptMapGroupElementType",
    "ConceptMapGroupElementTargetType",
    "ConceptMapGroupElementTargetDependsOnType",
    "ConceptMapGroupElementTargetPropertyType",
    "ConceptMapGroupUnmappedType",
    "ConceptMapPropertyType",
    "ConditionType",
    "ConditionDefinitionType",
    "ConditionDefinitionMedicationType",
    "ConditionDefinitionObservationType",
    "ConditionDefinitionPlanType",
    "ConditionDefinitionPreconditionType",
    "ConditionDefinitionQuestionnaireType",
    "ConditionParticipantType",
    "ConditionStageType",
    "ConsentType",
    "ConsentPolicyBasisType",
    "ConsentProvisionType",
    "ConsentProvisionActorType",
    "ConsentProvisionDataType",
    "ConsentVerificationType",
    "ContactDetailType",
    "ContactPointType",
    "ContractType",
    "ContractContentDefinitionType",
    "ContractFriendlyType",
    "ContractLegalType",
    "ContractRuleType",
    "ContractSignerType",
    "ContractTermType",
    "ContractTermActionType",
    "ContractTermActionSubjectType",
    "ContractTermAssetType",
    "ContractTermAssetContextType",
    "ContractTermAssetValuedItemType",
    "ContractTermOfferType",
    "ContractTermOfferAnswerType",
    "ContractTermOfferPartyType",
    "ContractTermSecurityLabelType",
    "ContributorType",
    "CountType",
    "CoverageType",
    "CoverageClassType",
    "CoverageCostToBeneficiaryType",
    "CoverageCostToBeneficiaryExceptionType",
    "CoverageEligibilityRequestType",
    "CoverageEligibilityRequestEventType",
    "CoverageEligibilityRequestInsuranceType",
    "CoverageEligibilityRequestItemType",
    "CoverageEligibilityRequestItemDiagnosisType",
    "CoverageEligibilityRequestSupportingInfoType",
    "CoverageEligibilityResponseType",
    "CoverageEligibilityResponseErrorType",
    "CoverageEligibilityResponseEventType",
    "CoverageEligibilityResponseInsuranceType",
    "CoverageEligibilityResponseInsuranceItemType",
    "CoverageEligibilityResponseInsuranceItemBenefitType",
    "CoveragePaymentByType",
    "DataRequirementType",
    "DataRequirementCodeFilterType",
    "DataRequirementDateFilterType",
    "DataRequirementSortType",
    "DataRequirementValueFilterType",
    "DataTypeType",
    "DetectedIssueType",
    "DetectedIssueEvidenceType",
    "DetectedIssueMitigationType",
    "DeviceType",
    "DeviceAssociationType",
    "DeviceAssociationOperationType",
    "DeviceConformsToType",
    "DeviceDefinitionType",
    "DeviceDefinitionChargeItemType",
    "DeviceDefinitionClassificationType",
    "DeviceDefinitionConformsToType",
    "DeviceDefinitionCorrectiveActionType",
    "DeviceDefinitionDeviceNameType",
    "DeviceDefinitionGuidelineType",
    "DeviceDefinitionHasPartType",
    "DeviceDefinitionLinkType",
    "DeviceDefinitionMaterialType",
    "DeviceDefinitionPackagingType",
    "DeviceDefinitionPackagingDistributorType",
    "DeviceDefinitionPropertyType",
    "DeviceDefinitionRegulatoryIdentifierType",
    "DeviceDefinitionUdiDeviceIdentifierType",
    "DeviceDefinitionUdiDeviceIdentifierMarketDistributionType",
    "DeviceDefinitionVersionType",
    "DeviceDispenseType",
    "DeviceDispensePerformerType",
    "DeviceMetricType",
    "DeviceMetricCalibrationType",
    "DeviceNameType",
    "DevicePropertyType",
    "DeviceRequestType",
    "DeviceRequestParameterType",
    "DeviceUdiCarrierType",
    "DeviceUsageType",
    "DeviceUsageAdherenceType",
    "DeviceVersionType",
    "DiagnosticReportType",
    "DiagnosticReportMediaType",
    "DiagnosticReportSupportingInfoType",
    "DistanceType",
    "DocumentReferenceType",
    "DocumentReferenceAttesterType",
    "DocumentReferenceContentType",
    "DocumentReferenceContentProfileType",
    "DocumentReferenceRelatesToType",
    "DomainResourceType",
    "DosageType",
    "DosageDoseAndRateType",
    "DurationType",
    "ElementType",
    "ElementDefinitionType",
    "ElementDefinitionBaseType",
    "ElementDefinitionBindingType",
    "ElementDefinitionBindingAdditionalType",
    "ElementDefinitionConstraintType",
    "ElementDefinitionExampleType",
    "ElementDefinitionMappingType",
    "ElementDefinitionSlicingType",
    "ElementDefinitionSlicingDiscriminatorType",
    "ElementDefinitionTypeType",
    "EncounterType",
    "EncounterAdmissionType",
    "EncounterDiagnosisType",
    "EncounterHistoryType",
    "EncounterHistoryLocationType",
    "EncounterLocationType",
    "EncounterParticipantType",
    "EncounterReasonType",
    "EndpointType",
    "EndpointPayloadType",
    "EnrollmentRequestType",
    "EnrollmentResponseType",
    "EpisodeOfCareType",
    "EpisodeOfCareDiagnosisType",
    "EpisodeOfCareReasonType",
    "EpisodeOfCareStatusHistoryType",
    "EventDefinitionType",
    "EvidenceType",
    "EvidenceCertaintyType",
    "EvidenceReportType",
    "EvidenceReportRelatesToType",
    "EvidenceReportRelatesToTargetType",
    "EvidenceReportSectionType",
    "EvidenceReportSubjectType",
    "EvidenceReportSubjectCharacteristicType",
    "EvidenceStatisticType",
    "EvidenceStatisticAttributeEstimateType",
    "EvidenceStatisticModelCharacteristicType",
    "EvidenceStatisticModelCharacteristicVariableType",
    "EvidenceStatisticSampleSizeType",
    "EvidenceVariableType",
    "EvidenceVariableCategoryType",
    "EvidenceVariableCharacteristicType",
    "EvidenceVariableCharacteristicDefinitionByCombinationType",
    "EvidenceVariableCharacteristicDefinitionByTypeAndValueType",
    "EvidenceVariableCharacteristicTimeFromEventType",
    "EvidenceVariableDefinitionType",
    "ExampleScenarioType",
    "ExampleScenarioActorType",
    "ExampleScenarioInstanceType",
    "ExampleScenarioInstanceContainedInstanceType",
    "ExampleScenarioInstanceVersionType",
    "ExampleScenarioProcessType",
    "ExampleScenarioProcessStepType",
    "ExampleScenarioProcessStepAlternativeType",
    "ExampleScenarioProcessStepOperationType",
    "ExplanationOfBenefitType",
    "ExplanationOfBenefitAccidentType",
    "ExplanationOfBenefitAddItemType",
    "ExplanationOfBenefitAddItemBodySiteType",
    "ExplanationOfBenefitAddItemDetailType",
    "ExplanationOfBenefitAddItemDetailSubDetailType",
    "ExplanationOfBenefitBenefitBalanceType",
    "ExplanationOfBenefitBenefitBalanceFinancialType",
    "ExplanationOfBenefitCareTeamType",
    "ExplanationOfBenefitDiagnosisType",
    "ExplanationOfBenefitEventType",
    "ExplanationOfBenefitInsuranceType",
    "ExplanationOfBenefitItemType",
    "ExplanationOfBenefitItemAdjudicationType",
    "ExplanationOfBenefitItemBodySiteType",
    "ExplanationOfBenefitItemDetailType",
    "ExplanationOfBenefitItemDetailSubDetailType",
    "ExplanationOfBenefitItemReviewOutcomeType",
    "ExplanationOfBenefitPayeeType",
    "ExplanationOfBenefitPaymentType",
    "ExplanationOfBenefitProcedureType",
    "ExplanationOfBenefitProcessNoteType",
    "ExplanationOfBenefitRelatedType",
    "ExplanationOfBenefitSupportingInfoType",
    "ExplanationOfBenefitTotalType",
    "ExpressionType",
    "ExtendedContactDetailType",
    "ExtensionType",
    "FamilyMemberHistoryType",
    "FamilyMemberHistoryConditionType",
    "FamilyMemberHistoryParticipantType",
    "FamilyMemberHistoryProcedureType",
    "FlagType",
    "FormularyItemType",
    "GenomicStudyType",
    "GenomicStudyAnalysisType",
    "GenomicStudyAnalysisDeviceType",
    "GenomicStudyAnalysisInputType",
    "GenomicStudyAnalysisOutputType",
    "GenomicStudyAnalysisPerformerType",
    "GoalType",
    "GoalTargetType",
    "GraphDefinitionType",
    "GraphDefinitionLinkType",
    "GraphDefinitionLinkCompartmentType",
    "GraphDefinitionNodeType",
    "GroupType",
    "GroupCharacteristicType",
    "GroupMemberType",
    "GuidanceResponseType",
    "HealthcareServiceType",
    "HealthcareServiceEligibilityType",
    "HumanNameType",
    "IdentifierType",
    "ImagingSelectionType",
    "ImagingSelectionInstanceType",
    "ImagingSelectionInstanceImageRegion2DType",
    "ImagingSelectionInstanceImageRegion3DType",
    "ImagingSelectionPerformerType",
    "ImagingStudyType",
    "ImagingStudySeriesType",
    "ImagingStudySeriesInstanceType",
    "ImagingStudySeriesPerformerType",
    "ImmunizationType",
    "ImmunizationEvaluationType",
    "ImmunizationPerformerType",
    "ImmunizationProgramEligibilityType",
    "ImmunizationProtocolAppliedType",
    "ImmunizationReactionType",
    "ImmunizationRecommendationType",
    "ImmunizationRecommendationRecommendationType",
    "ImmunizationRecommendationRecommendationDateCriterionType",
    "ImplementationGuideType",
    "ImplementationGuideDefinitionType",
    "ImplementationGuideDefinitionGroupingType",
    "ImplementationGuideDefinitionPageType",
    "ImplementationGuideDefinitionParameterType",
    "ImplementationGuideDefinitionResourceType",
    "ImplementationGuideDefinitionTemplateType",
    "ImplementationGuideDependsOnType",
    "ImplementationGuideGlobalType",
    "ImplementationGuideManifestType",
    "ImplementationGuideManifestPageType",
    "ImplementationGuideManifestResourceType",
    "IngredientType",
    "IngredientManufacturerType",
    "IngredientSubstanceType",
    "IngredientSubstanceStrengthType",
    "IngredientSubstanceStrengthReferenceStrengthType",
    "InsurancePlanType",
    "InsurancePlanCoverageType",
    "InsurancePlanCoverageBenefitType",
    "InsurancePlanCoverageBenefitLimitType",
    "InsurancePlanPlanType",
    "InsurancePlanPlanGeneralCostType",
    "InsurancePlanPlanSpecificCostType",
    "InsurancePlanPlanSpecificCostBenefitType",
    "InsurancePlanPlanSpecificCostBenefitCostType",
    "InventoryItemType",
    "InventoryItemAssociationType",
    "InventoryItemCharacteristicType",
    "InventoryItemDescriptionType",
    "InventoryItemInstanceType",
    "InventoryItemNameType",
    "InventoryItemResponsibleOrganizationType",
    "InventoryReportType",
    "InventoryReportInventoryListingType",
    "InventoryReportInventoryListingItemType",
    "InvoiceType",
    "InvoiceLineItemType",
    "InvoiceParticipantType",
    "LibraryType",
    "LinkageType",
    "LinkageItemType",
    "ListType",
    "ListEntryType",
    "LocationType",
    "LocationPositionType",
    "ManufacturedItemDefinitionType",
    "ManufacturedItemDefinitionComponentType",
    "ManufacturedItemDefinitionComponentConstituentType",
    "ManufacturedItemDefinitionPropertyType",
    "MarketingStatusType",
    "MeasureType",
    "MeasureGroupType",
    "MeasureGroupPopulationType",
    "MeasureGroupStratifierType",
    "MeasureGroupStratifierComponentType",
    "MeasureReportType",
    "MeasureReportGroupType",
    "MeasureReportGroupPopulationType",
    "MeasureReportGroupStratifierType",
    "MeasureReportGroupStratifierStratumType",
    "MeasureReportGroupStratifierStratumComponentType",
    "MeasureReportGroupStratifierStratumPopulationType",
    "MeasureSupplementalDataType",
    "MeasureTermType",
    "MedicationType",
    "MedicationAdministrationType",
    "MedicationAdministrationDosageType",
    "MedicationAdministrationPerformerType",
    "MedicationBatchType",
    "MedicationDispenseType",
    "MedicationDispensePerformerType",
    "MedicationDispenseSubstitutionType",
    "MedicationIngredientType",
    "MedicationKnowledgeType",
    "MedicationKnowledgeCostType",
    "MedicationKnowledgeDefinitionalType",
    "MedicationKnowledgeDefinitionalDrugCharacteristicType",
    "MedicationKnowledgeDefinitionalIngredientType",
    "MedicationKnowledgeIndicationGuidelineType",
    "MedicationKnowledgeIndicationGuidelineDosingGuidelineType",
    "MedicationKnowledgeIndicationGuidelineDosingGuidelineDosageType",
    "MedicationKnowledgeIndicationGuidelineDosingGuidelinePatientCharacteristicType",
    "MedicationKnowledgeMedicineClassificationType",
    "MedicationKnowledgeMonitoringProgramType",
    "MedicationKnowledgeMonographType",
    "MedicationKnowledgePackagingType",
    "MedicationKnowledgeRegulatoryType",
    "MedicationKnowledgeRegulatoryMaxDispenseType",
    "MedicationKnowledgeRegulatorySubstitutionType",
    "MedicationKnowledgeRelatedMedicationKnowledgeType",
    "MedicationKnowledgeStorageGuidelineType",
    "MedicationKnowledgeStorageGuidelineEnvironmentalSettingType",
    "MedicationRequestType",
    "MedicationRequestDispenseRequestType",
    "MedicationRequestDispenseRequestInitialFillType",
    "MedicationRequestSubstitutionType",
    "MedicationStatementType",
    "MedicationStatementAdherenceType",
    "MedicinalProductDefinitionType",
    "MedicinalProductDefinitionCharacteristicType",
    "MedicinalProductDefinitionContactType",
    "MedicinalProductDefinitionCrossReferenceType",
    "MedicinalProductDefinitionNameType",
    "MedicinalProductDefinitionNamePartType",
    "MedicinalProductDefinitionNameUsageType",
    "MedicinalProductDefinitionOperationType",
    "MessageDefinitionType",
    "MessageDefinitionAllowedResponseType",
    "MessageDefinitionFocusType",
    "MessageHeaderType",
    "MessageHeaderDestinationType",
    "MessageHeaderResponseType",
    "MessageHeaderSourceType",
    "MetaType",
    "MetadataResourceType",
    "MolecularSequenceType",
    "MolecularSequenceRelativeType",
    "MolecularSequenceRelativeEditType",
    "MolecularSequenceRelativeStartingSequenceType",
    "MonetaryComponentType",
    "MoneyType",
    "NamingSystemType",
    "NamingSystemUniqueIdType",
    "NarrativeType",
    "NutritionIntakeType",
    "NutritionIntakeConsumedItemType",
    "NutritionIntakeIngredientLabelType",
    "NutritionIntakePerformerType",
    "NutritionOrderType",
    "NutritionOrderEnteralFormulaType",
    "NutritionOrderEnteralFormulaAdditiveType",
    "NutritionOrderEnteralFormulaAdministrationType",
    "NutritionOrderEnteralFormulaAdministrationScheduleType",
    "NutritionOrderOralDietType",
    "NutritionOrderOralDietNutrientType",
    "NutritionOrderOralDietScheduleType",
    "NutritionOrderOralDietTextureType",
    "NutritionOrderSupplementType",
    "NutritionOrderSupplementScheduleType",
    "NutritionProductType",
    "NutritionProductCharacteristicType",
    "NutritionProductIngredientType",
    "NutritionProductInstanceType",
    "NutritionProductNutrientType",
    "ObservationType",
    "ObservationComponentType",
    "ObservationDefinitionType",
    "ObservationDefinitionComponentType",
    "ObservationDefinitionQualifiedValueType",
    "ObservationReferenceRangeType",
    "ObservationTriggeredByType",
    "OperationDefinitionType",
    "OperationDefinitionOverloadType",
    "OperationDefinitionParameterType",
    "OperationDefinitionParameterBindingType",
    "OperationDefinitionParameterReferencedFromType",
    "OperationOutcomeType",
    "OperationOutcomeIssueType",
    "OrganizationType",
    "OrganizationAffiliationType",
    "OrganizationQualificationType",
    "PackagedProductDefinitionType",
    "PackagedProductDefinitionLegalStatusOfSupplyType",
    "PackagedProductDefinitionPackagingType",
    "PackagedProductDefinitionPackagingContainedItemType",
    "PackagedProductDefinitionPackagingPropertyType",
    "ParameterDefinitionType",
    "ParametersType",
    "ParametersParameterType",
    "PatientType",
    "PatientCommunicationType",
    "PatientContactType",
    "PatientLinkType",
    "PaymentNoticeType",
    "PaymentReconciliationType",
    "PaymentReconciliationAllocationType",
    "PaymentReconciliationProcessNoteType",
    "PeriodType",
    "PermissionType",
    "PermissionJustificationType",
    "PermissionRuleType",
    "PermissionRuleActivityType",
    "PermissionRuleDataType",
    "PermissionRuleDataResourceType",
    "PersonType",
    "PersonCommunicationType",
    "PersonLinkType",
    "PlanDefinitionType",
    "PlanDefinitionActionType",
    "PlanDefinitionActionConditionType",
    "PlanDefinitionActionDynamicValueType",
    "PlanDefinitionActionInputType",
    "PlanDefinitionActionOutputType",
    "PlanDefinitionActionParticipantType",
    "PlanDefinitionActionRelatedActionType",
    "PlanDefinitionActorType",
    "PlanDefinitionActorOptionType",
    "PlanDefinitionGoalType",
    "PlanDefinitionGoalTargetType",
    "PractitionerType",
    "PractitionerCommunicationType",
    "PractitionerQualificationType",
    "PractitionerRoleType",
    "PrimitiveTypeType",
    "ProcedureType",
    "ProcedureFocalDeviceType",
    "ProcedurePerformerType",
    "ProductShelfLifeType",
    "ProvenanceType",
    "ProvenanceAgentType",
    "ProvenanceEntityType",
    "QuantityType",
    "QuestionnaireType",
    "QuestionnaireItemType",
    "QuestionnaireItemAnswerOptionType",
    "QuestionnaireItemEnableWhenType",
    "QuestionnaireItemInitialType",
    "QuestionnaireResponseType",
    "QuestionnaireResponseItemType",
    "QuestionnaireResponseItemAnswerType",
    "RangeType",
    "RatioType",
    "RatioRangeType",
    "ReferenceType",
    "RegulatedAuthorizationType",
    "RegulatedAuthorizationCaseType",
    "RelatedArtifactType",
    "RelatedPersonType",
    "RelatedPersonCommunicationType",
    "RequestOrchestrationType",
    "RequestOrchestrationActionType",
    "RequestOrchestrationActionConditionType",
    "RequestOrchestrationActionDynamicValueType",
    "RequestOrchestrationActionInputType",
    "RequestOrchestrationActionOutputType",
    "RequestOrchestrationActionParticipantType",
    "RequestOrchestrationActionRelatedActionType",
    "RequirementsType",
    "RequirementsStatementType",
    "ResearchStudyType",
    "ResearchStudyAssociatedPartyType",
    "ResearchStudyComparisonGroupType",
    "ResearchStudyLabelType",
    "ResearchStudyObjectiveType",
    "ResearchStudyOutcomeMeasureType",
    "ResearchStudyProgressStatusType",
    "ResearchStudyRecruitmentType",
    "ResearchSubjectType",
    "ResearchSubjectProgressType",
    "ResourceType",
    "RiskAssessmentType",
    "RiskAssessmentPredictionType",
    "SampledDataType",
    "ScheduleType",
    "SearchParameterType",
    "SearchParameterComponentType",
    "ServiceRequestType",
    "ServiceRequestOrderDetailType",
    "ServiceRequestOrderDetailParameterType",
    "ServiceRequestPatientInstructionType",
    "SignatureType",
    "SlotType",
    "SpecimenType",
    "SpecimenCollectionType",
    "SpecimenContainerType",
    "SpecimenDefinitionType",
    "SpecimenDefinitionTypeTestedType",
    "SpecimenDefinitionTypeTestedContainerType",
    "SpecimenDefinitionTypeTestedContainerAdditiveType",
    "SpecimenDefinitionTypeTestedHandlingType",
    "SpecimenFeatureType",
    "SpecimenProcessingType",
    "StructureDefinitionType",
    "StructureDefinitionContextType",
    "StructureDefinitionDifferentialType",
    "StructureDefinitionMappingType",
    "StructureDefinitionSnapshotType",
    "StructureMapType",
    "StructureMapConstType",
    "StructureMapGroupType",
    "StructureMapGroupInputType",
    "StructureMapGroupRuleType",
    "StructureMapGroupRuleDependentType",
    "StructureMapGroupRuleSourceType",
    "StructureMapGroupRuleTargetType",
    "StructureMapGroupRuleTargetParameterType",
    "StructureMapStructureType",
    "SubscriptionType",
    "SubscriptionFilterByType",
    "SubscriptionParameterType",
    "SubscriptionStatusType",
    "SubscriptionStatusNotificationEventType",
    "SubscriptionTopicType",
    "SubscriptionTopicCanFilterByType",
    "SubscriptionTopicEventTriggerType",
    "SubscriptionTopicNotificationShapeType",
    "SubscriptionTopicResourceTriggerType",
    "SubscriptionTopicResourceTriggerQueryCriteriaType",
    "SubstanceType",
    "SubstanceDefinitionType",
    "SubstanceDefinitionCharacterizationType",
    "SubstanceDefinitionCodeType",
    "SubstanceDefinitionMoietyType",
    "SubstanceDefinitionMolecularWeightType",
    "SubstanceDefinitionNameType",
    "SubstanceDefinitionNameOfficialType",
    "SubstanceDefinitionPropertyType",
    "SubstanceDefinitionRelationshipType",
    "SubstanceDefinitionSourceMaterialType",
    "SubstanceDefinitionStructureType",
    "SubstanceDefinitionStructureRepresentationType",
    "SubstanceIngredientType",
    "SubstanceNucleicAcidType",
    "SubstanceNucleicAcidSubunitType",
    "SubstanceNucleicAcidSubunitLinkageType",
    "SubstanceNucleicAcidSubunitSugarType",
    "SubstancePolymerType",
    "SubstancePolymerMonomerSetType",
    "SubstancePolymerMonomerSetStartingMaterialType",
    "SubstancePolymerRepeatType",
    "SubstancePolymerRepeatRepeatUnitType",
    "SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisationType",
    "SubstancePolymerRepeatRepeatUnitStructuralRepresentationType",
    "SubstanceProteinType",
    "SubstanceProteinSubunitType",
    "SubstanceReferenceInformationType",
    "SubstanceReferenceInformationGeneType",
    "SubstanceReferenceInformationGeneElementType",
    "SubstanceReferenceInformationTargetType",
    "SubstanceSourceMaterialType",
    "SubstanceSourceMaterialFractionDescriptionType",
    "SubstanceSourceMaterialOrganismType",
    "SubstanceSourceMaterialOrganismAuthorType",
    "SubstanceSourceMaterialOrganismHybridType",
    "SubstanceSourceMaterialOrganismOrganismGeneralType",
    "SubstanceSourceMaterialPartDescriptionType",
    "SupplyDeliveryType",
    "SupplyDeliverySuppliedItemType",
    "SupplyRequestType",
    "SupplyRequestParameterType",
    "TaskType",
    "TaskInputType",
    "TaskOutputType",
    "TaskPerformerType",
    "TaskRestrictionType",
    "TerminologyCapabilitiesType",
    "TerminologyCapabilitiesClosureType",
    "TerminologyCapabilitiesCodeSystemType",
    "TerminologyCapabilitiesCodeSystemVersionType",
    "TerminologyCapabilitiesCodeSystemVersionFilterType",
    "TerminologyCapabilitiesExpansionType",
    "TerminologyCapabilitiesExpansionParameterType",
    "TerminologyCapabilitiesImplementationType",
    "TerminologyCapabilitiesSoftwareType",
    "TerminologyCapabilitiesTranslationType",
    "TerminologyCapabilitiesValidateCodeType",
    "TestPlanType",
    "TestPlanDependencyType",
    "TestPlanTestCaseType",
    "TestPlanTestCaseAssertionType",
    "TestPlanTestCaseDependencyType",
    "TestPlanTestCaseTestDataType",
    "TestPlanTestCaseTestRunType",
    "TestPlanTestCaseTestRunScriptType",
    "TestReportType",
    "TestReportParticipantType",
    "TestReportSetupType",
    "TestReportSetupActionType",
    "TestReportSetupActionAssertType",
    "TestReportSetupActionAssertRequirementType",
    "TestReportSetupActionOperationType",
    "TestReportTeardownType",
    "TestReportTeardownActionType",
    "TestReportTestType",
    "TestReportTestActionType",
    "TestScriptType",
    "TestScriptDestinationType",
    "TestScriptFixtureType",
    "TestScriptMetadataType",
    "TestScriptMetadataCapabilityType",
    "TestScriptMetadataLinkType",
    "TestScriptOriginType",
    "TestScriptScopeType",
    "TestScriptSetupType",
    "TestScriptSetupActionType",
    "TestScriptSetupActionAssertType",
    "TestScriptSetupActionAssertRequirementType",
    "TestScriptSetupActionOperationType",
    "TestScriptSetupActionOperationRequestHeaderType",
    "TestScriptTeardownType",
    "TestScriptTeardownActionType",
    "TestScriptTestType",
    "TestScriptTestActionType",
    "TestScriptVariableType",
    "TimingType",
    "TimingRepeatType",
    "TransportType",
    "TransportInputType",
    "TransportOutputType",
    "TransportRestrictionType",
    "TriggerDefinitionType",
    "UsageContextType",
    "ValueSetType",
    "ValueSetComposeType",
    "ValueSetComposeIncludeType",
    "ValueSetComposeIncludeConceptType",
    "ValueSetComposeIncludeConceptDesignationType",
    "ValueSetComposeIncludeFilterType",
    "ValueSetExpansionType",
    "ValueSetExpansionContainsType",
    "ValueSetExpansionContainsPropertyType",
    "ValueSetExpansionContainsPropertySubPropertyType",
    "ValueSetExpansionParameterType",
    "ValueSetExpansionPropertyType",
    "ValueSetScopeType",
    "VerificationResultType",
    "VerificationResultAttestationType",
    "VerificationResultPrimarySourceType",
    "VerificationResultValidatorType",
    "VirtualServiceDetailType",
    "VisionPrescriptionType",
    "VisionPrescriptionLensSpecificationType",
    "VisionPrescriptionLensSpecificationPrismType",
]
