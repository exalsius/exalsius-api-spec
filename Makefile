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
.PHONY: lint

build:
	@echo "Bundling OpenAPI spec into dist/bundle.yaml…"
	docker run --init --rm \
		--user $(shell id -u):$(shell id -g) \
		-v $(CURRENT_DIR):/spec \
		redocly/cli \
		--config /spec/openapi/redocly.yaml \
		bundle /spec/openapi/openapi.yaml -o /spec/dist/bundle.yaml
.PHONY: build

run-redocly:
	docker run --init --rm -p 8080:8080 \
		--user $(shell id -u):$(shell id -g) \
		-v $(CURRENT_DIR):/spec \
		redocly/cli \
		--config /spec/openapi/redocly.yaml \
		preview-docs /spec/openapi/openapi.yaml --host 0.0.0.0
.PHONY: run-redocly

run-swagger:
	docker run --rm -p 8081:8080 \
        -e SWAGGER_JSON=/spec/openapi/openapi.yaml \
        -v "$(CURRENT_DIR):/spec:ro" \
		swaggerapi/swagger-ui
.PHONY: run-swagger

mock-server: build
	docker run --init --rm -v $(CURRENT_DIR):/tmp \
	 -p 4010:4010 \
	  stoplight/prism:4 \
	  mock -d -h 0.0.0.0 "/tmp/dist/bundle.yaml"
.PHONY: mock-server

generate:
	./scripts/generate-client.sh
.PHONY: generate

generate-server:
	@echo "Generating server stub"
	docker run --rm -v "${PWD}:/local" \
		--user $(shell id -u):$(shell id -g) \
		openapitools/openapi-generator-cli generate \
		-i local/dist/bundle.yaml \
		--package-name "exalsius_api_server" \
		-g python-fastapi \
		-t /local/custom-templates/python-fastapi \
		--additional-properties=fastapiImplementationPackage=controllers \
		-o /local/server
.PHONY: generate-server