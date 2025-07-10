from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Address
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import datatype, fhirtypes


class Address(datatype.DataType):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An address expressed using postal conventions (as opposed to GPS or other
    location definition formats).
    An address expressed using postal conventions (as opposed to GPS or other
    location definition formats).  This data type may be used to convey
    addresses for use in delivering mail as well as for visiting locations
    which might not be valid for mail delivery.  There are a variety of postal
    address formats defined around the world.
    The ISO21090-codedString may be used to provide a coded representation of
    the contents of strings in an Address.
    """

    __resource_type__ = "Address"

    city: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="city",
        title="Name of city, town etc.",
        description=(
            "The name of the city, town, suburb, village or other community or "
            "delivery center."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    city__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_city", title="Extension field for ``city``."
    )

    country: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="country",
        title="Country (e.g. may be ISO 3166 2 or 3 letter code)",
        description="Country - a nation as commonly understood or generally accepted.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    country__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_country", title="Extension field for ``country``."
    )

    district: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="district",
        title="District name (aka county)",
        description="The name of the administrative area (county).",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    district__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_district", title="Extension field for ``district``."
    )

    line: typing.List[fhirtypes.StringType | None] | None = Field(  # type: ignore
        default=None,
        alias="line",
        title="Street name, number, direction & P.O. Box etc.",
        description=(
            "This component contains the house number, apartment number, street "
            "name, street direction,  P.O. Box number, delivery hints, and similar "
            "address information."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    line__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        default=None, alias="_line", title="Extension field for ``line``."
    )

    period: fhirtypes.PeriodType | None = Field(  # type: ignore
        default=None,
        alias="period",
        title="Time period when address was/is in use",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    postalCode: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="postalCode",
        title="Postal code for area",
        description="A postal code designating a region defined by the postal service.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    postalCode__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_postalCode", title="Extension field for ``postalCode``."
    )

    state: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="state",
        title="Sub-unit of country (abbreviations ok)",
        description=(
            "Sub-unit of a country with limited sovereignty in a federally "
            "organized country. A code may be used if codes are in common use (e.g."
            " US 2 letter state codes)."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    state__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_state", title="Extension field for ``state``."
    )

    text: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="text",
        title="Text representation of the address",
        description=(
            "Specifies the entire address as it should be displayed e.g. on a "
            "postal label. This may be provided instead of or as well as the "
            "specific parts."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    text__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_text", title="Extension field for ``text``."
    )

    type: fhirtypes.CodeType | None = Field(  # type: ignore
        default=None,
        alias="type",
        title="postal | physical | both",
        description=(
            "Distinguishes between physical addresses (those you can visit) and "
            "mailing addresses (e.g. PO Boxes and care-of addresses). Most "
            "addresses are both."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["postal", "physical", "both"],
        },
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_type", title="Extension field for ``type``."
    )

    use: fhirtypes.CodeType | None = Field(  # type: ignore
        default=None,
        alias="use",
        title="home | work | temp | old | billing - purpose of this address",
        description="The purpose of this address.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["home", "work", "temp", "old", "billing"],
        },
    )
    use__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_use", title="Extension field for ``use``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``Address`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "extension",
            "use",
            "type",
            "text",
            "line",
            "city",
            "district",
            "state",
            "postalCode",
            "country",
            "period",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``Address`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "use",
            "type",
            "text",
            "line",
            "city",
            "district",
            "state",
            "postalCode",
            "country",
            "period",
        ]
