from __future__ import annotations as _annotations

"""XML Utilities"""
import datetime
import decimal
import importlib
import logging
import typing
import uuid
from collections import OrderedDict, deque
from copy import copy
from functools import lru_cache
from pathlib import Path
from types import ModuleType

from lxml import etree  # type: ignore
from lxml.etree import QName  # type: ignore
from pydantic.fields import FieldInfo
from pydantic_core._pydantic_core import Url

from .utils import (
    get_base64_encoder,
    get_fhir_type_name,
    is_list_type,
    is_primitive_type,
)

if typing.TYPE_CHECKING:
    from .fhirabstractmodel import FHIRAbstractModel

__author__ = "Md Nazrul Islam"
__email__ = "email2nazrul@gmail.com"

StrBytes = typing.Union[str, bytes]
StrNone = typing.Union[str, None]
StrBytesNone = typing.Union[str, bytes, None]
DictStr = typing.Dict[str, str]
DictStrBytes = typing.Dict[str, StrBytes]
DictStrNoneKey = typing.Dict[typing.Union[str, None], str]
DictStrBytesNoneKey = typing.Dict[StrNone, StrBytes]
TupleStrKeyVal = typing.Tuple[str, StrBytes]
ROOT_NS = "http://hl7.org/fhir"
XHTML_NS = "http://www.w3.org/1999/xhtml"
EMPTY_VALUE = None
LOG = logging.getLogger(__name__)


def first_cap(string: str):
    """ """
    return string[0].upper() + string[1:]


def xml_represent(type_, val):
    """XML  Representation"""
    if val is None:
        return val
    type_name = get_fhir_type_name(type_)
    if type_name == "boolean":
        return val is True and "true" or "false"

    if type_name in (
        "string",
        "code",
        "id",
        "markdown",
        "xhtml",
        "oid",
        "canonical",
        "uri",
    ):
        if isinstance(val, bytes):
            val = val.decode("utf-8")
        return val

    if type_name in ("decimal", "integer", "integer64", "unsignedInt", "positiveInt"):
        if isinstance(val, decimal.Decimal):
            val = float(val)
        return str(val)
    if type_name in "base64Binary":
        encoder = get_base64_encoder(type_)
        if encoder is not None:
            val = encoder.encode(val)
        if isinstance(val, bytes):
            val = val.decode("utf-8")
        return val

    if type_name == "date":
        """ """
        if isinstance(val, str):
            return val
        if isinstance(val, datetime.datetime):
            val = val.date()
        if isinstance(val, datetime.date):
            val = val.isoformat()
        return val

    if type_name == "dateTime":
        if isinstance(val, str):
            return val
        if isinstance(val, datetime.datetime):
            return val.isoformat()

    if type_name == "time":
        if isinstance(val, datetime.time):
            val = val.isoformat()
        return val

    if type_name == "instant":
        if isinstance(val, datetime.datetime):
            val = val.isoformat()
        return val

    if type_name == "url":
        if isinstance(val, Url):
            val = str(val)
        return val

    if type_name == "uuid":
        """ """
        if isinstance(val, uuid.UUID):
            val = f"urn:uuid:{str(val)}"
        if not val.startswith("urn:uuid:"):
            val = f"urn:uuid:{val}"
        return val

    raise NotImplementedError


@lru_cache(maxsize=None, typed=True)
def get_fhir_root_module(klass_module: str):
    """ """
    mod_ = ".".join(klass_module.split(".")[:-1])
    return importlib.import_module(mod_)


class SimpleNodeStorage:
    __slots__ = ("__storage__", "node")
    if typing.TYPE_CHECKING:
        node: "Node"
        __storage__: deque

    def __init__(self, node):
        """ """
        assert isinstance(node, Node)
        object.__setattr__(self, "node", node)
        object.__setattr__(self, "__storage__", deque())

    def __iter__(self):
        """ """
        return iter(self.__storage__)

    def __getitem__(self, index):
        """ """
        return self.__storage__[index]

    def __len__(self):
        """ """
        return len(self.__storage__)

    def append(self, item):
        """ """
        self.__storage__.append(item)

    def extend(self, items):
        """ """
        self.__storage__.extend(items)

    def as_list(self):
        """ """
        return list(self.__storage__)


class NodeContainer(SimpleNodeStorage):
    """ """

    def __init__(self, node):
        """ """
        super(NodeContainer, self).__init__(node)

    def append(self, item):
        """ """
        assert isinstance(item, (Node, etree._Element))
        SimpleNodeStorage.append(self, item)

    def extend(self, items):
        """ """
        if not all([isinstance(i, (Node, etree._Element)) for i in items]):
            raise ValueError("value must be instance of ``Node``")
        SimpleNodeStorage.extend(self, items)


class AttributeContainer(SimpleNodeStorage):
    """ """

    def __init__(self, node: "Node"):
        """ """
        super(AttributeContainer, self).__init__(node)

    def append(self, item: "Attribute"):
        """ """
        assert isinstance(item, Attribute)
        if (
            len(self.node._allowed_attrs) > 0
            and item.name not in self.node._allowed_attrs
        ):
            raise ValueError(f"'{item.name}' is not allowed attribute.")
        SimpleNodeStorage.append(self, item)

    def extend(self, items: typing.List["Attribute"]):
        """ """
        if not all([isinstance(i, Attribute) for i in items]):
            raise ValueError("value must be instance of ``fhirxml.Attribute``")
        for item in items:
            if (
                len(self.node._allowed_attrs) > 0
                and item.name not in self.node._allowed_attrs
            ):
                raise ValueError(f"'{item.name}' is not allowed attribute.")

        SimpleNodeStorage.extend(self, items)


class NamespaceContainer(SimpleNodeStorage):
    """ """

    def __init__(self, node: "Node"):
        """ """
        super(NamespaceContainer, self).__init__(node)

    def append(self, item: "Namespace"):
        """ """
        assert isinstance(item, Namespace)
        SimpleNodeStorage.append(self, item)

    def extend(self, items: typing.List["Namespace"]):
        """ """
        if not all([isinstance(i, Namespace) for i in items]):
            raise ValueError("value must be instance of fhirxml.Namespace")
        SimpleNodeStorage.extend(self, items)


class CommentContainer(SimpleNodeStorage):
    """ """

    def __init__(self, node: "Node"):
        """ """
        super(CommentContainer, self).__init__(node)

    def append(self, item: "Comment"):
        """ """
        assert isinstance(item, Comment)
        SimpleNodeStorage.append(self, item)

    def extend(self, items: typing.List["Comment"]):
        """ """
        if not all([isinstance(i, Comment) for i in items]):
            raise ValueError("value must be instance of fhirxml.Comment")
        SimpleNodeStorage.extend(self, items)


class AttributeValue:
    """ """

    def __init__(self, raw: StrBytes, quote: bool = False):
        """ """
        if isinstance(raw, bytes):
            raw = raw.decode()
        self.raw: str = raw
        self.quote = quote

    def to_xml(self) -> str:
        """ """
        val = self.raw
        if self.quote:
            val = "'{0}'".format(val)
        return val

    def __str__(self):
        return self.to_xml()

    @typing.no_type_check
    def __eq__(self, other: "AttributeValue"):
        """ """
        return (self.raw == other.raw) and (self.quote == other.quote)


class Attribute:
    """ """

    def __init__(
        self,
        name: typing.Union[str, QName],
        value: typing.Union[StrBytes, AttributeValue, None],
    ):
        """ """
        self.name: typing.Union[str, QName] = name
        if typing.TYPE_CHECKING:
            self.value: typing.Union[StrBytes, AttributeValue, None]
        if isinstance(value, (AttributeValue, str)):
            self.value = value
        else:
            if isinstance(value, bytes):
                value = value.decode()
            self.value = value

    def __str__(self):
        """ """
        return '{0}="{1}"'.format(*self.to_xml())

    def to_xml(self) -> typing.Tuple[str, StrNone]:
        """ """
        val: typing.Optional[str] = None

        if isinstance(self.value, AttributeValue):
            val = self.value.to_xml()
        elif self.value is not None:
            val = typing.cast(str, self.value)

        return self.name, val

    def __repr__(self):
        """ """
        return f"<{self.__class__.__name__} {self.__str__()}>"

    @typing.no_type_check
    def __eq__(self, other: "Attribute"):
        """ """
        return (self.name == other.name) and (self.value == other.value)


class Namespace:
    """ """

    def __init__(self, name: StrNone, location: StrBytes):
        """ """
        self.name: StrNone = name
        if isinstance(location, bytes):
            location = location.decode()
        self.location = location

    def __str__(self):
        """ """
        name = ""
        if self.name:
            name = f":{self.name}"
        return 'xmlns{0}="{1}"'.format(name, self.location)

    def to_xml(self):
        """ """
        return self.name, self.location

    def __repr__(self):
        """ """
        return "<{0} {1}>".format(self.__class__.__name__, self.__str__())

    @typing.no_type_check
    def __eq__(self, other: "Namespace"):
        """ """
        return (self.name == other.name) and (self.location == other.location)


class Comment:
    """XML/Node comment"""

    __slots__ = ("_text",)

    def __init__(self, comment: StrBytes):
        """ """
        if isinstance(comment, str):
            comment = comment.encode()
        self._text: bytes = comment

    def to_xml(self) -> etree._Comment:
        """ """
        return etree.Comment(self._text)

    def to_string(self) -> str:
        return self._text.decode()

    @classmethod
    def from_element(cls, element: etree._Comment) -> "Comment":
        """ """
        return cls(element.text)

    def __str__(self):
        return self.to_string()


class Node:
    """ """

    _allowed_attrs: typing.Set[str] = set()

    def __init__(
        self,
        name: typing.Union[str, QName],
        *,
        value: typing.Optional[StrBytes] = None,
        text: typing.Union[StrBytes, "Node", None] = None,
        attributes: typing.Optional[typing.List[Attribute]] = None,
        namespaces: typing.Optional[typing.List[Namespace]] = None,
        comments: typing.Optional[typing.List[Comment]] = None,
        parent: typing.Optional["Node"] = None,
        children: typing.Optional[typing.List["Node"]] = None,
    ):
        """ """
        self.name = name
        self._value = None
        self._text = None
        self.attributes = AttributeContainer(self)
        self.namespaces = NamespaceContainer(self)
        self.comments = CommentContainer(self)
        self.parent = None
        self.children = NodeContainer(self)

        if text:
            self.set_text(text)
        if value:
            self.value = value

        if attributes:
            self.attributes.extend(attributes)
        if namespaces:
            self.namespaces.extend(namespaces)
        if comments:
            self.comments.extend(comments)
        if parent:
            assert isinstance(parent, Node)
            self.parent = parent
        if children:
            self.children.extend(children)

    def rename(self, new_name):
        """Rename the current Node name"""
        if self.name == new_name:
            raise ValueError("Current Node name and provided name are identical!")
        self.name = new_name

    def add_namespace(
        self,
        ns: typing.Union[Namespace, StrNone],
        location: typing.Optional[StrBytes] = None,
    ):
        """ """
        if isinstance(ns, Namespace):
            self.namespaces.append(ns)
            return
        if location is None:
            raise ValueError("'location' value is required.")

        self.namespaces.append(Namespace(ns, location))

    def add_attribute(
        self,
        attr: typing.Union[str, Attribute],
        value: typing.Optional[StrBytes] = None,
    ):
        """ """
        if isinstance(attr, Attribute):
            self.attributes.append(attr)
            return
        self.attributes.append(Attribute(attr, value))

    @property
    def text(self):
        """ """
        return self._text

    @text.setter
    def text(self, val):
        """ """
        self._text = val

    @property
    def value(self):
        """ """
        return self._value

    @value.setter
    def value(self, val):
        """ """
        self._value = val

    def set_text(self, value):
        """ """
        if isinstance(value, Node):
            value = value.to_string(pretty_print=False, xml_declaration=False)
        self._text = value

    def add_text(self, value, prefix="", suffix=""):
        """ """
        if isinstance(value, Node):
            value = value.to_string(pretty_print=False, xml_declaration=False)
        if not isinstance(value, str):
            if isinstance(value, bytes):
                value = value.decode()
            else:
                value = str(value)

        value = prefix + value + suffix
        if not self._text:
            self._text = ""
        self._text += value

    @classmethod
    def create(
        cls,
        name,
        *,
        value: typing.Union[str, bytes, None] = None,
        text: typing.Union[typing.Union[str, bytes], "Node", None] = None,
        attrs: typing.Union[
            DictStrBytes,
            typing.List[typing.Union[Attribute, typing.Tuple[str, StrBytes]]],
            None,
        ] = None,
        namespaces: typing.Union[
            DictStrBytesNoneKey,
            typing.List[typing.Union[Namespace, typing.Tuple[StrNone, StrBytes]]],
            None,
        ] = None,
    ):
        """ """
        self = cls(name=name, value=value, text=text)

        if attrs:
            if isinstance(attrs, dict):
                attrs = list(attrs.items())
            if isinstance(attrs, list):
                for attr in attrs:
                    if isinstance(attr, tuple):
                        self.add_attribute(*attr)
                    else:
                        self.add_attribute(attr)
            else:
                raise NotImplementedError

        if namespaces:
            if isinstance(namespaces, dict):
                namespaces = list(namespaces.items())

            if isinstance(namespaces, list):
                for ns in namespaces:
                    if isinstance(ns, tuple):
                        self.add_namespace(*ns)
                    else:
                        self.add_namespace(ns)
            else:
                raise NotImplementedError

        return self

    @staticmethod
    def clean_tag(element: etree._Element) -> str:
        """Clean tag name from namespace"""
        return QName(element.tag).localname

    @classmethod
    def from_element(
        cls,
        element: etree._Element,
        parent: typing.Optional["Node"] = None,
        exists_ns: typing.Optional[typing.List[Namespace]] = None,
        comments: typing.Optional[typing.List[Comment]] = None,
    ):
        """ """
        name = Node.clean_tag(element)
        me = cls(name)
        if element.text:
            me.text = element.text
        # Attributes
        for attr, value in element.attrib.items():
            if attr == "value":
                me.value = value
            else:
                me.add_attribute(attr, value)

        if exists_ns is None:
            exists_ns = []

        if parent is not None:
            exists_ns += parent.namespaces.as_list()

        # handle namespaces
        for prefix, location in element.nsmap.items():
            ns = Namespace(prefix, location)
            if ns in exists_ns:
                continue
            me.namespaces.append(ns)
            exists_ns.append(ns)

        # handle comments
        if comments:
            me.comments.extend(comments)

        # potential comments for children
        child_comments: typing.Optional[typing.List[Comment]] = None
        for child in element:
            if isinstance(child, etree._Comment):
                if child_comments is None:
                    child_comments = list()
                child_comments.append(Comment.from_element(child))
                continue

            if child.nsmap[None] == XHTML_NS:
                me.children.append(child)
                continue
            child_name = Node.clean_tag(child)
            child_class = globals().get(child_name, Node)
            child_class.from_element(
                child, parent=me, exists_ns=copy(exists_ns), comments=child_comments
            )
            # reset
            child_comments = None

        if parent is not None:
            parent.children.append(me)

        return me

    @staticmethod
    def inject_comments(
        node: "Node", comments: typing.Union[str, typing.List[str]]
    ) -> None:
        """working comments"""
        if comments is None:
            return
        if comments:
            if isinstance(comments, str):
                comments = [comments]
            for cm in comments:
                node.children.append(etree.Comment(cm))

    @staticmethod
    def add_fhir_element(
        parent: "Node", field: FieldInfo, value: typing.Any, ext=None, ext_field=None
    ):
        """"""
        child = Node.create(field.alias)
        if is_primitive_type(field):
            if isinstance(value, list):
                if ext and not isinstance(ext, list):
                    ext = [ext]

                if ext is None:
                    ext = []

                if len(value) < len(ext):
                    LOG.warning(
                        f"Some {(len(ext) - len(value))} extension(s) are ignored."
                    )

                for idx, val in enumerate(value):
                    try:
                        ext_ = ext[idx]
                    except IndexError:
                        ext_ = None
                    if ext_ is None and val is None:
                        continue
                    Node.add_fhir_element(
                        parent,
                        field,
                        value=val,
                        ext=ext_,
                        ext_field=ext_field,
                    )
            elif value is not None:
                child.value = xml_represent(field, value)
                if ext is not None:
                    Node.inject_comments(
                        parent, ext.__dict__.get("fhir_comments", None)
                    )
                    Node.add_fhir_element(
                        child,
                        field=ext_field,
                        value=ext,
                        ext=None,
                        ext_field=None,
                    )
                parent.children.append(child)
            else:
                child.value = EMPTY_VALUE
                if ext is not None:
                    exts = not isinstance(ext, list) and [ext] or ext
                    for ext_ in exts:
                        if ext_ is None:
                            continue
                        Node.inject_comments(
                            parent, ext_.__dict__.get("fhir_comments", None)
                        )
                        Node.add_fhir_element(
                            child,
                            field=ext_field,
                            value=ext_,
                            ext=None,
                            ext_field=None,
                        )
                parent.children.append(child)
            return

        # Handle Multiple non primitive type values
        if isinstance(value, list):
            for value_ in value:
                Node.add_fhir_element(
                    parent,
                    field,
                    value_,
                    ext=ext,
                    ext_field=ext_field,
                )
            return
        # we see it's instance of 'FHIRAbstractModel'
        parent_child = None
        fhir_type_name = get_fhir_type_name(field)
        if fhir_type_name == "Resource":
            # special case
            parent_child = child
            child = Node.create(value.get_resource_type())
            parent_child.children.append(child)

        if fhir_type_name == "FHIRPrimitiveExtension":
            # this is a special primitive extension
            del child
            # xxx: handle comments (add comment to main element, parent in this case)
            field = value.model_fields["extension"]
            value = value.__dict__.get(field.alias, None)
            if not value:
                return
            Node.add_fhir_element(
                parent,
                field,
                value,
                ext=ext,
                ext_field=ext_field,
            )
            return
        # working comments
        comments = value.__dict__.get("fhir_comments", None)
        Node.inject_comments(parent, comments)

        alias_maps = value.__class__.get_alias_mapping()
        for prop_name in value.__class__.elements_sequence():
            field_ = value.__class__.model_fields[alias_maps[prop_name]]
            val = value.__dict__.get(field_.alias)
            if fhir_type_name == "Extension" and field_.alias in ("url", "id") and val:
                child.add_attribute(field_.alias, val)
                continue
            if get_fhir_type_name(field_) == "xhtml" and val:
                # xxx: fhir-xhtml.xsd validation
                xhtml_element = etree.fromstring(val)
                if not (
                    xhtml_element.nsmap[None] == XHTML_NS
                    and str(etree.QName(XHTML_NS, field_.alias))
                ):
                    raise ValueError
                else:
                    child.children.append(xhtml_element)
                    continue

            value_ext, value_ext_field = None, None
            if is_primitive_type(field_):
                ext_key = f"{alias_maps[field_.alias]}__ext"
                value_ext = value.__dict__.get(ext_key, None)
                if value_ext:
                    value_ext_field = value.__class__.model_fields[ext_key]

            if value_ext is None and val is None:
                continue

            Node.add_fhir_element(
                child,
                field_,
                val,
                ext=value_ext,
                ext_field=value_ext_field,
            )
        if parent_child is None:
            parent.children.append(child)
        else:
            parent.children.append(parent_child)

    @classmethod
    def from_fhir_obj(cls, model: "FHIRAbstractModel"):
        """ """
        resource_node = cls(
            model.get_resource_type(), namespaces=[Namespace(None, ROOT_NS)]
        )
        alias_maps = model.__class__.get_alias_mapping()
        for prop_name in model.__class__.elements_sequence():
            field = model.__class__.model_fields[alias_maps[prop_name]]
            if typing.TYPE_CHECKING:
                assert field.alias
            value = model.__dict__.get(field.alias, None)
            value_ext, value_ext_field = None, None
            if is_primitive_type(field):
                ext_key = f"{field.alias}__ext"
                value_ext = model.__dict__.get(ext_key, None)
                if value_ext:
                    value_ext_field = model.__class__.model_fields[ext_key]

            if value_ext is None and value is None:
                continue

            Node.add_fhir_element(
                resource_node,
                field,
                value,
                ext=value_ext,
                ext_field=value_ext_field,
            )

        return resource_node

    def to_xml(self, parent: etree._Element = None):
        """ """
        params = {}
        nsmap = self.normalize_namespaces()
        if len(nsmap) > 0:
            params["nsmap"] = nsmap

        attrib = self.normalize_attributes()
        if len(attrib) > 0:
            params["attrib"] = attrib
        if self.value:
            params["value"] = (
                isinstance(self.value, AttributeValue)
                and self.value.to_xml()
                or self.value
            )

        if parent is None:
            # xxx: fix own comments
            me = etree.Element(self.name, **params)

        else:
            # handle comments
            if len(self.comments) > 0:
                parent.extend([c.to_xml() for c in self.comments])

            me = parent.makeelement(self.name, **params)

        if self.text:
            me.text = (
                isinstance(self.text, AttributeValue)
                and self.text.to_xml()
                or self.text
            )

        if len(self.children) == 0:
            return me

        for child in self.children:
            if isinstance(child, Node):
                child_node = child.to_xml(me)
            elif isinstance(child, etree._Element):
                child_node = child
            elif isinstance(child, (str, bytes)):
                child_node = etree.fromstring(child)
            else:
                raise NotImplementedError

            me.append(child_node)

        return me

    def normalize_attributes(self):
        """ """
        attrib = OrderedDict()
        for attr in self.attributes:
            key, val = attr.to_xml()
            attrib[key] = val
        return attrib

    def normalize_namespaces(self):
        """ """
        nsmap = OrderedDict()
        for ns in self.namespaces:
            key, val = ns.to_xml()
            nsmap[key] = val
        return nsmap

    @classmethod
    def validate(
        cls,
        element: typing.Union["Node", etree._Element, bytes],
        xsd_file: typing.Optional[Path] = None,
        xmlparser: typing.Optional[etree.XMLParser] = None,
    ):
        """ """
        if isinstance(element, cls):
            element_str = element.to_string(pretty_print=False)
        elif isinstance(element, etree._Element):
            element_str = etree.tostring(element)
        else:
            element_str = element
        if xmlparser is None and xsd_file is None:
            raise ValueError("Any of `xsd_file` or `parser` is required")

        if xmlparser is None:
            assert xsd_file and xsd_file.exists() and xsd_file.is_file()
            schema = etree.XMLSchema(file=str(xsd_file))
            xmlparser = etree.XMLParser(schema=schema)

        try:
            etree.fromstring(element_str, parser=xmlparser)
        except (etree.XMLSchemaError, etree.XMLSyntaxError) as exc:
            raise ValueError(str(exc))

    def to_string(
        self,
        pretty_print=False,
        xml_declaration=True,
        with_comments=True,
        strip_text=False,
    ):
        """ """
        el = self.to_xml()
        params = {"encoding": "utf-8", "method": "xml", "pretty_print": pretty_print}
        if xml_declaration:
            params["xml_declaration"] = '<?xml version="1.0" encoding="UTF-8"?>'
        params["with_comments"] = with_comments
        params["strip_text"] = strip_text

        return etree.tostring(el, **params)

    @staticmethod
    def get_fhir_value(
        obj: typing.Union["Node", etree._Element],
        field: "FieldInfo",
        root_mod: ModuleType,
    ) -> typing.Any:
        """ """
        if is_primitive_type(field):
            type_name = get_fhir_type_name(field)
            if type_name == "xhtml":
                if isinstance(obj, etree._Element):
                    value = etree.tostring(obj)
                else:
                    # we assume Node
                    value = obj.to_string(pretty_print=False, xml_declaration=False)
                return value

            value = obj.value

            if type_name == "uuid":
                if value.startswith("urn:uuid:"):
                    value = value[len("urn:uuid:") :]

        else:
            klass_ = root_mod.get_fhir_model_class(get_fhir_type_name(field))
            # field.shape
            value = obj.to_fhir(klass_, root_mod)

        return value

    def to_fhir(
        self, klass: typing.Type["FHIRAbstractModel"], root_mod: ModuleType = None
    ) -> "FHIRAbstractModel":
        """ """
        root_mod = root_mod or get_fhir_root_module(klass.__module__)
        if klass.get_resource_type() == "Resource" and len(self.children) > 0:
            # tiny hack to get FHIR release
            child = self.children[0]
            klass_ = root_mod.get_fhir_model_class(child.name)
            return child.to_fhir(klass_, root_mod)

        params: typing.Dict[str, typing.Any] = {
            "resource_type": klass.get_resource_type()
        }
        alias_maps = klass.get_alias_mapping()
        primitive_ext_list_values: typing.Dict[str, typing.Any] = {}
        if len(self.comments) > 0:
            comments = [c.to_string() for c in self.comments]
            if len(comments) == 1:
                params["fhir_comments"] = comments[0]
            else:
                params["fhir_comments"] = comments

        if klass.get_resource_type() == "Extension":
            for attribute in self.attributes:
                name, val = attribute.to_xml()
                params[name] = val

        for child in self.children:
            if isinstance(child, etree._Element):
                field_name = Node.clean_tag(child)
            else:
                field_name = child.name
            # important!
            field_name = alias_maps[field_name]
            field = klass.model_fields[field_name]
            is_list = is_list_type(field)

            value = Node.get_fhir_value(child, field, root_mod)

            if is_list:
                if field_name not in params:
                    params[field_name] = list()
                params[field_name].append(value)
            else:
                # xxx: handle None
                params[field_name] = value

            if (
                is_primitive_type(field)
                and isinstance(child, Node)
                and (len(child.children) > 0 or len(child.comments) > 0)
            ):
                ext_field_name = f"{field_name}__ext"
                primitive_ext_klass = root_mod.get_fhir_model_class(
                    "FHIRPrimitiveExtension"
                )
                ext_klass = root_mod.get_fhir_model_class(
                    get_fhir_type_name(primitive_ext_klass.model_fields["extension"])
                )
                primitive_ext_params = {}
                if len(child.comments) > 0:
                    p_ext_comments = [c.to_string() for c in child.comments]
                    if len(p_ext_comments) == 1:
                        primitive_ext_params["fhir_comments"] = p_ext_comments[0]
                    else:
                        primitive_ext_params["fhir_comments"] = p_ext_comments

                if len(child.children) > 0:
                    primitive_ext_params["extension"] = list()
                    for child_ in child.children:
                        primitive_ext_params["extension"].append(
                            child_.to_fhir(ext_klass, root_mod)
                        )

                primitive_ext = primitive_ext_klass(**primitive_ext_params)
                if is_list:
                    # special case
                    if ext_field_name not in primitive_ext_list_values:
                        primitive_ext_list_values[ext_field_name] = {}
                    primitive_ext_list_values[ext_field_name][
                        len(params[field_name]) - 1
                    ] = primitive_ext
                else:
                    params[ext_field_name] = primitive_ext

            if is_list and (
                len(params[field_name]) == 0
                or all([v is None for v in params[field_name]])
            ):
                del params[field_name]

        # treatment for list type primitive ext
        for p_ext_name in primitive_ext_list_values:
            exts = []
            for idx in range(len(params[p_ext_name[:-5]])):
                try:
                    exts.append(primitive_ext_list_values[p_ext_name][idx])
                except KeyError:
                    exts.append(None)
            params[p_ext_name] = exts

        return klass(**params)

    def __str__(self):
        """ """
        return self.to_string(pretty_print=False)


def xml_dumps(
    model: "FHIRAbstractModel",
    *,
    pretty_print=False,
    xml_declaration=True,
    with_comments=True,
    strip_text=False,
):
    """ """
    node = Node.from_fhir_obj(model)
    return node.to_string(
        pretty_print=pretty_print,
        xml_declaration=xml_declaration,
        with_comments=with_comments,
        strip_text=strip_text,
    )


def xml_loads(
    cls: typing.Type["FHIRAbstractModel"],
    b: str | bytes | bytearray,
    xmlparser: etree.XMLParser = None,
) -> "FHIRAbstractModel":
    """ """
    root = etree.fromstring(b, parser=xmlparser)
    node = Node.from_element(root)
    return node.to_fhir(cls)


__all__ = ["xml_dumps", "xml_loads"]
