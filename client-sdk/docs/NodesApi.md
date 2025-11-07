# exalsius_api_client.NodesApi

All URIs are relative to *https://api.exalsius.ai/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_node**](NodesApi.md#delete_node) | **DELETE** /node/{node_id} | Delete a node from the pool
[**describe_node**](NodesApi.md#describe_node) | **GET** /node/{node_id} | Get details of a single node in the node pool (self-managed or cloud)
[**import_node_from_offer**](NodesApi.md#import_node_from_offer) | **POST** /node/import/offer/{offer_id} | Import a node from an offer
[**import_ssh**](NodesApi.md#import_ssh) | **POST** /node/import/ssh | Import a self-managed node via SSH
[**list_nodes**](NodesApi.md#list_nodes) | **GET** /nodes | List all imported nodes in the node pool
[**patch_node**](NodesApi.md#patch_node) | **PATCH** /node/{node_id} | Patch a node


# **delete_node**
> NodeDeleteResponse delete_node(node_id)

Delete a node from the pool

**Delete a node from the pool**

Permanently delete a node from your node pool. This operation is only allowed when the node is in the 
`AVAILABLE` state.

**Warning: This operation is irreversible.**

**Prerequisites:**
- The node must be in the `AVAILABLE` state
- If the node is currently in use (i.e., not available), you must first detach it from its cluster

**Behavior:**
- The node will be permanently removed from your node pool
- Once deleted, the node cannot be used in any cluster deployments
- For cloud nodes, this does not terminate the instance; it only removes it from the pool
- For self-managed nodes, the node is simply removed from management


### Example

* OAuth Authentication (OAuth2):

```python
import exalsius_api_client
from exalsius_api_client.models.node_delete_response import NodeDeleteResponse
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
    api_instance = exalsius_api_client.NodesApi(api_client)
    node_id = 'node_id_example' # str | ID of the node to delete

    try:
        # Delete a node from the pool
        api_response = api_instance.delete_node(node_id)
        print("The response of NodesApi->delete_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodesApi->delete_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| ID of the node to delete | 

### Return type

[**NodeDeleteResponse**](NodeDeleteResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Node delete response |  -  |
**404** | Error response |  -  |
**409** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **describe_node**
> NodeResponse describe_node(node_id)

Get details of a single node in the node pool (self-managed or cloud)

**Retrieve the details of a single node in the node pool**

Fetch comprehensive metadata for a specific node in your pool. The response includes a `node_type` 
property to distinguish between self-managed (SSH) nodes and cloud-imported instances. The response 
structure varies based on the node type, with cloud nodes including pricing and instance information, 
while self-managed nodes include SSH connection details and heartbeat information.


### Example

* OAuth Authentication (OAuth2):

```python
import exalsius_api_client
from exalsius_api_client.models.node_response import NodeResponse
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
    api_instance = exalsius_api_client.NodesApi(api_client)
    node_id = 'node_id_example' # str | ID of the node to describe

    try:
        # Get details of a single node in the node pool (self-managed or cloud)
        api_response = api_instance.describe_node(node_id)
        print("The response of NodesApi->describe_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodesApi->describe_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| ID of the node to describe | 

### Return type

[**NodeResponse**](NodeResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A single node (self-managed or cloud) |  -  |
**404** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_node_from_offer**
> NodeImportResponse import_node_from_offer(offer_id, hostname=hostname, amount=amount)

Import a node from an offer

**Import cloud nodes into the pool**

Use this operation to import one or more nodes of a given cloud instance type into the node pool.

**Parameters**
  - `offer_id`: The identifier of the cloud provider's offer you wish to import (see GET /offers).
  - `amount`: The number of instances of the instance type to import.

**Behavior**

Importing a node from an offer to the node pool does not yet start a virtual machine and
therefore does not yet involve any costs. A virtual machine of the given instance type
will only be started when you deploy a cluster using the node.
The `price_per_hour` of the node will be the price of the offer at the time of import.
When deploying a cluster, the actual hourly rate will be the `price_per_hour` of the offer at that time.

**Result**

On success, you'll receive one or more node IDs. Use these IDs with the `/clusters` endpoint to add nodes to your clusters.


### Example

* OAuth Authentication (OAuth2):

```python
import exalsius_api_client
from exalsius_api_client.models.node_import_response import NodeImportResponse
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
    api_instance = exalsius_api_client.NodesApi(api_client)
    offer_id = 'offer_id_example' # str | 
    hostname = '' # str |  (optional) (default to '')
    amount = 1 # int |  (optional) (default to 1)

    try:
        # Import a node from an offer
        api_response = api_instance.import_node_from_offer(offer_id, hostname=hostname, amount=amount)
        print("The response of NodesApi->import_node_from_offer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodesApi->import_node_from_offer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **str**|  | 
 **hostname** | **str**|  | [optional] [default to &#39;&#39;]
 **amount** | **int**|  | [optional] [default to 1]

### Return type

[**NodeImportResponse**](NodeImportResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Nodes successfully imported |  -  |
**400** | Error response |  -  |
**404** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_ssh**
> NodeImportResponse import_ssh(node_import_ssh_request)

Import a self-managed node via SSH

**Import a self-managed node into the pool**

Use this operation to bring an existing server under SSH control into your node pool.
The node will be added to the node pool and will be available to select for a cluster deployment.

**Parameters**

In order to import a self-managed node, you need to provide the following information:
- The IP or hostname of the node with the SSH port (e.g. `192.168.1.1:22`)
- The username to access the node
- The ID of the SSH key to use for the node (see the SSH Keys endpoint)

**Behavior**

On success, the new node enters a `PENDING` state while we verify SSH connectivity and inspect its resources. This process may take up to 10 minutes; if it isn't ready by then, the import will fail. The node will transition to `AVAILABLE` once discovery is complete.

**Monitoring**
You can poll its status at any time via GET /node/{node_id}.

**Result**

Returns the generated node ID. Use that ID with the `/clusters` endpoint to include this node in your cluster deployments.


### Example

* OAuth Authentication (OAuth2):

```python
import exalsius_api_client
from exalsius_api_client.models.node_import_response import NodeImportResponse
from exalsius_api_client.models.node_import_ssh_request import NodeImportSshRequest
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
    api_instance = exalsius_api_client.NodesApi(api_client)
    node_import_ssh_request = {"hostname":"my-server-001","endpoint":"192.168.1.100:22","username":"ubuntu","ssh_key_id":"123e4567-e89b-12d3-a456-426614174000","description":"On-premises GPU server"} # NodeImportSshRequest | 

    try:
        # Import a self-managed node via SSH
        api_response = api_instance.import_ssh(node_import_ssh_request)
        print("The response of NodesApi->import_ssh:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodesApi->import_ssh: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_import_ssh_request** | [**NodeImportSshRequest**](NodeImportSshRequest.md)|  | 

### Return type

[**NodeImportResponse**](NodeImportResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Nodes successfully imported |  -  |
**400** | Error response |  -  |
**409** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_nodes**
> NodesListResponse list_nodes(node_type=node_type, provider=provider)

List all imported nodes in the node pool

**List nodes in the pool**

Retrieve all nodes in your node pool, including both self-managed (SSH) nodes and cloud-imported nodes.
Nodes can be filtered by type and provider to help you find specific nodes.

**Filtering:**
- `node_type`: Filter by node type - `CLOUD` for cloud-imported nodes or `SELF_MANAGED` for SSH-managed nodes
- `provider`: Filter by cloud provider (e.g., "aws", "azure", "gcp") - only applies to cloud nodes

**Examples**

Here's an example of how to filter by node type:
  ```
  /nodes?node_type=SELF_MANAGED
  ```
  
  Here's an example of how to filter by provider:
  ```
  /nodes?provider=aws
  ```


### Example

* OAuth Authentication (OAuth2):

```python
import exalsius_api_client
from exalsius_api_client.models.nodes_list_response import NodesListResponse
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
    api_instance = exalsius_api_client.NodesApi(api_client)
    node_type = 'node_type_example' # str | Only return nodes of this type.   Possible values: - `SELF_MANAGED` - only self-managed (SSH) nodes   - `CLOUD` - only cloud-imported nodes  (optional)
    provider = 'provider_example' # str | Only return nodes of this provider. Example: - `aws` - only AWS node instances  (optional)

    try:
        # List all imported nodes in the node pool
        api_response = api_instance.list_nodes(node_type=node_type, provider=provider)
        print("The response of NodesApi->list_nodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodesApi->list_nodes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_type** | **str**| Only return nodes of this type.   Possible values: - &#x60;SELF_MANAGED&#x60; - only self-managed (SSH) nodes   - &#x60;CLOUD&#x60; - only cloud-imported nodes  | [optional] 
 **provider** | **str**| Only return nodes of this provider. Example: - &#x60;aws&#x60; - only AWS node instances  | [optional] 

### Return type

[**NodesListResponse**](NodesListResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of nodes in the node pool |  * X-Total-Count - Total number of existing service templates <br>  |
**422** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_node**
> NodePatchResponse patch_node(node_id, node_patch_request=node_patch_request)

Patch a node

**Patch a node**

Update a node's properties or send a heartbeat signal. This endpoint is typically used by node agents 
to report status updates and maintain connectivity.

**Behavior:**
- If request body is provided, the node's properties (description, hardware specs) will be updated
- If no request body is provided, this acts as a heartbeat to indicate the node is still active
- For self-managed nodes, this updates the `last_heartbeat_date`
- Returns an access token that can be used for subsequent operations


### Example

* OAuth Authentication (OAuth2):

```python
import exalsius_api_client
from exalsius_api_client.models.node_patch_request import NodePatchRequest
from exalsius_api_client.models.node_patch_response import NodePatchResponse
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
    api_instance = exalsius_api_client.NodesApi(api_client)
    node_id = 'node_id_example' # str | 
    node_patch_request = exalsius_api_client.NodePatchRequest() # NodePatchRequest |  (optional)

    try:
        # Patch a node
        api_response = api_instance.patch_node(node_id, node_patch_request=node_patch_request)
        print("The response of NodesApi->patch_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodesApi->patch_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**|  | 
 **node_patch_request** | [**NodePatchRequest**](NodePatchRequest.md)|  | [optional] 

### Return type

[**NodePatchResponse**](NodePatchResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Node patch response |  -  |
**404** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

