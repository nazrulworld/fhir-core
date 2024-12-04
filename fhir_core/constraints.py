import datetime
import decimal
import typing
import uuid

__author__ = "Md Nazrul Islam"
__email__ = "email2nazrul@gmail.com"

TYPES_ID_MAX_LENGTH = 255
TYPES_STRING_ALLOW_EMPTY_STR = False
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

FHIR_TYPES_MAPS: typing.Dict[str, str] = {}
FHIR_PRIMITIVES_MAPS: typing.Dict[typing.Any, str] = {
    str: "string",
    int: "integer",
    bool: "boolean",
    bytes: "base64Binary",
    bytearray: "base64Binary",
    float: "decimal",
    datetime.datetime: "dateTime",
    datetime.date: "date",
    datetime.time: "time",
    decimal.Decimal: "decimal",
    uuid.UUID: "uuid",
}

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
FHIR_PRIMITIVES = frozenset(
    [
        "boolean",
        "string",
        "base64Binary",
        "code",
        "id",
        "decimal",
        "integer",
        "integer64",
        "unsignedInt",
        "positiveInt",
        "uri",
        "oid",
        "uuid",
        "canonical",
        "url",
        "markdown",
        "xhtml",
        "date",
        "dateTime",
        "instant",
        "time",
    ]
)
