import datetime
import decimal
import typing
import uuid
from functools import lru_cache
from typing import get_args, get_origin

from pydantic.fields import FieldInfo

try:
    import yaml

    HAS_YAML_SUPPORT = True
except ImportError:
    HAS_YAML_SUPPORT = False

try:
    import lxml

    HAS_XML_SUPPORT = True
except ImportError:
    HAS_XML_SUPPORT = False
__author__ = "Md Nazrul Islam"
__email__ = "email2nazrul@gmail.com"

PY_PRIMITIVES = frozenset(
    [
        str,
        int,
        bool,
        bytes,
        bytearray,
        float,
        datetime.datetime,
        datetime.date,
        datetime.time,
        decimal.Decimal,
        uuid.UUID,
    ]
)


def _is_primitive_type(annotation: typing.Any) -> typing.Union[bool, None]:
    """ """
    origin = get_origin(annotation)
    if origin is None:
        if annotation in PY_PRIMITIVES:
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


__all__ = ["is_primitive_type", "HAS_XML_SUPPORT", "HAS_YAML_SUPPORT"]
