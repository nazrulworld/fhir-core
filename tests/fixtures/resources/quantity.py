# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SimpleQuantity
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from pydantic import Field

from . import datatype, fhirtypes


class Quantity(datatype.DataType):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A measured or measurable amount.
    A measured amount (or an amount that can potentially be measured). Note
    that measured amounts include amounts that are not precisely quantified,
    including amounts involving arbitrary units and floating currencies.
    """

    __resource_type__ = "Quantity"

    code: fhirtypes.CodeType = Field(
        None,
        alias="code",
        title="Coded form of the unit",
        description=(
            "A computer processable form of the unit in some unit representation "
            "system."
        ),
        json_schema_extra={"element_property": True},
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_code", title="Extension field for ``code``."
    )

    comparator: fhirtypes.CodeType = Field(
        None,
        alias="comparator",
        title="< | <= | >= | > | ad - how to understand the value",
        description=(
            "How the value should be understood and represented - whether the "
            "actual value is greater or less than the stated value due to "
            'measurement issues; e.g. if the comparator is "<" , then the real '
            "value is < stated value."
        ),
        json_schema_extra={
            "element_property": True,
            "enum_values": ["\u003c", "\u003c=", "\u003e=", "\u003e", "ad"],
        },
    )
    comparator__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_comparator", title="Extension field for ``comparator``."
    )

    system: fhirtypes.UriType = Field(
        None,
        alias="system",
        title="System that defines coded unit form",
        description=(
            "The identification of the system that provides the coded form of the "
            "unit."
        ),
        json_schema_extra={"element_property": True},
        # if property is element of this resource.
    )
    system__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_system", title="Extension field for ``system``."
    )

    unit: fhirtypes.StringType = Field(
        None,
        alias="unit",
        title="Unit representation",
        description="A human-readable form of the unit.",
        # if property is an element of this resource.
        json_schema_extra={"element_property": True},
    )
    unit__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_unit", title="Extension field for ``unit``."
    )

    value: fhirtypes.DecimalType = Field(
        None,
        alias="value",
        title="Numerical value (with implicit precision)",
        description=(
            "The value of the measured amount. The value includes an implicit "
            "precision in the presentation of the value."
        ),
        # if property is element of this resource.
        json_schema_extra={"element_property": True},
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_value", title="Extension field for ``value``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``Quantity`` according to specification,
        with preserving the original sequence order.
        """
        return ["id", "extension", "value", "comparator", "unit", "system", "code"]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names from
        ``Quantity`` according to specification,
        with preserving the original sequence order.
        """
        return ["value", "comparator", "unit", "system", "code"]
