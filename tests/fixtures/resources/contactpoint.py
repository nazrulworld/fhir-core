from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/ContactPoint
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from pydantic import Field

from . import datatype, fhirtypes


class ContactPoint(datatype.DataType):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Details of a Technology mediated contact point (phone, fax, email, etc.).
    Details for all kinds of technology mediated contact points for a person or
    organization, including telephone, email, etc.
    """

    __resource_type__ = "ContactPoint"

    period: fhirtypes.PeriodType | None = Field(  # type: ignore
        default=None,
        alias="period",
        title="Time period when the contact point was/is in use",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    rank: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        default=None,
        alias="rank",
        title="Specify preferred order of use (1 = highest)",
        description=(
            "Specifies a preferred order in which to use a set of contacts. "
            "ContactPoints with lower rank values are more preferred than those "
            "with higher rank values."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    rank__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_rank", title="Extension field for ``rank``."
    )

    system: fhirtypes.CodeType | None = Field(  # type: ignore
        default=None,
        alias="system",
        title="phone | fax | email | pager | url | sms | other",
        description=(
            "Telecommunications form for contact point - what communications system"
            " is required to make use of the contact."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["phone", "fax", "email", "pager", "url", "sms", "other"],
        },
    )
    system__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_system", title="Extension field for ``system``."
    )

    use: fhirtypes.CodeType | None = Field(  # type: ignore
        default=None,
        alias="use",
        title="home | work | temp | old | mobile - purpose of this contact point",
        description="Identifies the purpose for the contact point.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["home", "work", "temp", "old", "mobile"],
        },
    )
    use__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_use", title="Extension field for ``use``."
    )

    value: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="value",
        title="The actual contact point details",
        description=(
            "The actual contact point details, in a form that is meaningful to the "
            "designated communication system (i.e. phone number or email address)."
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
        ``ContactPoint`` according to specification,
        with preserving the original sequence order.
        """
        return ["id", "extension", "system", "value", "use", "rank", "period"]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``ContactPoint`` according to specification,
        with preserving the original sequence order.
        """
        return ["system", "value", "use", "rank", "period"]
