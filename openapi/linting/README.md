# OpenAPI Linting with Spectral

This repository includes a Spectral configuration that enforces the [Zalando RESTful API Guidelines](https://opensource.zalando.com/restful-api-guidelines/). The ruleset is defined in `spectral.json` and automatically validates OpenAPI specifications against Zalando's best practices for REST API design.

The rules enforce key guidelines around:
- JSON object responses
- API versioning 
- Property naming conventions
- Enum handling

To use this linting configuration:

1. Install the e.g. [Spectral VS Code extension](https://marketplace.visualstudio.com/items?itemName=stoplight.spectral) and configure it in your editor
2. The ruleset will automatically validate your OpenAPI specs against the Zalando guidelines
3. Fix any validation errors to ensure compliance with the style guide
4. Alternatively, you can run linting from the command line using `make lint` using a docker container

The full set of enforced rules can be found in the `zalando.json` file.
