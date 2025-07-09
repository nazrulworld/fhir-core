from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Patient
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class Patient(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Information about an individual or animal receiving health care services.
    Demographics and other administrative information about an individual or
    animal receiving care or other health-related services.
    """

    __resource_type__ = "Patient"

    active: bool | None = Field(  # type: ignore
        default=None,
        alias="active",
        title="Whether this patient's record is in active use",
        description=(
            "Whether this patient record is in active use.  Many systems use this "
            "property to mark as non-current patients, such as those that have not "
            "been seen for a period of time based on an organization's business "
            "rules.  It is often used to filter patient lists to exclude inactive "
            "patients  Deceased patients may also be marked as inactive for the "
            "same reasons, but may be active for some time after death."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    active__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_active", title="Extension field for ``active``."
    )

    address: typing.List[fhirtypes.AddressType] | None = Field(  # type: ignore
        default=None,
        alias="address",
        title="An address for the individual",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    birthDate: fhirtypes.DateType | None = Field(  # type: ignore
        default=None,
        alias="birthDate",
        title="The date of birth for the individual",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    birthDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_birthDate", title="Extension field for ``birthDate``."
    )

    communication: typing.List[fhirtypes.PatientCommunicationType] | None = Field(  # type: ignore
        default=None,
        alias="communication",
        title=(
            "A language which may be used to communicate with the patient about his"
            " or her health"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    contact: typing.List[fhirtypes.PatientContactType] | None = Field(  # type: ignore
        default=None,
        alias="contact",
        title="A contact party (e.g. guardian, partner, friend) for the patient",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    deceasedBoolean: bool | None = Field(  # type: ignore
        default=None,
        alias="deceasedBoolean",
        title="Indicates if the individual is deceased or not",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # Choice of Data Types. i.e deceased[x]
            "one_of_many": "deceased",
            "one_of_many_required": False,
        },
    )
    deceasedBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_deceasedBoolean",
        title="Extension field for ``deceasedBoolean``.",
    )

    deceasedDateTime: fhirtypes.DateTimeType | None = Field(  # type: ignore
        default=None,
        alias="deceasedDateTime",
        title="Indicates if the individual is deceased or not",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # Choice of Data Types. i.e deceased[x]
            "one_of_many": "deceased",
            "one_of_many_required": False,
        },
    )
    deceasedDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_deceasedDateTime",
        title="Extension field for ``deceasedDateTime``.",
    )

    gender: fhirtypes.CodeType | None = Field(  # type: ignore
        default=None,
        alias="gender",
        title="male | female | other | unknown",
        description=(
            "Administrative Gender - the gender that the patient is considered to "
            "have for administration and record keeping purposes."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["male", "female", "other", "unknown"],
        },
    )
    gender__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_gender", title="Extension field for ``gender``."
    )

    generalPractitioner: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        default=None,
        alias="generalPractitioner",
        title="Patient's nominated primary care provider",
        description="Patient's nominated care provider.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Organization",
                "Practitioner",
                "PractitionerRole",
            ],
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        default=None,
        alias="identifier",
        title="An identifier for this patient",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    link: typing.List[fhirtypes.PatientLinkType] | None = Field(  # type: ignore
        default=None,
        alias="link",
        title=(
            "Link to a Patient or RelatedPerson resource that concerns the same "
            "actual individual"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    managingOrganization: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="managingOrganization",
        title="Organization that is the custodian of the patient record",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    maritalStatus: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="maritalStatus",
        title="Marital (civil) status of a patient",
        description="This field contains a patient's most recent marital (civil) status.",
        json_schema_extra={
            "element_property": True,
        },
    )

    multipleBirthBoolean: bool | None = Field(  # type: ignore
        default=None,
        alias="multipleBirthBoolean",
        title="Whether patient is part of a multiple birth",
        description=(
            "Indicates whether the patient is part of a multiple (boolean) or "
            "indicates the actual birth order (integer)."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e multipleBirth[x]
            "one_of_many": "multipleBirth",
            "one_of_many_required": False,
        },
    )
    multipleBirthBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_multipleBirthBoolean",
        title="Extension field for ``multipleBirthBoolean``.",
    )

    multipleBirthInteger: fhirtypes.IntegerType | None = Field(  # type: ignore
        default=None,
        alias="multipleBirthInteger",
        title="Whether patient is part of a multiple birth",
        description=(
            "Indicates whether the patient is part of a multiple (boolean) or "
            "indicates the actual birth order (integer)."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e multipleBirth[x]
            "one_of_many": "multipleBirth",
            "one_of_many_required": False,
        },
    )
    multipleBirthInteger__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_multipleBirthInteger",
        title="Extension field for ``multipleBirthInteger``.",
    )

    name: typing.List[fhirtypes.HumanNameType] | None = Field(  # type: ignore
        default=None,
        alias="name",
        title="A name associated with the patient",
        description="A name associated with the individual.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    photo: typing.List[fhirtypes.AttachmentType] | None = Field(  # type: ignore
        default=None,
        alias="photo",
        title="Image of the patient",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    telecom: typing.List[fhirtypes.ContactPointType] | None = Field(  # type: ignore
        default=None,
        alias="telecom",
        title="A contact detail for the individual",
        description=(
            "A contact detail (e.g. a telephone number or an email address) by "
            "which the individual may be contacted."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``Patient`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "meta",
            "implicitRules",
            "language",
            "text",
            "contained",
            "extension",
            "modifierExtension",
            "identifier",
            "active",
            "name",
            "telecom",
            "gender",
            "birthDate",
            "deceasedBoolean",
            "deceasedDateTime",
            "address",
            "maritalStatus",
            "multipleBirthBoolean",
            "multipleBirthInteger",
            "photo",
            "contact",
            "communication",
            "generalPractitioner",
            "managingOrganization",
            "link",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``Patient`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "meta",
            "implicitRules",
            "modifierExtension",
            "identifier",
            "active",
            "name",
            "telecom",
            "gender",
            "birthDate",
            "deceasedBoolean",
            "deceasedDateTime",
            "address",
            "managingOrganization",
            "link",
        ]

    def get_one_of_many_fields(self) -> typing.Dict[str, typing.List[str]]:
        """https://www.hl7.org/fhir/formats.html#choice
        A few elements have a choice of more than one data type for their content.
        All such elements have a name that takes the form nnn[x].
        The "nnn" part of the name is constant, and the "[x]" is replaced with
        the title-cased name of the type that is actually used.
        The table view shows each of these names explicitly.

        Elements that have a choice of data type cannot repeat - they must have a
        maximum cardinality of 1. When constructing an instance of an element with a
        choice of types, the authoring system must create a single element with a
        data type chosen from among the list of permitted data types.
        """
        one_of_many_fields = {
            "deceased": ["deceasedBoolean", "deceasedDateTime"],
            "multipleBirth": ["multipleBirthBoolean", "multipleBirthInteger"],
        }
        return one_of_many_fields


class PatientCommunication(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A language which may be used to communicate with the patient about his or
    her health.
    """

    __resource_type__ = "PatientCommunication"

    language: fhirtypes.CodeableConceptType = Field(  # type: ignore
        default=...,
        alias="language",
        title=(
            "The language which can be used to communicate with the patient about "
            "his or her health"
        ),
        description=(
            "The ISO-639-1 alpha 2 code in lower case for the language, optionally "
            "followed by a hyphen and the ISO-3166-1 alpha 2 code for the region in"
            ' upper case; e.g. "en" for English, or "en-US" for American English '
            'versus "en-AU" for Australian English.'
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    preferred: bool | None = Field(  # type: ignore
        default=None,
        alias="preferred",
        title="Language preference indicator",
        description=(
            "Indicates whether or not the patient prefers this language (over other"
            " languages he masters up a certain level)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    preferred__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_preferred", title="Extension field for ``preferred``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``PatientCommunication`` according to specification,
        with preserving the original sequence order.
        """
        return ["id", "extension", "modifierExtension", "language", "preferred"]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``PatientCommunication`` according to specification,
        with preserving the original sequence order.
        """
        return ["modifierExtension"]


class PatientContact(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A contact party (e.g. guardian, partner, friend) for the patient.
    """

    __resource_type__ = "PatientContact"

    address: fhirtypes.AddressType | None = Field(  # type: ignore
        default=None,
        alias="address",
        title="Address for the contact person",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    gender: fhirtypes.CodeType | None = Field(  # type: ignore
        default=None,
        alias="gender",
        title="male | female | other | unknown",
        description=(
            "Administrative Gender - the gender that the contact person is "
            "considered to have for administration and record keeping purposes."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["male", "female", "other", "unknown"],
        },
    )
    gender__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_gender", title="Extension field for ``gender``."
    )

    name: fhirtypes.HumanNameType | None = Field(  # type: ignore
        default=None,
        alias="name",
        title="A name associated with the contact person",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    organization: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="organization",
        title="Organization that is associated with the contact",
        description=(
            "Organization on behalf of which the contact is acting or for which the"
            " contact is working."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    period: fhirtypes.PeriodType | None = Field(  # type: ignore
        default=None,
        alias="period",
        title=(
            "The period during which this contact person or organization is valid "
            "to be contacted relating to this patient"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    relationship: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        default=None,
        alias="relationship",
        title="The kind of relationship",
        description=(
            "The nature of the relationship between the patient and the contact "
            "person."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    telecom: typing.List[fhirtypes.ContactPointType] | None = Field(  # type: ignore
        default=None,
        alias="telecom",
        title="A contact detail for the person",
        description=(
            "A contact detail for the person, e.g. a telephone number or an email "
            "address."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``PatientContact`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "relationship",
            "name",
            "telecom",
            "address",
            "gender",
            "organization",
            "period",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``PatientContact`` according to specification,
        with preserving the original sequence order.
        """
        return ["modifierExtension"]


class PatientLink(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Link to a Patient or RelatedPerson resource that concerns the same actual
    individual.
    """

    __resource_type__ = "PatientLink"

    other: fhirtypes.ReferenceType = Field(  # type: ignore
        default=...,
        alias="other",
        title="The other patient or related person resource that the link refers to",
        description=(
            "Link to a Patient or RelatedPerson resource that concerns the same "
            "actual individual."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Patient", "RelatedPerson"],
        },
    )

    type: fhirtypes.CodeType | None = Field(  # type: ignore
        default=None,
        alias="type",
        title="replaced-by | replaces | refer | seealso",
        description=(
            "The type of link between this patient resource and another patient "
            "resource."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["replaced-by", "replaces", "refer", "seealso"],
        },
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_type", title="Extension field for ``type``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``PatientLink`` according to specification,
        with preserving the original sequence order.
        """
        return ["id", "extension", "modifierExtension", "other", "type"]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``PatientLink`` according to specification,
        with preserving the original sequence order.
        """
        return ["modifierExtension", "other", "type"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("type", "type__ext")]
        return required_fields
