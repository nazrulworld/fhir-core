# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Narrative
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""

from pydantic import Field

from . import datatype, fhirtypes


class Narrative(datatype.DataType):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Human-readable summary of the resource (essential clinical and business
    information).
    A human-readable summary of the resource conveying the essential clinical
    and business information for the resource.
    """

    __resource_type__ = "Narrative"

    div: fhirtypes.XhtmlType = Field(
        None,
        alias="div",
        title="Limited xhtml content",
        description="The actual narrative content, a stripped down version of XHTML.",
        # if property is element of this resource.
        json_schema_extra={"element_property": True, "element_required": True},
    )
    div__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_div", title="Extension field for ``div``."
    )

    status: fhirtypes.CodeType = Field(
        None,
        alias="status",
        title="generated | extensions | additional | empty",
        description=(
            "The status of the narrative - whether it's entirely generated (from "
            "just the defined data or the extensions too), or whether a human "
            "authored it and it may contain additional data."
        ),
        # if property is element of this resource.
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            "enum_values": ["generated", "extensions", "additional", "empty"],
        },
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Narrative`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "status", "div"]

    def get_required_fields(self):
        """ """
        return [("div", "div__ext"), ("status", "status__ext")]
