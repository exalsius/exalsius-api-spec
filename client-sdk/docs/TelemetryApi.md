# exalsius_api_client.TelemetryApi

All URIs are relative to *https://api.exalsius.ai/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_telemetry_event**](TelemetryApi.md#post_telemetry_event) | **POST** /telemetry | Post a telemetry event


# **post_telemetry_event**
> post_telemetry_event(telemetry_event_request)

Post a telemetry event



### Example

* OAuth Authentication (OAuth2):

```python
import exalsius_api_client
from exalsius_api_client.models.telemetry_event_request import TelemetryEventRequest
from exalsius_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.exalsius.ai/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = exalsius_api_client.Configuration(
    host = "https://api.exalsius.ai/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with exalsius_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = exalsius_api_client.TelemetryApi(api_client)
    telemetry_event_request = {"event_name":"list-workspaces-event"} # TelemetryEventRequest | 

    try:
        # Post a telemetry event
        api_instance.post_telemetry_event(telemetry_event_request)
    except Exception as e:
        print("Exception when calling TelemetryApi->post_telemetry_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **telemetry_event_request** | [**TelemetryEventRequest**](TelemetryEventRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Telemetry event accepted. |  -  |
**400** | Error response |  -  |
**422** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

