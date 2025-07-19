# exalsius_api_client.ColoniesApi

All URIs are relative to *https://api.exalsius.ai/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_colony**](ColoniesApi.md#create_colony) | **POST** /colonies | Create a colony
[**delete_colony**](ColoniesApi.md#delete_colony) | **DELETE** /colony/{colony_id} | Delete (tear-down) a colony
[**describe_colony**](ColoniesApi.md#describe_colony) | **GET** /colony/{colony_id} | Get details of a single colony
[**get_colony_kubeconfig**](ColoniesApi.md#get_colony_kubeconfig) | **GET** /colony/{colony_id}/kubeconfig | Get the kubeconfig for a colony
[**list_colonies**](ColoniesApi.md#list_colonies) | **GET** /colonies | List all colonies


# **create_colony**
> ColonyCreateResponse create_colony(colony_create_request)

Create a colony

**Create a colony**

Create a new colony.

**Parameters**

- `name`: The name of the colony

**Behavior**

Creating a new colony will result in a new colony resource being created. 
Clusters will be added to the colony as they are created.


### Example


```python
import exalsius_api_client
from exalsius_api_client.models.colony_create_request import ColonyCreateRequest
from exalsius_api_client.models.colony_create_response import ColonyCreateResponse
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
    api_instance = exalsius_api_client.ColoniesApi(api_client)
    colony_create_request = exalsius_api_client.ColonyCreateRequest() # ColonyCreateRequest | 

    try:
        # Create a colony
        api_response = api_instance.create_colony(colony_create_request)
        print("The response of ColoniesApi->create_colony:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ColoniesApi->create_colony: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **colony_create_request** | [**ColonyCreateRequest**](ColonyCreateRequest.md)|  | 

### Return type

[**ColonyCreateResponse**](ColonyCreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Colony creation response |  -  |
**400** | Error response |  -  |
**409** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_colony**
> ColonyDeleteResponse delete_colony(colony_id)

Delete (tear-down) a colony

**Delete a colony**

Permanently delete a colony. This also deletes all clusters
that belong to the colony.
Once deleted, the colony is no longer part of your account.

**Note**

This operation is irreversible.


### Example


```python
import exalsius_api_client
from exalsius_api_client.models.colony_delete_response import ColonyDeleteResponse
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
    api_instance = exalsius_api_client.ColoniesApi(api_client)
    colony_id = 'colony_id_example' # str | ID of the colony to delete

    try:
        # Delete (tear-down) a colony
        api_response = api_instance.delete_colony(colony_id)
        print("The response of ColoniesApi->delete_colony:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ColoniesApi->delete_colony: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **colony_id** | **str**| ID of the colony to delete | 

### Return type

[**ColonyDeleteResponse**](ColonyDeleteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Colony deletion response |  -  |
**404** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **describe_colony**
> ColonyResponse describe_colony(colony_id)

Get details of a single colony

**Retrieve the details of a single colony**

Fetch all metadata for one colony.


### Example


```python
import exalsius_api_client
from exalsius_api_client.models.colony_response import ColonyResponse
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
    api_instance = exalsius_api_client.ColoniesApi(api_client)
    colony_id = 'colony_id_example' # str | ID of the colony to describe

    try:
        # Get details of a single colony
        api_response = api_instance.describe_colony(colony_id)
        print("The response of ColoniesApi->describe_colony:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ColoniesApi->describe_colony: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **colony_id** | **str**| ID of the colony to describe | 

### Return type

[**ColonyResponse**](ColonyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Colony details |  -  |
**404** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_colony_kubeconfig**
> ColonyKubeconfigResponse get_colony_kubeconfig(colony_id)

Get the kubeconfig for a colony

**Get the kubeconfig for a colony**

The kubeconfig file contains the credentials to access all clusters of the colony.


### Example


```python
import exalsius_api_client
from exalsius_api_client.models.colony_kubeconfig_response import ColonyKubeconfigResponse
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
    api_instance = exalsius_api_client.ColoniesApi(api_client)
    colony_id = 'colony_id_example' # str | The ID of the colony to get the kubeconfig for

    try:
        # Get the kubeconfig for a colony
        api_response = api_instance.get_colony_kubeconfig(colony_id)
        print("The response of ColoniesApi->get_colony_kubeconfig:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ColoniesApi->get_colony_kubeconfig: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **colony_id** | **str**| The ID of the colony to get the kubeconfig for | 

### Return type

[**ColonyKubeconfigResponse**](ColonyKubeconfigResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The kubeconfig file for all clusters of a colony |  -  |
**404** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_colonies**
> ColoniesListResponse list_colonies()

List all colonies

**List all colonies**

Retrieve all colonies


### Example


```python
import exalsius_api_client
from exalsius_api_client.models.colonies_list_response import ColoniesListResponse
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
    api_instance = exalsius_api_client.ColoniesApi(api_client)

    try:
        # List all colonies
        api_response = api_instance.list_colonies()
        print("The response of ColoniesApi->list_colonies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ColoniesApi->list_colonies: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ColoniesListResponse**](ColoniesListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of colonies |  -  |
**404** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

