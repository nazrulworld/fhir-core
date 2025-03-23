=======
History
=======

1.0.1 (2025-03-23)
------------------

Fixes

- External issue https://github.com/nazrulworld/fhir.resources/issues/175


1.0.0 (2024-12-25)
------------------

- **XML serialization/deserialization support has been added**.

- Remove dependency on `typed-ast` as it is not needed and won't work in later Python versions.

- Fix typo in test case.

- Raising 'ValueError' has been suspended inside Fhir Model Validation 'fhir_model_validator()', if None value is provided.

0.1.3 (2024-10-24)
------------------

- Improves missing value validation message, as error type is now ``model_field_validation.missing``.


0.1.2 (2024-10-09)
------------------

- Improve validation error message.


0.1.1 (2024-10-09)
------------------

- Version policy updated, now `.bx` suffix has been removed.

Fixes

- Business logic for None type validation against FHIR Model validator as None value is acceptable! Instead, you should make Pydantic field optional.


0.1.0b9 (2024-10-02)
--------------------

Fixes

- Issue: AttributeError: 'NoneType' object has no attribute '__resource_type__' https://github.com/nazrulworld/fhir.resources/issues/164#issuecomment-2338404044


0.1.0b8 (2024-08-04)
--------------------

- YAML dump & validate options are added into FHIRAbstractModel.


0.1.0b7 (2024-07-31)
--------------------

- typing hint added for the function ´´create_fhir_type´´ and ´´create_fhir_element_or_resource_type´´.


0.1.0b6 (2024-07-30)
--------------------

- Core configurations for types ``Id`` & ``String`` are coming from constraint module.

- Default maximum char length ``Id`` is now 255.


0.1.0b5 (2024-07-28)
--------------------

- Fixes the function that is checking is_primitive, as missing bytes and bytesarray are added.

- Encoding is handled for Base64Binary type.


0.1.0b4 (2024-07-28)
--------------------

- Fixes extension serialization.


0.1.0b3 (2024-07-28)
--------------------

- Fixes the function that is checking is_primitive.

- Fixes validator for Resource & Element types.


0.1.0b2 (2024-07-27)
--------------------

Bugfixes

- Fixes pattern as string for some of primitives types. fx UriType.

- Fixes model serializer.


0.1.0b1 (2024-07-26)
--------------------

- The first beta release! and this release is not stable enough to use in production.
