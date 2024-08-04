=======
History
=======

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
