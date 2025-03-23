#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

import platform

from setuptools import find_namespace_packages, setup

PY_VERSION_TUPLE = platform.python_version_tuple()
PY_VERSION_9_OR_EARLIER = PY_VERSION_TUPLE[0] == "3" and int(PY_VERSION_TUPLE[1]) <= 9
PY_VERSION_10_OR_LATER = PY_VERSION_TUPLE[0] == "3" and int(PY_VERSION_TUPLE[1]) >= 10
PY_VERSION_11_OR_LATER = PY_VERSION_10_OR_LATER and int(PY_VERSION_TUPLE[1]) >= 11

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = ["pydantic>=2.7.4,<3.0"]
if PY_VERSION_9_OR_EARLIER:
    requirements.append("eval-type-backport")

setup_requirements = ["pytest-runner"]

test_requirements = [
    "coverage",
    "pytest>5.4.0;python_version>='3.6'",
    "pytest-cov>=2.10.0;python_version>='3.6'",
    "flake8" + (PY_VERSION_10_OR_LATER and "==6.0" or "==5.0.4;python_version<'3.10'"),
    "flake8-isort"
    + (PY_VERSION_10_OR_LATER and ">=6.0.0" or "==4.2.0;python_version<'3.10'"),
    "flake8-bugbear"
    + (PY_VERSION_10_OR_LATER and ">=22.12.6" or "==20.1.4;python_version<'3.10'"),
    "requests==2.23.0;python_version<'3.10'",
    "isort" + (PY_VERSION_10_OR_LATER and ">=5.11.4" or "==4.3.21"),
    "black",
    "mypy",
    "PyYAML>=6.0.1",
    "types-PyYAML",
    "types-simplejson",
    "types-requests",
    "setuptools==65.6.3;python_version>='3.7'",
    "lxml",
]
if PY_VERSION_10_OR_LATER:
    test_requirements.append("importlib-metadata>=5.2.0")

development_requirements = [
    "Jinja2==2.11.1",
    "MarkupSafe==1.1.1",
    "colorlog==2.10.0",
    "certifi",
    "fhirspec",
    "zest-releaser[recommended]",
]
setup(
    author="Md Nazrul Islam",
    author_email="email2nazrul@gmail.com",
    # Get more from https://pypi.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Typing :: Typed",
    ],
    description="FHIR Core library",
    install_requires=requirements,
    license="BSD license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="fhir, core, resources, python, hl7, health IT, healthcare",
    name="fhir_core",
    packages=find_namespace_packages(
        include=["fhir_core"],
        exclude=["ez_setup", "tests"],
    ),
    package_data={"fhir_core": ["py.typed"]},
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    extras_require={
        "test": (test_requirements + setup_requirements),
        "dev": (test_requirements + development_requirements),
    },
    url="https://github.com/nazrulworld/fhir-core",
    version="1.0.0.dev0",
    zip_safe=False,
    python_requires=">=3.8",
    project_urls={
        "CI: Travis": "https://travis-ci.org/github/nazrulworld/fhir-core",
        "Coverage: codecov": "https://codecov.io/gh/nazrulworld/fhir-core",
        "GitHub: issues": "https://github.com/nazrulworld/fhir-core/issues",
        "GitHub: repo": "https://github.com/nazrulworld/fhir-core",
    },
)
