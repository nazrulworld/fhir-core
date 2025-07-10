from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Identifier
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from pydantic import Field

from . import datatype, fhirtypes


class Identifier(datatype.DataType):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An identifier intended for computation.
    An identifier - identifies some entity uniquely and unambiguously.
    Typically this is used for business identifiers.
    """

    __resource_type__ = "Identifier"

    assigner: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="assigner",
        title="Organization that issued id (may be just text)",
        description="Organization that issued/manages the identifier.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    period: fhirtypes.PeriodType | None = Field(  # type: ignore
        default=None,
        alias="period",
        title="Time period when id is/was valid for use",
        description="Time period during which identifier is/was valid for use.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    system: fhirtypes.UriType | None = Field(  # type: ignore
        default=None,
        alias="system",
        title="The namespace for the identifier value",
        description=(
            "Establishes the namespace for the value - that is, an absolute URL "
            "that describes a set values that are unique."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    system__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_system", title="Extension field for ``system``."
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="type",
        title="Description of identifier",
        description=(
            "A coded type for the identifier that can be used to determine which "
            "identifier to use for a specific purpose."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    use: fhirtypes.CodeType | None = Field(  # type: ignore
        default=None,
        alias="use",
        title="usual | official | temp | secondary | old (If known)",
        description="The purpose of this identifier.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["usual", "official", "temp", "secondary", "old"],
        },
    )
    use__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_use", title="Extension field for ``use``."
    )

    value: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="value",
        title="The value that is unique",
        description=(
            "The portion of the identifier typically relevant to the user and which"
            " is unique within the context of the system."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_value", title="Extension field for ``value``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``Identifier`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "extension",
            "use",
            "type",
            "system",
            "value",
            "period",
            "assigner",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``Identifier`` according to specification,
        with preserving the original sequence order.
        """
        return ["use", "type", "system", "value", "period", "assigner"]
