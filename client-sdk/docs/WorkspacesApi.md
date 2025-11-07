# exalsius_api_client.WorkspacesApi

All URIs are relative to *https://api.exalsius.ai/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_workspace**](WorkspacesApi.md#create_workspace) | **POST** /workspaces | Create a workspace
[**delete_workspace**](WorkspacesApi.md#delete_workspace) | **DELETE** /workspace/{workspace_id} | Delete a workspace
[**describe_workspace**](WorkspacesApi.md#describe_workspace) | **GET** /workspace/{workspace_id} | Get details of a single workspace
[**list_workspaces**](WorkspacesApi.md#list_workspaces) | **GET** /workspaces | List all workspaces
[**start_workspace**](WorkspacesApi.md#start_workspace) | **POST** /workspace/{workspace_id}/start | Start a workspace
[**stop_workspace**](WorkspacesApi.md#stop_workspace) | **POST** /workspace/{workspace_id}/stop | Stop a workspace


# **create_workspace**
> WorkspaceCreateResponse create_workspace(workspace_create_request)

Create a workspace

**Create a workspace**

Create a new workspace.

**Parameters**

- `name`: The name of the workspace
- `cluster_id`: The ID of the cluster to deploy the workspace to
- `template`: The template to use for the workspace
- `resources`: The resources to use for the workspace

**Behavior**

Creating a new workspace will result in a new workspace resource being created. The workspace will be in 
the `PENDING` state initially and will transition to `RUNNING` once deployment completes. You can check 
the workspace status using `GET /workspace/{workspace_id}`.


### Example

* OAuth Authentication (OAuth2):

```python
import exalsius_api_client
from exalsius_api_client.models.workspace_create_request import WorkspaceCreateRequest
from exalsius_api_client.models.workspace_create_response import WorkspaceCreateResponse
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
    api_instance = exalsius_api_client.WorkspacesApi(api_client)
    workspace_create_request = {"name":"my-jupyter-workspace","cluster_id":"123e4567-e89b-12d3-a456-426614174000","template":{"name":"jupyter-notebook","variables":{"notebook_port":"8888"}},"resources":{"gpu_count":1,"gpu_type":"A100","gpu_vendor":"NVIDIA","cpu_cores":4,"memory_gb":16,"storage_gb":100},"description":"My machine learning workspace"} # WorkspaceCreateRequest | 

    try:
        # Create a workspace
        api_response = api_instance.create_workspace(workspace_create_request)
        print("The response of WorkspacesApi->create_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->create_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_create_request** | [**WorkspaceCreateRequest**](WorkspaceCreateRequest.md)|  | 

### Return type

[**WorkspaceCreateResponse**](WorkspaceCreateResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Workspace creation response |  -  |
**400** | Error response |  -  |
**409** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_workspace**
> WorkspaceDeleteResponse delete_workspace(workspace_id)

Delete a workspace

**Delete a workspace**

Permanently delete a workspace and all its associated resources.

**Warning: This operation is irreversible.**

**Behavior:**
- The workspace will be marked for deletion immediately
- All associated Pods and resources will be terminated
- Persistent volumes may be retained depending on the storage policy
- The deletion process may take a few minutes to complete
- Once deleted, the workspace cannot be recovered


### Example

* OAuth Authentication (OAuth2):

```python
import exalsius_api_client
from exalsius_api_client.models.workspace_delete_response import WorkspaceDeleteResponse
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
    api_instance = exalsius_api_client.WorkspacesApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace to delete

    try:
        # Delete a workspace
        api_response = api_instance.delete_workspace(workspace_id)
        print("The response of WorkspacesApi->delete_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->delete_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| ID of the workspace to delete | 

### Return type

[**WorkspaceDeleteResponse**](WorkspaceDeleteResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Workspace deletion response |  -  |
**404** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **describe_workspace**
> WorkspaceResponse describe_workspace(workspace_id)

Get details of a single workspace

**Retrieve the details of a single workspace**

Fetch comprehensive metadata for a specific workspace, including its status, configuration,
resource allocation, access information, and deployment details.


### Example

* OAuth Authentication (OAuth2):

```python
import exalsius_api_client
from exalsius_api_client.models.workspace_response import WorkspaceResponse
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
    api_instance = exalsius_api_client.WorkspacesApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace to describe

    try:
        # Get details of a single workspace
        api_response = api_instance.describe_workspace(workspace_id)
        print("The response of WorkspacesApi->describe_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->describe_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| ID of the workspace to describe | 

### Return type

[**WorkspaceResponse**](WorkspaceResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A single workspace |  -  |
**404** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_workspaces**
> WorkspacesListResponse list_workspaces(cluster_id=cluster_id)

List all workspaces

**List all workspaces**

Retrieve all workspaces associated with your account. You can optionally filter workspaces by cluster ID
to see only workspaces deployed on a specific cluster.

**Filtering:**
- `cluster_id`: Filter workspaces by the cluster they are deployed on (UUID format)

**Examples**

Here's an example of how to filter by cluster ID:
```
/workspaces?cluster_id=123e4567-e89b-12d3-a456-426614174000
```


### Example

* OAuth Authentication (OAuth2):

```python
import exalsius_api_client
from exalsius_api_client.models.workspaces_list_response import WorkspacesListResponse
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
    api_instance = exalsius_api_client.WorkspacesApi(api_client)
    cluster_id = 'cluster_id_example' # str | Only return workspaces that are associated with this cluster.  (optional)

    try:
        # List all workspaces
        api_response = api_instance.list_workspaces(cluster_id=cluster_id)
        print("The response of WorkspacesApi->list_workspaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->list_workspaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Only return workspaces that are associated with this cluster.  | [optional] 

### Return type

[**WorkspacesListResponse**](WorkspacesListResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of workspaces |  * X-Total-Count - Total number of existing service templates <br>  |
**404** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_workspace**
> WorkspaceStartResponse start_workspace(workspace_id)

Start a workspace

**Start a workspace**

Start a workspace by bringing up all associated Pods and services. This can also mean that the workspace was previously stopped to save costs.

**Behavior:**
- All Pods associated with the workspace will be started
- The workspace status will transition to `RUNNING`
- Access information (ports, IPs) will be published (or restored if the workspace was previously stopped)
- Persistent volumes remain intact and data is preserved


### Example

* OAuth Authentication (OAuth2):

```python
import exalsius_api_client
from exalsius_api_client.models.workspace_start_response import WorkspaceStartResponse
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
    api_instance = exalsius_api_client.WorkspacesApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace to start

    try:
        # Start a workspace
        api_response = api_instance.start_workspace(workspace_id)
        print("The response of WorkspacesApi->start_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->start_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| ID of the workspace to start | 

### Return type

[**WorkspaceStartResponse**](WorkspaceStartResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Workspace start response |  -  |
**404** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_workspace**
> WorkspaceStopResponse stop_workspace(workspace_id)

Stop a workspace

**Stop a workspace**

Stop a running workspace by halting all associated Pods and services. This operation helps reduce
costs by stopping compute resources while preserving data. Note that this is only possible for selected workspace types.

**Behavior:**
- All Pods associated with the workspace will be stopped or terminated
- The workspace status will transition from `RUNNING` to `STOPPED`
- Persistent volumes remain attached and data is preserved
- Access information (ports, IPs) will be unavailable until the workspace is restarted
- The workspace can be restarted later using the `POST /workspace/{workspace_id}/start` endpoint


### Example

* OAuth Authentication (OAuth2):

```python
import exalsius_api_client
from exalsius_api_client.models.workspace_stop_response import WorkspaceStopResponse
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
    api_instance = exalsius_api_client.WorkspacesApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace to stop

    try:
        # Stop a workspace
        api_response = api_instance.stop_workspace(workspace_id)
        print("The response of WorkspacesApi->stop_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->stop_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| ID of the workspace to stop | 

### Return type

[**WorkspaceStopResponse**](WorkspaceStopResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Workspace stop response |  -  |
**404** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

