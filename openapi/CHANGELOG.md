# Changelog

## [1.2.0](https://github.com/exalsius/exalsius-api-spec/compare/openapi-v1.1.6...openapi-v1.2.0) (2025-05-28)


### Features

* add ClusterAddNodeRequest model ([27bb895](https://github.com/exalsius/exalsius-api-spec/commit/27bb895494e0deeb4e2c8611ced12e2bfdd726e1))


### Bug Fixes

* add 409 conflict response when cluster already exists ([a00ce5d](https://github.com/exalsius/exalsius-api-spec/commit/a00ce5dfe863a14c6588ea70aa424d4a51756b4b))
* add a ClusterDelete response model ([28bbe86](https://github.com/exalsius/exalsius-api-spec/commit/28bbe860d32d17099b13b53b05139bdaccb299ec))
* adjust the ClusterNodeResponse schema ([5dfb3bc](https://github.com/exalsius/exalsius-api-spec/commit/5dfb3bcdbe892c1d725efeaee505a14bfefb6181))
* change cluster_id format to string for delete_node request param ([8b94967](https://github.com/exalsius/exalsius-api-spec/commit/8b9496716ba94ba7ba2ef381d1a9761cc90d072c))
* change cluster_id format to uuid strings ([c8396ca](https://github.com/exalsius/exalsius-api-spec/commit/c8396ca17b613513ea90e67efb17f238095345ca))
* only allow strings for service deployment values to make it json serializable ([e6bd076](https://github.com/exalsius/exalsius-api-spec/commit/e6bd07639be82e2ef2c372d0e56f034f4da357ed))
* remove NodeRole filter for /cluster/{id}/nodes ([e112b1e](https://github.com/exalsius/exalsius-api-spec/commit/e112b1e722180bad763e883543d5bb3d218e0a16))

## [1.1.6](https://github.com/exalsius/exalsius-api-spec/compare/openapi-v1.1.5...openapi-v1.1.6) (2025-05-27)


### Bug Fixes

* change node-invalid-type response code to 422 ([#37](https://github.com/exalsius/exalsius-api-spec/issues/37)) ([c1071c3](https://github.com/exalsius/exalsius-api-spec/commit/c1071c32adff7d6075461ed6a7f997b92ad9c78f))
* use correct error response model ([#39](https://github.com/exalsius/exalsius-api-spec/issues/39)) ([e6f60dc](https://github.com/exalsius/exalsius-api-spec/commit/e6f60dc9dab4498e291f5c763e2a598bdfba8b0c))

## [1.1.5](https://github.com/exalsius/exalsius-api-spec/compare/openapi-v1.1.4...openapi-v1.1.5) (2025-05-23)


### Bug Fixes

* adjust NodesListResponse ([f647c12](https://github.com/exalsius/exalsius-api-spec/commit/f647c12a1f083b24f703d853ec4c83489b1c6fb0))
* fix discriminator logic for node types and use enums for node_type ([d18fccb](https://github.com/exalsius/exalsius-api-spec/commit/d18fccbd23cdfa8a2add9484c9c901bbbd5f98cd))
* split up schemas and responses ([6275bf1](https://github.com/exalsius/exalsius-api-spec/commit/6275bf1f7d0eedc84bcdbcc6b055f1ac8c942c1d))
* use correct response models in paths; add delete ssh-key path ([81e38b3](https://github.com/exalsius/exalsius-api-spec/commit/81e38b3f9e5066e151086ec09d8d61b96c6e4ed4))
* use oneOf in NodeResponse ([29eb3de](https://github.com/exalsius/exalsius-api-spec/commit/29eb3de3a1d8b776125f40a1e43667437401c4be))

## [1.1.4](https://github.com/exalsius/exalsius-api-spec/compare/openapi-v1.1.3...openapi-v1.1.4) (2025-05-20)


### Bug Fixes

* add missing SSH key create request model ([#32](https://github.com/exalsius/exalsius-api-spec/issues/32)) ([a6d43a8](https://github.com/exalsius/exalsius-api-spec/commit/a6d43a84f1352b9fefde86673d837105db78d6b9))

## [1.1.3](https://github.com/exalsius/exalsius-api-spec/compare/openapi-v1.1.2...openapi-v1.1.3) (2025-05-20)


### Bug Fixes

* use integer IDs for all models ([#30](https://github.com/exalsius/exalsius-api-spec/issues/30)) ([7e79741](https://github.com/exalsius/exalsius-api-spec/commit/7e79741e4d5ab0c51ad7cc8d2d5a971c65f82a3d))

## [1.1.2](https://github.com/exalsius/exalsius-api-spec/compare/openapi-v1.1.1...openapi-v1.1.2) (2025-05-19)


### Bug Fixes

* rename status paramter in /clusters endpoint to cluster_status ([#28](https://github.com/exalsius/exalsius-api-spec/issues/28)) ([f91087e](https://github.com/exalsius/exalsius-api-spec/commit/f91087e97b0cd54338965157e71ca79adaf4f770))

## [1.1.1](https://github.com/exalsius/exalsius-api-spec/compare/openapi-v1.1.0...openapi-v1.1.1) (2025-05-19)


### Bug Fixes

* **openapi:** set default response status code ([#26](https://github.com/exalsius/exalsius-api-spec/issues/26)) ([6346f36](https://github.com/exalsius/exalsius-api-spec/commit/6346f36f41d6b6fd27d4a26ab79ca768527cb003))

## [1.1.0](https://github.com/exalsius/exalsius-api-spec/compare/openapi-v1.0.0...openapi-v1.1.0) (2025-05-16)


### Features

* add /clusters/deploy endpoint ([4f4d591](https://github.com/exalsius/exalsius-api-spec/commit/4f4d59194bfd7e3afa14dff9773411364a7972f6))


### Bug Fixes

* adjust enums and integer formats ([9ef25e5](https://github.com/exalsius/exalsius-api-spec/commit/9ef25e54305492950f429fe94c983c557b441b43))
* adjust error model according to RFC 7807 ([15ba13b](https://github.com/exalsius/exalsius-api-spec/commit/15ba13bbe2d0ae8869902db4a46f28b53ecf00b3))
* **base_node:** use x-extensible-enum and specify integer format ([ba64e21](https://github.com/exalsius/exalsius-api-spec/commit/ba64e21d1d97f3d6c6b4d4b34374562ca2dbe844))
* change ID type to integer ([#5](https://github.com/exalsius/exalsius-api-spec/issues/5)) ([5701fdd](https://github.com/exalsius/exalsius-api-spec/commit/5701fdd1e859dfba9b3d496cd9031e3c6e9fba60))
* **cluster:** rename status to cluster_status and use extensible enums ([96dca55](https://github.com/exalsius/exalsius-api-spec/commit/96dca55fa0dd587082f96ad48dd3eee3bb2f8191))
* disable security for now ([c6551b5](https://github.com/exalsius/exalsius-api-spec/commit/c6551b54bec5f498bb021089559eb52128e4987b))
* fix paths and components according to api styleguide ([ce57148](https://github.com/exalsius/exalsius-api-spec/commit/ce571489ad963ccb9724d680ade67a1765e4758d))
* fix POST /clusters response ([102d34b](https://github.com/exalsius/exalsius-api-spec/commit/102d34b8264c3189e9eb9d817b8f2a09c325b964))
* fix versioning of openapi schema ([#18](https://github.com/exalsius/exalsius-api-spec/issues/18)) ([c4b6609](https://github.com/exalsius/exalsius-api-spec/commit/c4b660964ae3e4a89215e1e91cb30cde09ce9412))
* rename request yaml files and selfManagedNode ([fd2faee](https://github.com/exalsius/exalsius-api-spec/commit/fd2faeeb67a2cf116885e6b8b98ebe2f385c3546))
* use consistent error models across failure scenarios ([0a33f14](https://github.com/exalsius/exalsius-api-spec/commit/0a33f145d029001c6475023ae47ad4767caf35c6))
* use snake_case for property names ([3ad2e41](https://github.com/exalsius/exalsius-api-spec/commit/3ad2e41bbe68e8c630b883a2ef76463a93bb102e))
* use x-extensible-enum instead of enum ([bb5d987](https://github.com/exalsius/exalsius-api-spec/commit/bb5d98714214065863b4b49a3a219c3d6fd705b2))
