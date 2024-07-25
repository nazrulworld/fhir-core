# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Annotation
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic.v1 import Field, root_validator
from pydantic.v1.error_wrappers import ErrorWrapper, ValidationError
from pydantic.v1.errors import MissingError, NoneIsNotAllowedError

from . import datatype, fhirtypes


class Annotation(datatype.DataType):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Text node with attribution.
    A  text note which also  contains information about who made the statement
    and when.
    """

    __resource_type__ = "Annotation"

    authorReference: fhirtypes.ReferenceType = Field(
        None,
        alias="authorReference",
        title="Individual responsible for the annotation",
        description="The individual responsible for making the annotation.",
        # if property is element of this resource.
        json_schema_extra={
            "element_property": True,
            "one_of_many": "author",
            "one_of_many_required": False,
            "enum_reference_types": [
                "Practitioner",
                "PractitionerRole",
                "Patient",
                "RelatedPerson",
                "Organization",
            ],
        },
    )

    authorString: fhirtypes.StringType = Field(
        None,
        alias="authorString",
        title="Individual responsible for the annotation",
        description="The individual responsible for making the annotation.",
        # if property is element of this resource.
        json_schema_extra={
            "element_property": True,
            "one_of_many": "author",
            "one_of_many_required": False,
        },
    )
    authorString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_authorString", title="Extension field for ``authorString``."
    )

    text: fhirtypes.MarkdownType = Field(
        None,
        alias="text",
        title="The annotation  - text content (as markdown)",
        description="The text of the annotation in markdown format.",
        # if property is element of this resource.
        json_schema_extra={"element_property": True, "element_required": True},
    )
    text__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_text", title="Extension field for ``text``."
    )

    time: fhirtypes.DateTimeType = Field(
        None,
        alias="time",
        title="When the annotation was made",
        description="Indicates when this particular annotation was made.",
        # if property is element of this resource.
        json_schema_extra={"element_property": True},
    )
    time__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_time", title="Extension field for ``time``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Annotation`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "authorReference", "authorString", "time", "text"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """ """
        return [("text", "text__ext")]

    def get_one_of_many_fields(self) -> typing.Dict[str, typing.List[str]]:
        """ """
        return {"author": ["authorReference", "authorString"]}
