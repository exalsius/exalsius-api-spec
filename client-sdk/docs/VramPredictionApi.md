# exalsius_api_client.VramPredictionApi

All URIs are relative to *https://api.exalsius.ai/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_vram_prediction**](VramPredictionApi.md#get_vram_prediction) | **POST** /vram-prediction | Get the VRAM prediction for LLM fine-tuning
[**get_vram_prediction_metadata**](VramPredictionApi.md#get_vram_prediction_metadata) | **GET** /vram-prediction/metadata | List available models and the range of parameters for VRAM prediction endpoint


# **get_vram_prediction**
> VramPredictionResponse get_vram_prediction(vram_prediction_request)

Get the VRAM prediction for LLM fine-tuning

**Get the VRAM prediction for LLM-finetuning**

This endpoint returns predicted memory usage (VRAM) for a given LLM fine-tuning configuration.

**Request Parameters:**
- `model`: The machine learning model to train
- `batch_size`: Number of samples processed per training step
- `sequence_length`: Length of input sequences (tokens)
- (Optional) `accumulation_steps`: Number of gradient accumulation steps (use 1 for no accumulation). Default: 1

**Response:**
- `vram`: Predicted VRAM usage in GB


### Example

* OAuth Authentication (OAuth2):

```python
import exalsius_api_client
from exalsius_api_client.models.vram_prediction_request import VramPredictionRequest
from exalsius_api_client.models.vram_prediction_response import VramPredictionResponse
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
    api_instance = exalsius_api_client.VramPredictionApi(api_client)
    vram_prediction_request = {"model":"meta-llama/Llama-3.2-1B","batch_size":4,"sequence_length":2048} # VramPredictionRequest | 

    try:
        # Get the VRAM prediction for LLM fine-tuning
        api_response = api_instance.get_vram_prediction(vram_prediction_request)
        print("The response of VramPredictionApi->get_vram_prediction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VramPredictionApi->get_vram_prediction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vram_prediction_request** | [**VramPredictionRequest**](VramPredictionRequest.md)|  | 

### Return type

[**VramPredictionResponse**](VramPredictionResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | VRAM Prediction response |  -  |
**400** | Error response |  -  |
**422** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vram_prediction_metadata**
> VramPredictionMetadataResponse get_vram_prediction_metadata()

List available models and the range of parameters for VRAM prediction endpoint

Retrieve the distinct values and numeric ranges available within the VRAMPrediction endpoint.


### Example

* OAuth Authentication (OAuth2):

```python
import exalsius_api_client
from exalsius_api_client.models.vram_prediction_metadata_response import VramPredictionMetadataResponse
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
    api_instance = exalsius_api_client.VramPredictionApi(api_client)

    try:
        # List available models and the range of parameters for VRAM prediction endpoint
        api_response = api_instance.get_vram_prediction_metadata()
        print("The response of VramPredictionApi->get_vram_prediction_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VramPredictionApi->get_vram_prediction_metadata: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**VramPredictionMetadataResponse**](VramPredictionMetadataResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | VRAM Prediction  metadata |  -  |
**400** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

