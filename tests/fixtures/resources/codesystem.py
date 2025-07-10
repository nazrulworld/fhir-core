from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/CodeSystem
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class CodeSystem(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Declares the existence of and describes a code system or code system
    supplement.
    The CodeSystem resource is used to declare the existence of and describe a
    code system or code system supplement and its key properties, and
    optionally define a part or all of its content.
    """

    __resource_type__ = "CodeSystem"

    approvalDate: fhirtypes.DateType | None = Field(  # type: ignore
        default=None,
        alias="approvalDate",
        title="When the CodeSystem was approved by publisher",
        description=(
            "The date on which the resource content was approved by the publisher. "
            "Approval happens once when the content is officially approved for "
            "usage."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    approvalDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_approvalDate",
        title="Extension field for ``approvalDate``.",
    )

    author: typing.List[fhirtypes.ContactDetailType] | None = Field(  # type: ignore
        default=None,
        alias="author",
        title="Who authored the CodeSystem",
        description=(
            "An individiual or organization primarily involved in the creation and "
            "maintenance of the CodeSystem."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    caseSensitive: bool | None = Field(  # type: ignore
        default=None,
        alias="caseSensitive",
        title="If code comparison is case sensitive",
        description=(
            "If code comparison is case sensitive when codes within this system are"
            " compared to each other."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    caseSensitive__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_caseSensitive",
        title="Extension field for ``caseSensitive``.",
    )

    compositional: bool | None = Field(  # type: ignore
        default=None,
        alias="compositional",
        title="If code system defines a compositional grammar",
        description="The code system defines a compositional (post-coordination) grammar.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    compositional__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_compositional",
        title="Extension field for ``compositional``.",
    )

    concept: typing.List[fhirtypes.CodeSystemConceptType] | None = Field(  # type: ignore
        default=None,
        alias="concept",
        title="Concepts in the code system",
        description=(
            "Concepts that are in the code system. The concept definitions are "
            "inherently hierarchical, but the definitions must be consulted to "
            "determine what the meanings of the hierarchical relationships are."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    contact: typing.List[fhirtypes.ContactDetailType] | None = Field(  # type: ignore
        default=None,
        alias="contact",
        title="Contact details for the publisher",
        description=(
            "Contact details to assist a user in finding and communicating with the"
            " publisher."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    content: fhirtypes.CodeType | None = Field(  # type: ignore
        default=None,
        alias="content",
        title="not-present | example | fragment | complete | supplement",
        description=(
            "The extent of the content of the code system (the concepts and codes "
            "it defines) are represented in this resource instance."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "not-present",
                "example",
                "fragment",
                "complete",
                "supplement",
            ],
        },
    )
    content__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_content", title="Extension field for ``content``."
    )

    copyright: fhirtypes.MarkdownType | None = Field(  # type: ignore
        default=None,
        alias="copyright",
        title="Use and/or publishing restrictions",
        description=(
            "A copyright statement relating to the code system and/or its contents."
            " Copyright statements are generally legal restrictions on the use and "
            "publishing of the code system."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_copyright", title="Extension field for ``copyright``."
    )

    copyrightLabel: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="copyrightLabel",
        title="Copyright holder and year(s)",
        description=(
            "A short string (<50 characters), suitable for inclusion in a page "
            "footer that identifies the copyright holder, effective period, and "
            "optionally whether rights are resctricted. (e.g. 'All rights "
            "reserved', 'Some rights reserved')."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    copyrightLabel__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_copyrightLabel",
        title="Extension field for ``copyrightLabel``.",
    )

    count: fhirtypes.UnsignedIntType | None = Field(  # type: ignore
        default=None,
        alias="count",
        title="Total concepts in the code system",
        description=(
            "The total number of concepts defined by the code system. Where the "
            "code system has a compositional grammar, the basis of this count is "
            "defined by the system steward."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    count__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_count", title="Extension field for ``count``."
    )

    date: fhirtypes.DateTimeType | None = Field(  # type: ignore
        default=None,
        alias="date",
        title="Date last changed",
        description=(
            "The date  (and optionally time) when the code system was last "
            "significantly changed. The date must change when the business version "
            "changes and it must change if the status code changes. In addition, it"
            " should change when the substantive content of the code system "
            "changes."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_date", title="Extension field for ``date``."
    )

    description: fhirtypes.MarkdownType | None = Field(  # type: ignore
        default=None,
        alias="description",
        title="Natural language description of the code system",
        description=(
            "A free text natural language description of the code system from a "
            "consumer's perspective."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_description", title="Extension field for ``description``."
    )

    editor: typing.List[fhirtypes.ContactDetailType] | None = Field(  # type: ignore
        default=None,
        alias="editor",
        title="Who edited the CodeSystem",
        description=(
            "An individual or organization primarily responsible for internal "
            "coherence of the CodeSystem."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    effectivePeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
        default=None,
        alias="effectivePeriod",
        title="When the CodeSystem is expected to be used",
        description=(
            "The period during which the CodeSystem content was or is planned to be"
            " in active use."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    endorser: typing.List[fhirtypes.ContactDetailType] | None = Field(  # type: ignore
        default=None,
        alias="endorser",
        title="Who endorsed the CodeSystem",
        description=(
            "An individual or organization asserted by the publisher to be "
            "responsible for officially endorsing the CodeSystem for use in some "
            "setting."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    experimental: bool | None = Field(  # type: ignore
        default=None,
        alias="experimental",
        title="For testing purposes, not real usage",
        description=(
            "A Boolean value to indicate that this code system is authored for "
            "testing purposes (or education/evaluation/marketing) and is not "
            "intended to be used for genuine usage."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_experimental",
        title="Extension field for ``experimental``.",
    )

    filter: typing.List[fhirtypes.CodeSystemFilterType] | None = Field(  # type: ignore
        default=None,
        alias="filter",
        title="Filter that can be used in a value set",
        description=(
            "A filter that can be used in a value set compose statement when "
            "selecting concepts using a filter."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    hierarchyMeaning: fhirtypes.CodeType | None = Field(  # type: ignore
        default=None,
        alias="hierarchyMeaning",
        title="grouped-by | is-a | part-of | classified-with",
        description=(
            "The meaning of the hierarchy of concepts as represented in this "
            "resource."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["grouped-by", "is-a", "part-of", "classified-with"],
        },
    )
    hierarchyMeaning__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_hierarchyMeaning",
        title="Extension field for ``hierarchyMeaning``.",
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        default=None,
        alias="identifier",
        title="Additional identifier for the code system (business identifier)",
        description=(
            "A formal identifier that is used to identify this code system when it "
            "is represented in other formats, or referenced in a specification, "
            "model, design or an instance."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    jurisdiction: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        default=None,
        alias="jurisdiction",
        title="Intended jurisdiction for code system (if applicable)",
        description=(
            "A legal or geographic region in which the code system is intended to "
            "be used."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    lastReviewDate: fhirtypes.DateType | None = Field(  # type: ignore
        default=None,
        alias="lastReviewDate",
        title="When the CodeSystem was last reviewed by the publisher",
        description=(
            "The date on which the resource content was last reviewed. Review "
            "happens periodically after approval but does not change the original "
            "approval date."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    lastReviewDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_lastReviewDate",
        title="Extension field for ``lastReviewDate``.",
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="name",
        title="Name for this code system (computer friendly)",
        description=(
            "A natural language name identifying the code system. This name should "
            "be usable as an identifier for the module by machine processing "
            "applications such as code generation."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_name", title="Extension field for ``name``."
    )

    property: typing.List[fhirtypes.CodeSystemPropertyType] | None = Field(  # type: ignore
        default=None,
        alias="property",
        title="Additional information supplied about each concept",
        description=(
            "A property defines an additional slot through which additional "
            "information can be provided about a concept."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    publisher: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="publisher",
        title="Name of the publisher/steward (organization or individual)",
        description=(
            "The name of the organization or individual responsible for the release"
            " and ongoing maintenance of the code system."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_publisher", title="Extension field for ``publisher``."
    )

    purpose: fhirtypes.MarkdownType | None = Field(  # type: ignore
        default=None,
        alias="purpose",
        title="Why this code system is defined",
        description=(
            "Explanation of why this code system is needed and why it has been "
            "designed as it has."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_purpose", title="Extension field for ``purpose``."
    )

    relatedArtifact: typing.List[fhirtypes.RelatedArtifactType] | None = Field(  # type: ignore
        default=None,
        alias="relatedArtifact",
        title="Additional documentation, citations, etc",
        description=(
            "Related artifacts such as additional documentation, justification, "
            "dependencies, bibliographic references, and predecessor and successor "
            "artifacts."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    reviewer: typing.List[fhirtypes.ContactDetailType] | None = Field(  # type: ignore
        default=None,
        alias="reviewer",
        title="Who reviewed the CodeSystem",
        description=(
            "An individual or organization asserted by the publisher to be "
            "primarily responsible for review of some aspect of the CodeSystem."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        default=None,
        alias="status",
        title="draft | active | retired | unknown",
        description=(
            "The status of this code system. Enables tracking the life-cycle of the"
            " content."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["draft", "active", "retired", "unknown"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_status", title="Extension field for ``status``."
    )

    supplements: fhirtypes.CanonicalType | None = Field(  # type: ignore
        default=None,
        alias="supplements",
        title="Canonical URL of Code System this adds designations and properties to",
        description=(
            "The canonical URL of the code system that this code system supplement "
            "is adding designations and properties to."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["CodeSystem"],
        },
    )
    supplements__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_supplements", title="Extension field for ``supplements``."
    )

    title: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="title",
        title="Name for this code system (human friendly)",
        description="A short, descriptive, user-friendly title for the code system.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_title", title="Extension field for ``title``."
    )

    topic: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        default=None,
        alias="topic",
        title="E.g. Education, Treatment, Assessment, etc",
        description=(
            "Descriptions related to the content of the CodeSystem. Topics provide "
            "a high-level categorization as well as keywords for the CodeSystem "
            "that can be useful for filtering and searching."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    url: fhirtypes.UriType | None = Field(  # type: ignore
        default=None,
        alias="url",
        title=(
            "Canonical identifier for this code system, represented as a URI "
            "(globally unique) (Coding.system)"
        ),
        description=(
            "An absolute URI that is used to identify this code system when it is "
            "referenced in a specification, model, design or an instance; also "
            "called its canonical identifier. This SHOULD be globally unique and "
            "SHOULD be a literal address at which an authoritative instance of this"
            " code system is (or will be) published. This URL can be the target of "
            "a canonical reference. It SHALL remain the same when the code system "
            "is stored on different servers. This is used in "
            "[Coding](datatypes.html#Coding).system."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_url", title="Extension field for ``url``."
    )

    useContext: typing.List[fhirtypes.UsageContextType] | None = Field(  # type: ignore
        default=None,
        alias="useContext",
        title="The context that the content is intended to support",
        description=(
            "The content was developed with a focus and intent of supporting the "
            "contexts that are listed. These contexts may be general categories "
            "(gender, age, ...) or may be references to specific programs "
            "(insurance plans, studies, ...) and may be used to assist with "
            "indexing and searching for appropriate code system instances."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    valueSet: fhirtypes.CanonicalType | None = Field(  # type: ignore
        default=None,
        alias="valueSet",
        title="Canonical reference to the value set with entire code system",
        description=(
            "Canonical reference to the value set that contains all codes in the "
            "code system independent of code status."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ValueSet"],
        },
    )
    valueSet__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_valueSet", title="Extension field for ``valueSet``."
    )

    version: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="version",
        title="Business version of the code system (Coding.version)",
        description=(
            "The identifier that is used to identify this version of the code "
            "system when it is referenced in a specification, model, design or "
            "instance. This is an arbitrary value managed by the code system author"
            " and is not expected to be globally unique. For example, it might be a"
            " timestamp (e.g. yyyymmdd) if a managed version is not available. "
            "There is also no expectation that versions can be placed in a "
            "lexicographical sequence. This is used in "
            "[Coding](datatypes.html#Coding).version."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_version", title="Extension field for ``version``."
    )

    versionAlgorithmCoding: fhirtypes.CodingType | None = Field(  # type: ignore
        default=None,
        alias="versionAlgorithmCoding",
        title="How to compare versions",
        description=(
            "Indicates the mechanism used to compare versions to determine which "
            "CodeSystem is more current."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # Choice of Data Types. i.e versionAlgorithm[x]
            "one_of_many": "versionAlgorithm",
            "one_of_many_required": False,
        },
    )

    versionAlgorithmString: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="versionAlgorithmString",
        title="How to compare versions",
        description=(
            "Indicates the mechanism used to compare versions to determine which "
            "CodeSystem is more current."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # Choice of Data Types. i.e versionAlgorithm[x]
            "one_of_many": "versionAlgorithm",
            "one_of_many_required": False,
        },
    )
    versionAlgorithmString__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_versionAlgorithmString",
        title="Extension field for ``versionAlgorithmString``.",
    )

    versionNeeded: bool | None = Field(  # type: ignore
        default=None,
        alias="versionNeeded",
        title="If definitions are not stable",
        description=(
            "This flag is used to signify that the code system does not commit to "
            "concept permanence across versions. If true, a version must be "
            "specified when referencing this code system."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    versionNeeded__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_versionNeeded",
        title="Extension field for ``versionNeeded``.",
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``CodeSystem`` according to specification,
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
            "url",
            "identifier",
            "version",
            "versionAlgorithmString",
            "versionAlgorithmCoding",
            "name",
            "title",
            "status",
            "experimental",
            "date",
            "publisher",
            "contact",
            "description",
            "useContext",
            "jurisdiction",
            "purpose",
            "copyright",
            "copyrightLabel",
            "approvalDate",
            "lastReviewDate",
            "effectivePeriod",
            "topic",
            "author",
            "editor",
            "reviewer",
            "endorser",
            "relatedArtifact",
            "caseSensitive",
            "valueSet",
            "hierarchyMeaning",
            "compositional",
            "versionNeeded",
            "content",
            "supplements",
            "count",
            "filter",
            "property",
            "concept",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``CodeSystem`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "meta",
            "implicitRules",
            "modifierExtension",
            "url",
            "identifier",
            "version",
            "versionAlgorithmString",
            "versionAlgorithmCoding",
            "name",
            "title",
            "status",
            "experimental",
            "date",
            "publisher",
            "contact",
            "useContext",
            "jurisdiction",
            "effectivePeriod",
            "caseSensitive",
            "valueSet",
            "hierarchyMeaning",
            "compositional",
            "versionNeeded",
            "content",
            "supplements",
            "count",
            "filter",
            "property",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("content", "content__ext"), ("status", "status__ext")]
        return required_fields

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
            "versionAlgorithm": ["versionAlgorithmCoding", "versionAlgorithmString"]
        }
        return one_of_many_fields


class CodeSystemConcept(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Concepts in the code system.
    Concepts that are in the code system. The concept definitions are
    inherently hierarchical, but the definitions must be consulted to determine
    what the meanings of the hierarchical relationships are.
    """

    __resource_type__ = "CodeSystemConcept"

    code: fhirtypes.CodeType | None = Field(  # type: ignore
        default=None,
        alias="code",
        title="Code that identifies concept",
        description=(
            "A code - a text symbol - that uniquely identifies the concept within "
            "the code system."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_code", title="Extension field for ``code``."
    )

    concept: typing.List[fhirtypes.CodeSystemConceptType] | None = Field(  # type: ignore
        default=None,
        alias="concept",
        title="Child Concepts (is-a/contains/categorizes)",
        description=(
            "Defines children of a concept to produce a hierarchy of concepts. The "
            "nature of the relationships is variable (is-a/contains/categorizes) - "
            "see hierarchyMeaning."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    definition: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="definition",
        title="Formal definition",
        description=(
            "The formal definition of the concept. The code system resource does "
            "not make formal definitions required, because of the prevalence of "
            "legacy systems. However, they are highly recommended, as without them "
            "there is no formal meaning associated with the concept."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    definition__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_definition", title="Extension field for ``definition``."
    )

    designation: typing.List[fhirtypes.CodeSystemConceptDesignationType] | None = Field(  # type: ignore
        default=None,
        alias="designation",
        title="Additional representations for the concept",
        description=(
            "Additional representations for the concept - other languages, aliases,"
            " specialized purposes, used for particular purposes, etc."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    display: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="display",
        title="Text to display to the user",
        description=(
            "A human readable string that is the recommended default way to present"
            " this concept to a user."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    display__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_display", title="Extension field for ``display``."
    )

    property: typing.List[fhirtypes.CodeSystemConceptPropertyType] | None = Field(  # type: ignore
        default=None,
        alias="property",
        title="Property value for the concept",
        description="A property value for this concept.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``CodeSystemConcept`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "code",
            "display",
            "definition",
            "designation",
            "property",
            "concept",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``CodeSystemConcept`` according to specification,
        with preserving the original sequence order.
        """
        return ["modifierExtension"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("code", "code__ext")]
        return required_fields


class CodeSystemConceptDesignation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Additional representations for the concept.
    Additional representations for the concept - other languages, aliases,
    specialized purposes, used for particular purposes, etc.
    """

    __resource_type__ = "CodeSystemConceptDesignation"

    additionalUse: typing.List[fhirtypes.CodingType] | None = Field(  # type: ignore
        default=None,
        alias="additionalUse",
        title="Additional ways how this designation would be used",
        description=(
            "Additional codes that detail how this designation would be used, if "
            "there is more than one use."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    language: fhirtypes.CodeType | None = Field(  # type: ignore
        default=None,
        alias="language",
        title="Human language of the designation",
        description="The language this designation is defined for.",
        json_schema_extra={
            "element_property": True,
        },
    )
    language__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_language", title="Extension field for ``language``."
    )

    use: fhirtypes.CodingType | None = Field(  # type: ignore
        default=None,
        alias="use",
        title="Details how this designation would be used",
        description="A code that details how this designation would be used.",
        json_schema_extra={
            "element_property": True,
        },
    )

    value: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="value",
        title="The text value for this designation",
        description=None,
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_value", title="Extension field for ``value``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``CodeSystemConceptDesignation`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "language",
            "use",
            "additionalUse",
            "value",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``CodeSystemConceptDesignation`` according to specification,
        with preserving the original sequence order.
        """
        return ["modifierExtension"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("value", "value__ext")]
        return required_fields


class CodeSystemConceptProperty(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Property value for the concept.
    A property value for this concept.
    """

    __resource_type__ = "CodeSystemConceptProperty"

    code: fhirtypes.CodeType | None = Field(  # type: ignore
        default=None,
        alias="code",
        title="Reference to CodeSystem.property.code",
        description="A code that is a reference to CodeSystem.property.code.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_code", title="Extension field for ``code``."
    )

    valueBoolean: bool | None = Field(  # type: ignore
        default=None,
        alias="valueBoolean",
        title="Value of the property for this concept",
        description="The value of this property.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_valueBoolean",
        title="Extension field for ``valueBoolean``.",
    )

    valueCode: fhirtypes.CodeType | None = Field(  # type: ignore
        default=None,
        alias="valueCode",
        title="Value of the property for this concept",
        description="The value of this property.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )
    valueCode__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_valueCode", title="Extension field for ``valueCode``."
    )

    valueCoding: fhirtypes.CodingType | None = Field(  # type: ignore
        default=None,
        alias="valueCoding",
        title="Value of the property for this concept",
        description="The value of this property.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )

    valueDateTime: fhirtypes.DateTimeType | None = Field(  # type: ignore
        default=None,
        alias="valueDateTime",
        title="Value of the property for this concept",
        description="The value of this property.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )
    valueDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_valueDateTime",
        title="Extension field for ``valueDateTime``.",
    )

    valueDecimal: fhirtypes.DecimalType | None = Field(  # type: ignore
        default=None,
        alias="valueDecimal",
        title="Value of the property for this concept",
        description="The value of this property.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )
    valueDecimal__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_valueDecimal",
        title="Extension field for ``valueDecimal``.",
    )

    valueInteger: fhirtypes.IntegerType | None = Field(  # type: ignore
        default=None,
        alias="valueInteger",
        title="Value of the property for this concept",
        description="The value of this property.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )
    valueInteger__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_valueInteger",
        title="Extension field for ``valueInteger``.",
    )

    valueString: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="valueString",
        title="Value of the property for this concept",
        description="The value of this property.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_valueString", title="Extension field for ``valueString``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``CodeSystemConceptProperty`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "code",
            "valueCode",
            "valueCoding",
            "valueString",
            "valueInteger",
            "valueBoolean",
            "valueDateTime",
            "valueDecimal",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``CodeSystemConceptProperty`` according to specification,
        with preserving the original sequence order.
        """
        return ["modifierExtension"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("code", "code__ext")]
        return required_fields

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
            "value": [
                "valueBoolean",
                "valueCode",
                "valueCoding",
                "valueDateTime",
                "valueDecimal",
                "valueInteger",
                "valueString",
            ]
        }
        return one_of_many_fields


class CodeSystemFilter(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Filter that can be used in a value set.
    A filter that can be used in a value set compose statement when selecting
    concepts using a filter.
    """

    __resource_type__ = "CodeSystemFilter"

    code: fhirtypes.CodeType | None = Field(  # type: ignore
        default=None,
        alias="code",
        title="Code that identifies the filter",
        description=(
            "The code that identifies this filter when it is used as a filter in "
            "[ValueSet](valueset.html#).compose.include.filter."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            "element_required": True,
        },
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_code", title="Extension field for ``code``."
    )

    description: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="description",
        title="How or why the filter is used",
        description="A description of how or why the filter is used.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_description", title="Extension field for ``description``."
    )

    operator: typing.List[fhirtypes.CodeType | None] | None = Field(  # type: ignore
        default=None,
        alias="operator",
        title=(
            "= | is-a | descendent-of | is-not-a | regex | in | not-in | "
            "generalizes | child-of | descendent-leaf | exists"
        ),
        description="A list of operators that can be used with the filter.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "=",
                "is-a",
                "descendent-of",
                "is-not-a",
                "regex",
                "in",
                "not-in",
                "generalizes",
                "child-of",
                "descendent-leaf",
                "exists",
            ],
        },
    )
    operator__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        default=None, alias="_operator", title="Extension field for ``operator``."
    )

    value: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="value",
        title="What to use for the value",
        description="A description of what the value for the filter should be.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            "element_required": True,
        },
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_value", title="Extension field for ``value``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``CodeSystemFilter`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "code",
            "description",
            "operator",
            "value",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``CodeSystemFilter`` according to specification,
        with preserving the original sequence order.
        """
        return ["modifierExtension", "code", "description", "operator", "value"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [
            ("code", "code__ext"),
            ("operator", "operator__ext"),
            ("value", "value__ext"),
        ]
        return required_fields


class CodeSystemProperty(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Additional information supplied about each concept.
    A property defines an additional slot through which additional information
    can be provided about a concept.
    """

    __resource_type__ = "CodeSystemProperty"

    code: fhirtypes.CodeType | None = Field(  # type: ignore
        default=None,
        alias="code",
        title=(
            "Identifies the property on the concepts, and when referred to in "
            "operations"
        ),
        description=(
            "A code that is used to identify the property. The code is used "
            "internally (in CodeSystem.concept.property.code) and also externally, "
            "such as in property filters."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            "element_required": True,
        },
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_code", title="Extension field for ``code``."
    )

    description: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="description",
        title="Why the property is defined, and/or what it conveys",
        description=(
            "A description of the property- why it is defined, and how its value "
            "might be used."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_description", title="Extension field for ``description``."
    )

    type: fhirtypes.CodeType | None = Field(  # type: ignore
        default=None,
        alias="type",
        title="code | Coding | string | integer | boolean | dateTime | decimal",
        description=(
            'The type of the property value. Properties of type "code" contain a '
            "code defined by the code system (e.g. a reference to another defined "
            "concept)."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "code",
                "Coding",
                "string",
                "integer",
                "boolean",
                "dateTime",
                "decimal",
            ],
        },
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_type", title="Extension field for ``type``."
    )

    uri: fhirtypes.UriType | None = Field(  # type: ignore
        default=None,
        alias="uri",
        title="Formal identifier for the property",
        description=(
            "Reference to the formal meaning of the property. One possible source "
            "of meaning is the [Concept Properties](codesystem-concept-"
            "properties.html) code system."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    uri__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_uri", title="Extension field for ``uri``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``CodeSystemProperty`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "code",
            "uri",
            "description",
            "type",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``CodeSystemProperty`` according to specification,
        with preserving the original sequence order.
        """
        return ["modifierExtension", "code", "uri", "description", "type"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("code", "code__ext"), ("type", "type__ext")]
        return required_fields
