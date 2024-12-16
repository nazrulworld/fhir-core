import typing
from functools import lru_cache
from typing import get_args, get_origin

from pydantic._internal._validators import import_string
from pydantic.fields import FieldInfo
from pydantic.types import Base64Encoder, EncodedBytes

from .constraints import FHIR_PRIMITIVES_MAPS, FHIR_TYPES_MAPS, PY_PRIMITIVES

__author__ = "Md Nazrul Islam"
__email__ = "email2nazrul@gmail.com"


def _is_primitive_type(annotation: typing.Any) -> typing.Union[bool, None]:
    """ """
    origin = get_origin(annotation)
    if origin is None:
        if annotation in FHIR_PRIMITIVES_MAPS:
            return True

    args = get_args(annotation)
    for arg in args:
        if _is_primitive_type(arg) is not None:
            # check number of args
            return True
    return None


@lru_cache(maxsize=1024, typed=True)
def is_primitive_type(field: FieldInfo) -> bool:
    """ """
    return _is_primitive_type(field.annotation) is not None


def _is_list_type(annotation: typing.Any) -> typing.Union[bool, None]:
    """ """
    origin = get_origin(annotation)
    if origin is None:
        return annotation is list
    if origin is list:
        return True
    args = get_args(annotation)
    for arg in args:
        val = _is_list_type(arg)
        if val is not None:
            return val
    return None


@lru_cache(maxsize=1024, typed=True)
def is_list_type(field: FieldInfo) -> bool:
    """ """
    return _is_list_type(field.annotation) is True


def _get_fhir_type(annotation: typing.Any, field: FieldInfo):
    """ """

    def _get(anno):
        if anno in FHIR_PRIMITIVES_MAPS:
            if anno in PY_PRIMITIVES:
                for type_ in field.metadata:
                    if type_.__class__ in FHIR_PRIMITIVES_MAPS:
                        return type_.__class__
            return anno
        try:
            if anno.__name__ in FHIR_TYPES_MAPS:
                return anno.__name__
        except AttributeError:
            pass
        return None

    val = _get(annotation)
    if val is not None:
        return val

    origin = get_origin(annotation)
    if origin is None:
        return _get(annotation)

    args = get_args(annotation)
    for arg in args:
        val = _get_fhir_type(arg, field)
        if val is not None:
            # check number of args
            return val
    return None


def get_fhir_type_name(field: FieldInfo):
    """ """
    fhir_type = _get_fhir_type(field.annotation, field)
    if fhir_type is None:
        raise ValueError
    if fhir_type in FHIR_PRIMITIVES_MAPS:
        return FHIR_PRIMITIVES_MAPS[fhir_type]
    if fhir_type in FHIR_TYPES_MAPS:
        return import_string(FHIR_TYPES_MAPS[fhir_type]).get_resource_type()
    raise ValueError


@lru_cache(maxsize=1024, typed=True)
def get_base64_encoder(field_info: FieldInfo) -> typing.Any:
    """ """
    for enc in field_info.metadata:
        # handle base64 output
        if isinstance(enc, EncodedBytes):
            return enc
    if "Base64Binary" in str(field_info.annotation):
        return Base64Encoder


__all__ = [
    "is_primitive_type",
    "get_fhir_type_name",
    "is_list_type",
    "get_base64_encoder",
]
