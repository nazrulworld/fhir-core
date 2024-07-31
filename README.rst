==========
FHIR® Core
==========

.. image:: https://img.shields.io/pypi/v/fhir-core.svg
        :target: https://pypi.python.org/pypi/fhir-core

.. image:: https://img.shields.io/pypi/pyversions/fhir-core.svg
        :target: https://pypi.python.org/pypi/fhir-core
        :alt: Supported Python Versions

.. image:: https://img.shields.io/travis/com/nazrulworld/fhir-core.svg
        :target: https://app.travis-ci.com/github/nazrulworld/fhir-core

.. image:: https://ci.appveyor.com/api/projects/status/1av308hpof6c9u5q?svg=true
        :target: https://ci.appveyor.com/project/nazrulworld/fhir-core
        :alt: Windows Build

.. image:: https://codecov.io/gh/nazrulworld/fhir.resources/branch/master/graph/badge.svg
        :target: https://codecov.io/gh/nazrulworld/fhir-core

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black

.. image:: https://static.pepy.tech/personalized-badge/fhir-core?period=total&units=international_system&left_color=black&right_color=green&left_text=Downloads
    :target: https://pepy.tech/project/fhir-core
    :alt: Downloads

.. image:: https://www.hl7.org/fhir/assets/images/fhir-logo-www.png
        :target: https://www.hl7.org/implement/standards/product_brief.cfm?product_id=449
        :alt: HL7® FHIR®

**Powered by Pydantic V2**. This library is developed for the support of the another libray `fhir.resources <https://github.com/nazrulworld/fhir.resources/>`_ but
you are more than welcome to use it for your own purpose. It provides an abstract base class for any FHIR resource model and `Primitive Datatypes <https://build.fhir.org/datatypes.html>`_
along with factories to create FHIR resource model and other complex datatypes.


Installation
------------

Just a simple ``pip install fhir-core``. But if you want development
version, just clone from https://github.com/nazrulworld/fhir-core and ``pip install -e .[dev]``.

Usages
------

**Example: 1**: This example creates an  Organization class with some of its attributes (id, active, name, address)::

    >>> from typing import List
    >>> from pydantic import Field
    >>> from fhir_core.fhirabstractmodel import FHIRAbstractModel
    >>> from fhir_core.types import IdType, BooleanType, StringType
    >>> data = {
    ...     "id": "f001",
    ...     "active": True,
    ...     "name": "Acme Corporation",
    ...     "address": ["Road 10": "Acme corporation", "2390", "USA"}]
    ... }
    >>> class Organization(FHIRAbstractModel):
    ...     __resource_type__ = "Organization"
    ...     id: IdType = Field(None, title="Id", alias="id", json_schema_extra={"element_property": True})
    ...     active: BooleanType = Field(None, title="Active", alias="active", json_schema_extra={"element_property": True})
    ...     name: StringType = Field(None, title="Name", alias="name", json_schema_extra={"element_property": True})
    ...     address: ListType[StringType] = Field(None, title="Address lines", alias="address", json_schema_extra={"element_property": True})
    ...
    ...     @classmethod
            def elements_sequence(cls):
                return ["id", "active", "name", "address"]
    ...
    >>> org = Organization.model_validate(data)
    >>> org.active is True
    True
    >>> org_json_str = org.model_dump_json()
    >>> Organization.model_validate_json(org_json_str).model_dump() == org.model_dump()
    True

**Complex examples**

    1. https://github.com/nazrulworld/fhir-core/blob/main/tests/fixtures/resources/extension.py
    2. https://github.com/nazrulworld/fhir-core/blob/main/tests/fixtures/resources/fhirtypes.py
    3. https://github.com/nazrulworld/fhir-core/blob/main/tests/fixtures/resources/codesystem.py

.. _`pydantic`: https://pydantic-docs.helpmanual.io/
.. _`FHIR`: https://www.hl7.org/implement/standards/product_brief.cfm

© Copyright HL7® logo, FHIR® logo and the flaming fire are registered trademarks
owned by `Health Level Seven International <https://www.hl7.org/legal/trademarks.cfm?ref=https://pypi.org/project/fhir-resources/>`_

.. role:: strike
    :class: strike
.. role:: raw-html(raw)
    :format: html
