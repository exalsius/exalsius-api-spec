# exalsius_api_client.OffersApi

All URIs are relative to *https://api.exalsius.ai/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_offers**](OffersApi.md#get_offers) | **GET** /offers | List and filter current GPU on-demand and spot market offers


# **get_offers**
> OffersListResponse get_offers(gpu_vendor=gpu_vendor, gpu_type=gpu_type, cloud_provider=cloud_provider, region=region, availability_zone=availability_zone, location=location, cpu_vendor=cpu_vendor, cpu_arch=cpu_arch, pricing_unit=pricing_unit, price_type=price_type, gpu_count_min=gpu_count_min, gpu_count_max=gpu_count_max, gpu_memory_min=gpu_memory_min, gpu_memory_max=gpu_memory_max, total_gpu_memory_min=total_gpu_memory_min, total_gpu_memory_max=total_gpu_memory_max, main_memory_min=main_memory_min, main_memory_max=main_memory_max, vcpus_min=vcpus_min, vcpus_max=vcpus_max, price_min=price_min, price_max=price_max, page_size=page_size, cursor=cursor, sort_by=sort_by, sort_order=sort_order)

List and filter current GPU on-demand and spot market offers

**List GPU offers (on-demand & spot instances)**
Retrieve current GPU instance offers from both on-demand and spot markets, with optional filters.


### Example

* OAuth Authentication (OAuth2):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with exalsius_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = exalsius_api_client.OffersApi(api_client)
    gpu_vendor = 'gpu_vendor_example' # str | The vendor of the GPU (optional)
    gpu_type = 'gpu_type_example' # str | The type of the GPU (optional)
    cloud_provider = 'cloud_provider_example' # str | The cloud provider of the offer (optional)
    region = 'region_example' # str | The region of the offer, e.g. us-east-1 (optional)
    availability_zone = 'availability_zone_example' # str | The availability zone of the offer (optional)
    location = 'location_example' # str | The location of the offer (optional)
    cpu_vendor = 'cpu_vendor_example' # str | The vendor of the CPU (optional)
    cpu_arch = 'cpu_arch_example' # str | The architecture of the CPU (optional)
    pricing_unit = 'pricing_unit_example' # str | The pricing unit (optional)
    price_type = 'price_type_example' # str | The type of pricing model (optional)
    gpu_count_min = 56 # int | Minimum number of GPUs (optional)
    gpu_count_max = 56 # int | Maximum number of GPUs (optional)
    gpu_memory_min = 56 # int | Minimum GPU memory of single GPU (MiB) (optional)
    gpu_memory_max = 56 # int | Maximum GPU memory of single GPU (MiB) (optional)
    total_gpu_memory_min = 56 # int | Minimum total GPU memory (MiB) (optional)
    total_gpu_memory_max = 56 # int | Maximum total GPU memory (MiB) (optional)
    main_memory_min = 56 # int | Minimum main memory (MiB) (optional)
    main_memory_max = 56 # int | Maximum main memory (MiB) (optional)
    vcpus_min = 56 # int | Minimum number of virtual CPUs (optional)
    vcpus_max = 56 # int | Maximum number of virtual CPUs (optional)
    price_min = 3.4 # float | Minimum price per hour (optional)
    price_max = 3.4 # float | Maximum price per hour (optional)
    page_size = 56 # int | The number of offers to return per page (optional)
    cursor = 'cursor_example' # str | The cursor for pagination. Use the `next_cursor` from the previous response to get the next page. (optional)
    sort_by = 'sort_by_example' # str | Field to sort by (optional)
    sort_order = 'sort_order_example' # str | Sort order (optional)

    try:
        # List and filter current GPU on-demand and spot market offers
        api_response = api_instance.get_offers(gpu_vendor=gpu_vendor, gpu_type=gpu_type, cloud_provider=cloud_provider, region=region, availability_zone=availability_zone, location=location, cpu_vendor=cpu_vendor, cpu_arch=cpu_arch, pricing_unit=pricing_unit, price_type=price_type, gpu_count_min=gpu_count_min, gpu_count_max=gpu_count_max, gpu_memory_min=gpu_memory_min, gpu_memory_max=gpu_memory_max, total_gpu_memory_min=total_gpu_memory_min, total_gpu_memory_max=total_gpu_memory_max, main_memory_min=main_memory_min, main_memory_max=main_memory_max, vcpus_min=vcpus_min, vcpus_max=vcpus_max, price_min=price_min, price_max=price_max, page_size=page_size, cursor=cursor, sort_by=sort_by, sort_order=sort_order)
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
 **availability_zone** | **str**| The availability zone of the offer | [optional] 
 **location** | **str**| The location of the offer | [optional] 
 **cpu_vendor** | **str**| The vendor of the CPU | [optional] 
 **cpu_arch** | **str**| The architecture of the CPU | [optional] 
 **pricing_unit** | **str**| The pricing unit | [optional] 
 **price_type** | **str**| The type of pricing model | [optional] 
 **gpu_count_min** | **int**| Minimum number of GPUs | [optional] 
 **gpu_count_max** | **int**| Maximum number of GPUs | [optional] 
 **gpu_memory_min** | **int**| Minimum GPU memory of single GPU (MiB) | [optional] 
 **gpu_memory_max** | **int**| Maximum GPU memory of single GPU (MiB) | [optional] 
 **total_gpu_memory_min** | **int**| Minimum total GPU memory (MiB) | [optional] 
 **total_gpu_memory_max** | **int**| Maximum total GPU memory (MiB) | [optional] 
 **main_memory_min** | **int**| Minimum main memory (MiB) | [optional] 
 **main_memory_max** | **int**| Maximum main memory (MiB) | [optional] 
 **vcpus_min** | **int**| Minimum number of virtual CPUs | [optional] 
 **vcpus_max** | **int**| Maximum number of virtual CPUs | [optional] 
 **price_min** | **float**| Minimum price per hour | [optional] 
 **price_max** | **float**| Maximum price per hour | [optional] 
 **page_size** | **int**| The number of offers to return per page | [optional] 
 **cursor** | **str**| The cursor for pagination. Use the &#x60;next_cursor&#x60; from the previous response to get the next page. | [optional] 
 **sort_by** | **str**| Field to sort by | [optional] 
 **sort_order** | **str**| Sort order | [optional] 

### Return type

[**OffersListResponse**](OffersListResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

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

