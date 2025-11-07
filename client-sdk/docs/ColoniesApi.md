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

Create a new colony to organize and manage multiple clusters together. Colonies enable coordinated 
management, scheduling, and operations across multiple clusters.

**Parameters:**
- `name`: A descriptive name for the colony (must be unique within your account)

**Behavior:**
- A new colony resource will be created with the specified name
- The colony starts empty (no clusters)
- Clusters can be added to the colony when they are created by specifying the colony ID
- Once created, you can use the colony's kubeconfig to access all clusters in the colony


### Example

* OAuth Authentication (OAuth2):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with exalsius_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = exalsius_api_client.ColoniesApi(api_client)
    colony_create_request = {"name":"my-colony"} # ColonyCreateRequest | 

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

[OAuth2](../README.md#OAuth2)

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

Permanently delete a colony and all clusters that belong to it. This operation will tear down all 
infrastructure associated with the colony.

**Warning: This operation is irreversible.**

**Behavior:**
- The colony will be permanently deleted from your account
- All clusters that belong to the colony will also be deleted
- All resources (nodes, workspaces, services) deployed on those clusters will be terminated
- The deletion process may take several minutes to complete
- Once deleted, the colony and its clusters cannot be recovered

**Response:**
The response includes the colony ID and a list of all cluster IDs that were deleted as part of this operation.


### Example

* OAuth Authentication (OAuth2):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

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

[OAuth2](../README.md#OAuth2)

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

Fetch comprehensive metadata for a specific colony, including its name, owner, associated cluster IDs, 
namespace, and creation timestamp. This information helps you understand the colony's composition and 
manage its clusters.


### Example

* OAuth Authentication (OAuth2):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

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

[OAuth2](../README.md#OAuth2)

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

Retrieve the kubeconfig file that provides access to all clusters within the colony. The kubeconfig 
contains authentication credentials and cluster connection information, allowing you to manage all 
clusters in the colony using standard Kubernetes tools (kubectl, etc.).

**Usage:**
- Save the kubeconfig to a file and set it as your `KUBECONFIG` environment variable
- Use `kubectl` or other Kubernetes tools to interact with clusters in the colony
- The kubeconfig includes contexts for all clusters in the colony, allowing you to switch between them
- This is useful for managing multiple clusters as a unified infrastructure group


### Example

* OAuth Authentication (OAuth2):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

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

[OAuth2](../README.md#OAuth2)

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

Retrieve all colonies associated with your account. Colonies are groups of clusters that can be managed 
together for coordinated operations and scheduling. Each colony can contain multiple clusters, allowing 
you to organize your infrastructure logically.


### Example

* OAuth Authentication (OAuth2):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

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

[OAuth2](../README.md#OAuth2)

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

