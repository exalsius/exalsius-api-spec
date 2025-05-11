install:
	echo "Installing npm deps and Python code-gen tools…"
	npm install

lint:
	@echo "Linting OpenAPI spec…"
	npm run test

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





