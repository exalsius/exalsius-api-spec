# exalsius_api_client.WorkspacesApi

All URIs are relative to *https://api.exalsius.ai/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_workspace**](WorkspacesApi.md#create_workspace) | **POST** /workspaces | Create a workspace
[**delete_workspace**](WorkspacesApi.md#delete_workspace) | **DELETE** /workspace/{workspace_id} | Delete a workspace
[**describe_workspace**](WorkspacesApi.md#describe_workspace) | **GET** /workspace/{workspace_id} | Get details of a single workspace
[**list_workspaces**](WorkspacesApi.md#list_workspaces) | **GET** /workspaces | List all workspaces
[**stop_workspace**](WorkspacesApi.md#stop_workspace) | **POST** /workspace/{workspace_id}/stop | Stop a workspace


# **create_workspace**
> WorkspaceCreateResponse create_workspace(workspace)

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
the `pending` state until the `GET /workspace/{workspace_id}` operation is returning another state.


### Example


```python
import exalsius_api_client
from exalsius_api_client.models.workspace import Workspace
from exalsius_api_client.models.workspace_create_response import WorkspaceCreateResponse
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
    api_instance = exalsius_api_client.WorkspacesApi(api_client)
    workspace = exalsius_api_client.Workspace() # Workspace | 

    try:
        # Create a workspace
        api_response = api_instance.create_workspace(workspace)
        print("The response of WorkspacesApi->create_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->create_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | [**Workspace**](Workspace.md)|  | 

### Return type

[**WorkspaceCreateResponse**](WorkspaceCreateResponse.md)

### Authorization

No authorization required

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

Delete a workspace. 

**Note**

This operation is irreversible.

**Behavior**

The workspace will be deleted as soon as possible. However, it may take a few minutes
for the workspace to be fully deleted.


### Example


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

No authorization required

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
> Workspace describe_workspace(workspace_id)

Get details of a single workspace

**Retrieve the details of a single workspace**

Fetch all metadata for one workspace.


### Example


```python
import exalsius_api_client
from exalsius_api_client.models.workspace import Workspace
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

[**Workspace**](Workspace.md)

### Authorization

No authorization required

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

Retrieve all workspaces, with optional filters:
- `cluster_id`: filter by cluster ID

**Examples**

Here's an example of how to filter by cluster ID:
```
/workspaces?cluster_id=123
```


### Example


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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of workspaces |  * X-Total-Count - Total number of existing workspaces <br>  |
**404** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_workspace**
> WorkspaceStopResponse stop_workspace(workspace_id)

Stop a workspace

**Stop a workspace**

Stop a workspace. This will stop or delete all associated Pods but keep the attached persistent volume.


### Example


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

No authorization required

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

