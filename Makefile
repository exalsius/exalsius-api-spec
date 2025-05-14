CURRENT_DIR := $(CURDIR)

install:
	echo "Installing npm deps and Python code-gen tools…"
	npm install

lint:
	@echo "Linting OpenAPI spec according to the Style Guide…"
	docker run --rm -it -v $(CURRENT_DIR)/openapi:/openapi \
	 stoplight/spectral --ruleset /openapi/linting/spectral.json lint "/openapi/openapi.yaml"

build:
	@echo "Bundling OpenAPI spec into dist/bundle.yaml…"
	npm run build

models:
	@echo "Generating Pydantic models from OpenAPI spec…"
	datamodel-codegen --input dist/bundle.yaml --output models.py

server:
	@echo "Generating Python server from OpenAPI spec…"
	openapi-generator-cli generate -i dist/bundle.yaml -g python-fastapi -o python_api/server --package-name exalsius_api

run-redocly:
	npm run start

run-swagger:
	docker run --rm -p 8081:8080 \
        -e SWAGGER_JSON=/spec/openapi.yaml \
        -v "$(pwd)/openapi:/spec:ro" \
		swaggerapi/swagger-ui

mock-server: build
	docker run --init --rm -v $(CURRENT_DIR):/tmp \
	 -p 4010:4010 \
	  stoplight/prism:4 \
	  mock -d -h 0.0.0.0 "/tmp/dist/bundle.yaml"

generate:
	datamodel-codegen \
		--input dist/bundle.yaml \
		--output models.py \
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


