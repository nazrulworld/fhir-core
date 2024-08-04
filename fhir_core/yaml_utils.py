from collections import OrderedDict
from datetime import datetime
from decimal import Decimal

from pydantic_core._pydantic_core import Url
from yaml import Node, ScalarNode, YAMLError, dump, load
from yaml.representer import Representer as BaseRepresenter
from yaml.representer import SafeRepresenter

try:
    from yaml import CDumper as Dumper
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Dumper, Loader  # type: ignore


__all__ = ["yaml_loads", "yaml_dumps"]

__author__ = "Md Nazrul Islam"
__email__ = "email2nazrul@gmail.com"


class Representer(SafeRepresenter):
    """ """

    def represent_decimal(self, data: Decimal) -> Node:
        """ """
        coerced = float(data)
        return self.represent_float(coerced)

    def represent_datetime(self, data: datetime) -> ScalarNode:
        """Issue #96, we are using T separator for ISO format"""
        value = data.isoformat(sep="T")
        return self.represent_scalar("tag:yaml.org,2002:timestamp", value)

    def represent_url(self, data: Url) -> Node:
        """!!python/object/new:pydantic_core._pydantic_core.Url"""
        coerced = str(data)
        return self.represent_str(coerced)


BaseRepresenter.add_representer(
    Decimal, Representer.represent_decimal  # type: ignore[arg-type]
)
# important! we don't want explicit tag of OrderedDict
# (tag:yaml.org,2002:python/object/apply:collections.OrderedDict)
BaseRepresenter.add_representer(OrderedDict, SafeRepresenter.represent_dict)
BaseRepresenter.add_representer(
    datetime, Representer.represent_datetime  # type: ignore[arg-type]
)
BaseRepresenter.add_representer(
    Url, Representer.represent_url  # type: ignore[arg-type]
)


def yaml_loads(stream, loader=None):
    """ """
    loader = loader or Loader
    try:
        return load(stream, Loader=loader)
    except YAMLError as exc:
        # ensure Pydantic compatible error handling
        raise ValueError(f"YAMLError: {exc}")


def yaml_dumps(
    data,
    *,
    stream=None,
    indent=None,
    width=None,
    line_break=None,
    sort_keys=False,
    encoding="utf-8",
    return_bytes=True,
):
    """ """
    try:
        res = dump(
            data,
            stream=stream,
            Dumper=Dumper,
            indent=indent,
            width=width,
            line_break=line_break,
            sort_keys=sort_keys,
            encoding=encoding,
        )
    except YAMLError as exc:
        # ensure Pydantic compatible error handling
        raise ValueError(f"YAMLError: {exc}")

    if stream is None and return_bytes is False:
        res = res.decode()

    return res
