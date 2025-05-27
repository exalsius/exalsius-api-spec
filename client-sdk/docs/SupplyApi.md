# exalsius_api_client.SupplyApi

All URIs are relative to *https://api.exalsius.ai/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_offers**](SupplyApi.md#get_offers) | **GET** /offers | List and filter current GPU on-demand and spot market offers


# **get_offers**
> OffersListResponse get_offers(gpu_vendor=gpu_vendor, gpu_type=gpu_type, provider=provider, region=region, gpu_count=gpu_count, price=price, limit=limit)

List and filter current GPU on-demand and spot market offers

**List GPU offers (on-demand & spot instances)**
Retrieve current GPU instance offers from both on-demand and spot markets, with optional filters.

**Parameters (optional)**
- `gpu_vendor`: The vendor of the GPU (nvidia, amd, intel, huawei)
- `gpu_type`: The type of the GPU
- `provider`: The cloud provider of the offer
- `region`: The region of the offer
- `gpu_count`: The minimum number of GPUs in the offer
- `price`: The maximum price per hour for the offer
- `limit`: The maximum number of offers to return

**Examples**

Here's an example of how to filter by vendor:
  ```
  /offers?gpu_vendor=nvidia
  ```

Here's an example of how to filter by provider:
  ```
  /offers?provider=aws
  ```

Here's an example of how to filter by provider and region:
  ```
  /offers?provider=aws&region=us-east-1
  ```
  
Here's an example of how to filter by provider, region, and gpuCount:
  ```
  /offers?provider=aws&region=us-east-1&gpuCount=1
  ```
  
**Result**

The response is paginated with a limit of 50 offers per page.
The offers are sorted by price per hour, from lowest to highest.


### Example


```python
import exalsius_api_client
from exalsius_api_client.models.offers_list_response import OffersListResponse
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
    api_instance = exalsius_api_client.SupplyApi(api_client)
    gpu_vendor = 'gpu_vendor_example' # str |  (optional)
    gpu_type = 'gpu_type_example' # str | The type of the GPU (optional)
    provider = 'provider_example' # str | The cloud provider of the offer (optional)
    region = 'region_example' # str | The region of the offer, e.g. us-east-1 (optional)
    gpu_count = 3.4 # float | The minimum number of GPUs in the offer (optional)
    price = 3.4 # float | The maximum price per hour for the offer (optional)
    limit = 3.4 # float | The maximum number of offers to return (optional)

    try:
        # List and filter current GPU on-demand and spot market offers
        api_response = api_instance.get_offers(gpu_vendor=gpu_vendor, gpu_type=gpu_type, provider=provider, region=region, gpu_count=gpu_count, price=price, limit=limit)
        print("The response of SupplyApi->get_offers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupplyApi->get_offers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gpu_vendor** | **str**|  | [optional] 
 **gpu_type** | **str**| The type of the GPU | [optional] 
 **provider** | **str**| The cloud provider of the offer | [optional] 
 **region** | **str**| The region of the offer, e.g. us-east-1 | [optional] 
 **gpu_count** | **float**| The minimum number of GPUs in the offer | [optional] 
 **price** | **float**| The maximum price per hour for the offer | [optional] 
 **limit** | **float**| The maximum number of offers to return | [optional] 

### Return type

[**OffersListResponse**](OffersListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of offers |  -  |
**400** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

