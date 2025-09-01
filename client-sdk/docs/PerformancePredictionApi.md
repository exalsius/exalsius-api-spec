# exalsius_api_client.PerformancePredictionApi

All URIs are relative to *https://api.exalsius.ai/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_performance_prediction**](PerformancePredictionApi.md#get_performance_prediction) | **POST** /performance-prediction | Get performance predictions for a configuration


# **get_performance_prediction**
> PerformancePredictionResponse get_performance_prediction(performance_prediction_request)

Get performance predictions for a configuration

This endpoint returns predicted runtime and memory usage for a given configuration of model, optimizer, batch size, and sequence length.


### Example

* OAuth Authentication (OAuth2):

```python
import exalsius_api_client
from exalsius_api_client.models.performance_prediction_request import PerformancePredictionRequest
from exalsius_api_client.models.performance_prediction_response import PerformancePredictionResponse
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
    api_instance = exalsius_api_client.PerformancePredictionApi(api_client)
    performance_prediction_request = exalsius_api_client.PerformancePredictionRequest() # PerformancePredictionRequest | 

    try:
        # Get performance predictions for a configuration
        api_response = api_instance.get_performance_prediction(performance_prediction_request)
        print("The response of PerformancePredictionApi->get_performance_prediction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PerformancePredictionApi->get_performance_prediction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **performance_prediction_request** | [**PerformancePredictionRequest**](PerformancePredictionRequest.md)|  | 

### Return type

[**PerformancePredictionResponse**](PerformancePredictionResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Performance Prediction |  -  |
**400** | Error response |  -  |
**422** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

