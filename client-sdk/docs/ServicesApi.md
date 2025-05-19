# exalsius_api_client.ServicesApi

All URIs are relative to *https://api.exalsius.ai/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_available_services**](ServicesApi.md#list_available_services) | **GET** /services | List all available services


# **list_available_services**
> ServicesListResponse list_available_services()

List all available services

**List all available services**

List all services that can be deployed.

**Note**

Services can be added to the exalsius management cluster using the `exalsius-operator`.

**Result**

Returns an array of service objects.


### Example


```python
import exalsius_api_client
from exalsius_api_client.models.services_list_response import ServicesListResponse
from exalsius_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.exalsius.ai/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = exalsius_api_client.Configuration(
    host = "https://api.exalsius.ai/v1"
)


# Enter a context with an instance of the API client
with exalsius_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = exalsius_api_client.ServicesApi(api_client)

    try:
        # List all available services
        api_response = api_instance.list_available_services()
        print("The response of ServicesApi->list_available_services:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->list_available_services: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ServicesListResponse**](ServicesListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of services |  -  |
**404** | Services not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

