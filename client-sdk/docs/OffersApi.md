# exalsius_api_client.OffersApi

All URIs are relative to *https://api.exalsius.ai/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_offers**](OffersApi.md#get_offers) | **GET** /offers | List and filter current GPU on-demand and spot market offers


# **get_offers**
> OffersListResponse get_offers(gpu_vendor=gpu_vendor, gpu_type=gpu_type, cloud_provider=cloud_provider, region=region, gpu_count=gpu_count, page_size=page_size, cursor=cursor)

List and filter current GPU on-demand and spot market offers

**List GPU offers (on-demand & spot instances)**
Retrieve current GPU instance offers from both on-demand and spot markets, with optional filters.

**Parameters (optional)**
- `gpu_vendor`: The vendor of the GPU (nvidia, amd, intel, huawei)
- `gpu_type`: The type of the GPU
- `provider`: The cloud provider of the offer
- `region`: The region of the offer
- `gpu_count`: The minimum number of GPUs in the offer
- `page_size`: The number of offers to return per page (default: 50, max: 100)
- `cursor`: The cursor for pagination. Use the `next_cursor` from the previous response to get the next page.

**Examples**

Here's an example of how to filter by vendor:
  ```
  /offers?gpu_vendor=nvidia
  ```

Here's an example of how to filter by provider:
  ```
  /offers?cloud_provider=aws
  ```

Here's an example of how to filter by provider and region:
  ```
  /offers?provider=aws&region=us-east-1
  ```
  
Here's an example of how to filter by provider, region, and gpuCount:
  ```
  /offers?provider=aws&region=us-east-1&gpuCount=1
  ```

Here's an example of pagination:
  ```
  # First page
  /offers?page_size=20
  
  # Next page using cursor from previous response
  /offers?page_size=20&cursor=eyJvZmZlcl9pZCI6ImF3cy1nNGRuLnhsYXJnZS11cy1lYXN0LTEtdXMtZWFzdC0xYSJ9
  ```
  
**Result**

The response includes:
- A list of offers
- The total number of offers matching the filters
- A cursor for the next page (if there are more results)
- A cursor for the previous page (if not on the first page)


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
    api_instance = exalsius_api_client.OffersApi(api_client)
    gpu_vendor = 'gpu_vendor_example' # str | The vendor of the GPU (optional)
    gpu_type = 'gpu_type_example' # str | The type of the GPU (optional)
    cloud_provider = 'cloud_provider_example' # str | The cloud provider of the offer (optional)
    region = 'region_example' # str | The region of the offer, e.g. us-east-1 (optional)
    gpu_count = 56 # int | The minimum number of GPUs in the offer (optional)
    page_size = 56 # int | The number of offers to return per page (optional)
    cursor = 'cursor_example' # str | The cursor for pagination. Use the `next_cursor` from the previous response to get the next page. (optional)

    try:
        # List and filter current GPU on-demand and spot market offers
        api_response = api_instance.get_offers(gpu_vendor=gpu_vendor, gpu_type=gpu_type, cloud_provider=cloud_provider, region=region, gpu_count=gpu_count, page_size=page_size, cursor=cursor)
        print("The response of OffersApi->get_offers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OffersApi->get_offers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gpu_vendor** | **str**| The vendor of the GPU | [optional] 
 **gpu_type** | **str**| The type of the GPU | [optional] 
 **cloud_provider** | **str**| The cloud provider of the offer | [optional] 
 **region** | **str**| The region of the offer, e.g. us-east-1 | [optional] 
 **gpu_count** | **int**| The minimum number of GPUs in the offer | [optional] 
 **page_size** | **int**| The number of offers to return per page | [optional] 
 **cursor** | **str**| The cursor for pagination. Use the &#x60;next_cursor&#x60; from the previous response to get the next page. | [optional] 

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

