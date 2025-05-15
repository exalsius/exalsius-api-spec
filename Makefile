CURRENT_DIR := $(CURDIR)

lint:
	@echo "Linting OpenAPI spec with Redocly…"
	docker run --rm \
		--user $(shell id -u):$(shell id -g) \
		-v $(CURRENT_DIR):/api-spec \
		-w /api-spec \
		redocly/cli \
		--config openapi/redocly.yaml \
		lint openapi/openapi.yaml

build:
	@echo "Bundling OpenAPI spec into dist/bundle.yaml…"
	docker run --init --rm \
		--user $(shell id -u):$(shell id -g) \
		-v $(CURRENT_DIR):/spec \
		redocly/cli \
		--config /spec/openapi/redocly.yaml \
		bundle /spec/openapi/openapi.yaml -o /spec/dist/bundle.yaml

run-redocly:
	docker run --init --rm -p 8080:8080 \
		--user $(shell id -u):$(shell id -g) \
		-v $(CURRENT_DIR):/spec \
		redocly/cli \
		--config /spec/openapi/redocly.yaml \
		preview-docs /spec/openapi/openapi.yaml --host 0.0.0.0

run-swagger:
	docker run --rm -p 8081:8080 \
        -e SWAGGER_JSON=/spec/openapi/openapi.yaml \
        -v "$(CURRENT_DIR):/spec:ro" \
		swaggerapi/swagger-ui

mock-server: build
	docker run --init --rm -v $(CURRENT_DIR):/tmp \
	 -p 4010:4010 \
	  stoplight/prism:4 \
	  mock -d -h 0.0.0.0 "/tmp/dist/bundle.yaml"

generate-models:
	docker run --rm -v "${CURRENT_DIR}:/local" \
		--user $(shell id -u):$(shell id -g) \
		koxudaxi/datamodel-code-generator \
		--input local/dist/bundle.yaml \
		--output local/models.py \
		--input-file-type openapi \
		--output-model-type pydantic_v2.BaseModel \
		--use-standard-collections \
		--use-union-operator \
		--target-python-version 3.13 \
		--snake-case-field \
		--use-schema-description \
		--disable-timestamp \
		--use-schema-description \
		--enable-version-header \
		--enum-field-as-literal one \
		--use-double-quotes \
		--field-constraints \
		--allow-population-by-field-name \
		--strict-nullable \
		--use-title-as-name

generate: build generate-client generate-server
.PHONY: generate-client generate-server

generate-client:
	@echo "Generating client SDK"
	docker run --rm -v "${PWD}:/local" \
		--user $(shell id -u):$(shell id -g) \
		openapitools/openapi-generator-cli generate \
		-i local/dist/bundle.yaml \
		--package-name "exalsius_api_client" \
		-g python \
		-o /local/client

generate-server:
	@echo "Generating server stub"
	docker run --rm -v "${PWD}:/local" \
		--user $(shell id -u):$(shell id -g) \
		openapitools/openapi-generator-cli generate \
		-i local/dist/bundle.yaml \
		--package-name "exalsius_api_server" \
		-g python-fastapi \
		-t /local/custom-templates/python-fastapi \
		--additional-properties=fastapiImplementationPackage=own_impl \
		-o /local/server;