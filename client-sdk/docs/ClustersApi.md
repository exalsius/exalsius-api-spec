# exalsius_api_client.ClustersApi

All URIs are relative to *https://api.exalsius.ai/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_nodes**](ClustersApi.md#add_nodes) | **POST** /cluster/{cluster_id}/nodes | Add nodes to a cluster
[**adopt_cluster**](ClustersApi.md#adopt_cluster) | **POST** /clusters/adopt | Adopt a cluster
[**create_cluster**](ClustersApi.md#create_cluster) | **POST** /clusters | Create a cluster
[**delete_cluster**](ClustersApi.md#delete_cluster) | **DELETE** /cluster/{cluster_id} | Delete (tear-down) a cluster
[**delete_node_from_cluster**](ClustersApi.md#delete_node_from_cluster) | **DELETE** /cluster/{cluster_id}/nodes/{node_id} | Delete a node from a cluster
[**deploy_cluster**](ClustersApi.md#deploy_cluster) | **POST** /cluster/{cluster_id}/deploy | Deploy a new cluster
[**describe_cluster**](ClustersApi.md#describe_cluster) | **GET** /cluster/{cluster_id} | Get details of a single cluster
[**get_cluster_kubeconfig**](ClustersApi.md#get_cluster_kubeconfig) | **GET** /cluster/{cluster_id}/kubeconfig | Get the kubeconfig for a cluster
[**get_cluster_logs**](ClustersApi.md#get_cluster_logs) | **GET** /cluster/{cluster_id}/logs | Get cluster logs
[**get_cluster_resources**](ClustersApi.md#get_cluster_resources) | **GET** /cluster/{cluster_id}/resources | List available / occupied resources in the cluster
[**get_dashboard_auth**](ClustersApi.md#get_dashboard_auth) | **GET** /cluster/{cluster_id}/dashboard-auth | Get dashboard authentication
[**get_dashboard_url**](ClustersApi.md#get_dashboard_url) | **GET** /cluster/{cluster_id}/dashboard-url | Get dashboard URL
[**get_nodes**](ClustersApi.md#get_nodes) | **GET** /cluster/{cluster_id}/nodes | Get nodes of a cluster
[**list_clusters**](ClustersApi.md#list_clusters) | **GET** /clusters | List all clusters


# **add_nodes**
> ClusterNodesResponse add_nodes(cluster_id, cluster_add_node_request)

Add nodes to a cluster

**Add nodes to a cluster**

Add one or more nodes to an existing cluster. Nodes can be added as either control plane nodes or 
worker nodes, depending on your cluster's needs.

**Request Body:**
- `nodes_to_add`: Array of nodes to add, where each node has:
  - `node_id`: The ID of the node to add (required)
  - `node_role`: The role of the node (required). Possible values:
    - `CONTROL_PLANE` - control plane node (manages the cluster)
    - `WORKER` - worker node (runs workloads)

**Prerequisites:**
- Nodes must be in the `AVAILABLE` state
- Nodes must be of the same type (e.g., all self-managed or all from the same cloud region)
- For control plane nodes, you typically need an odd number (1, 3, 5) for high availability

**Behavior:**
- If the cluster is already deployed (`READY` state), nodes will be added to the running cluster
- If the cluster is in `PENDING` state, nodes will be associated but the cluster remains pending until deployment
- The node addition process may take several minutes to complete
- Once added, nodes become part of the cluster and can run workloads


### Example

* OAuth Authentication (OAuth2):

```python
import exalsius_api_client
from exalsius_api_client.models.cluster_add_node_request import ClusterAddNodeRequest
from exalsius_api_client.models.cluster_nodes_response import ClusterNodesResponse
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
    api_instance = exalsius_api_client.ClustersApi(api_client)
    cluster_id = 'cluster_id_example' # str | 
    cluster_add_node_request = {"nodes_to_add":[{"node_id":"123e4567-e89b-12d3-a456-426614174001","node_role":"CONTROL_PLANE"}]} # ClusterAddNodeRequest | 

    try:
        # Add nodes to a cluster
        api_response = api_instance.add_nodes(cluster_id, cluster_add_node_request)
        print("The response of ClustersApi->add_nodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->add_nodes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **cluster_add_node_request** | [**ClusterAddNodeRequest**](ClusterAddNodeRequest.md)|  | 

### Return type

[**ClusterNodesResponse**](ClusterNodesResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | List of nodes in the cluster |  -  |
**404** | Error response |  -  |
**409** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **adopt_cluster**
> ClusterCreateResponse adopt_cluster(cluster_adopt_request)

Adopt a cluster

**Adopt a cluster**

Adopt an existing Kubernetes cluster that is already running and managed outside of exalsius. This 
allows you to bring your own Kubernetes cluster under exalsius management, enabling you to use 
exalsius features like workspace provisioning, service deployment, and resource monitoring.

**Parameters:**
- `name`: A descriptive name for the adopted cluster
- `kubeconfig_b64`: The base64-encoded kubeconfig file for accessing the cluster
- `k8s_version`: The Kubernetes version of the cluster (optional, but recommended)
- `colony_id`: The ID of the colony to add the cluster to (optional)

**Behavior:**
- The cluster will be registered in exalsius and can be managed through the API
- You can deploy workspaces and services to the adopted cluster
- The cluster will appear in cluster listings and can be monitored like any other cluster
- The original cluster management remains unchanged; exalsius only manages workloads on the cluster


### Example

* OAuth Authentication (OAuth2):

```python
import exalsius_api_client
from exalsius_api_client.models.cluster_adopt_request import ClusterAdoptRequest
from exalsius_api_client.models.cluster_create_response import ClusterCreateResponse
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
    api_instance = exalsius_api_client.ClustersApi(api_client)
    cluster_adopt_request = {"name":"my-adopted-cluster","kubeconfig_b64":"YXBpVmVyc2lvbjogdjEKY2x1c3RlcnM6Ci0gY2x1c3RlcjoKICAgIHNlcnZlcjogaHR0cHM6Ly9hcGkuZXhhbHNpdXMuYWkvY2x1c3RlcnMvMTIz...","k8s_version":"1.30"} # ClusterAdoptRequest | 

    try:
        # Adopt a cluster
        api_response = api_instance.adopt_cluster(cluster_adopt_request)
        print("The response of ClustersApi->adopt_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->adopt_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_adopt_request** | [**ClusterAdoptRequest**](ClusterAdoptRequest.md)|  | 

### Return type

[**ClusterCreateResponse**](ClusterCreateResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Cluster adoption response |  -  |
**400** | Error response |  -  |
**409** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cluster**
> ClusterCreateResponse create_cluster(cluster_create_request)

Create a cluster

**Create a cluster**

Create a new cluster.

**Parameters**

- `name`: The name of the cluster (required)
- `cluster_type`: The type of cluster (required). Possible values: `CLOUD`, `REMOTE`, `ADOPTED`, `DOCKER`
- `vpn_cluster`: Whether the cluster should be provisioned with VPN connectivity (optional, defaults to `false`)
- `telemetry_enabled`: Enables observability/monitoring integrations for the cluster (optional, defaults to `false`)
- `colony_id`: The ID of the colony to add the cluster to (optional)
- `cluster_labels`: Arbitrary key/value labels applied to the cluster (optional)
- `machine_pre_start_commands`: Commands to run on each machine before the cluster starts (optional)
- `local_storage`: Local storage provisioner config. Supports `enabled` (bool, default `true`) and `basePath` (string) (optional)
- `k8s_version`: The Kubernetes version of the cluster (optional, defaults based on cluster type)
- `to_be_deleted_at`: The date and time the cluster will be deleted (optional)
- `control_plane_node_ids`: The IDs of the control plane nodes (optional)
- `worker_node_ids`: The IDs of the worker nodes (optional)
- `service_deployments`: The services to deploy in the cluster (optional)

If `to_be_deleted_at` is provided, the cluster will automatically be deleted at the specified date and time.
If `control_plane_node_ids` or `worker_node_ids` are provided, the nodes will be added to the cluster.
If `service_deployments` are provided, the services will be deployed in the cluster.
If `local_storage` is configured, the storage provisioner will adopt the supplied settings when the cluster becomes ready.

**Behavior:**
- A new cluster resource will be created with the specified configuration
- The cluster will be in the `PENDING` state until deployment is initiated
- You must call `POST /cluster/{cluster_id}/deploy` to actually deploy the cluster
- If nodes are specified, they will be associated with the cluster but not deployed until the deploy operation is called
- If `service_deployments` are specified, services will be deployed after the cluster is ready


### Example

* OAuth Authentication (OAuth2):

```python
import exalsius_api_client
from exalsius_api_client.models.cluster_create_request import ClusterCreateRequest
from exalsius_api_client.models.cluster_create_response import ClusterCreateResponse
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
    api_instance = exalsius_api_client.ClustersApi(api_client)
    cluster_create_request = {"name":"my-cloud-cluster","cluster_type":"CLOUD","k8s_version":"1.30","control_plane_node_ids":["123e4567-e89b-12d3-a456-426614174000"],"worker_node_ids":["123e4567-e89b-12d3-a456-426614174001","123e4567-e89b-12d3-a456-426614174002"]} # ClusterCreateRequest | 

    try:
        # Create a cluster
        api_response = api_instance.create_cluster(cluster_create_request)
        print("The response of ClustersApi->create_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->create_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_create_request** | [**ClusterCreateRequest**](ClusterCreateRequest.md)|  | 

### Return type

[**ClusterCreateResponse**](ClusterCreateResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Cluster creation response |  -  |
**400** | Error response |  -  |
**409** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cluster**
> ClusterDeleteResponse delete_cluster(cluster_id, propagate=propagate)

Delete (tear-down) a cluster

**Delete a cluster**

Permanently delete a cluster and tear down all associated infrastructure. This operation will 
terminate all resources running on the cluster, including workspaces and services.

**Warning: This operation is irreversible.**

**Behavior:**
- The cluster will be deleted as soon as possible
- The deletion process may take several minutes to complete
- The cluster will transition to the `DELETING` state during the process
- Once deleted, nodes are returned to the node pool and can be reused in future deployments
- All workspaces and services running on the cluster will be terminated

**Parameters:**
- `propagate`: If `true`, the deletion will also remove nodes from the node pool (default: `false`)


### Example

* OAuth Authentication (OAuth2):

```python
import exalsius_api_client
from exalsius_api_client.models.cluster_delete_response import ClusterDeleteResponse
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
    api_instance = exalsius_api_client.ClustersApi(api_client)
    cluster_id = 'cluster_id_example' # str | ID of the cluster to delete
    propagate = False # bool | Whether to propagate the deletion to all nodes in the given cluster (optional) (default to False)

    try:
        # Delete (tear-down) a cluster
        api_response = api_instance.delete_cluster(cluster_id, propagate=propagate)
        print("The response of ClustersApi->delete_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->delete_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| ID of the cluster to delete | 
 **propagate** | **bool**| Whether to propagate the deletion to all nodes in the given cluster | [optional] [default to False]

### Return type

[**ClusterDeleteResponse**](ClusterDeleteResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cluster deletion response |  -  |
**404** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_node_from_cluster**
> ClusterNodeRemoveResponse delete_node_from_cluster(cluster_id, node_id)

Delete a node from a cluster

**Delete a node from a cluster**

Remove a node from a cluster and return it to the node pool. This operation is useful for scaling 
down a cluster or replacing nodes.

**Behavior:**
- The node will be gracefully removed from the cluster
- Any workloads running on the node will be rescheduled to other nodes (if available)
- The node will be returned to the node pool and can be reused in other clusters
- The removal process may take several minutes to complete
- The cluster will continue operating with the remaining nodes

**Note:**
- Removing control plane nodes may affect cluster availability if you remove too many
- Ensure you have sufficient remaining nodes to handle your workloads
- The operation returns a 202 status code as it is asynchronous


### Example

* OAuth Authentication (OAuth2):

```python
import exalsius_api_client
from exalsius_api_client.models.cluster_node_remove_response import ClusterNodeRemoveResponse
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
    api_instance = exalsius_api_client.ClustersApi(api_client)
    cluster_id = 'cluster_id_example' # str | 
    node_id = 'node_id_example' # str | 

    try:
        # Delete a node from a cluster
        api_response = api_instance.delete_node_from_cluster(cluster_id, node_id)
        print("The response of ClustersApi->delete_node_from_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->delete_node_from_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **node_id** | **str**|  | 

### Return type

[**ClusterNodeRemoveResponse**](ClusterNodeRemoveResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Node removed from cluster |  -  |
**404** | Error response |  -  |
**409** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deploy_cluster**
> ClusterDeployResponse deploy_cluster(cluster_id)

Deploy a new cluster

**Deploy a new cluster**

Initiate the deployment of a cluster that is in the `PENDING` state. This operation will start 
the Kubernetes cluster deployment process, configuring all nodes and setting up the cluster 
infrastructure.

**Prerequisites:**
- The cluster must be in the `PENDING` state
- The cluster must have at least one control plane node and one worker node assigned
- All assigned nodes must be in the `AVAILABLE` state

**Behavior:**
- The cluster deployment will begin as soon as possible
- The cluster will transition to the `DEPLOYING` state
- The deployment process may take several minutes to complete
- Once deployment completes, the cluster will transition to the `READY` state
- If deployment fails, the cluster will transition to the `FAILED` state

**Response:**
Returns the cluster ID to confirm the deployment has been initiated.


### Example

* OAuth Authentication (OAuth2):

```python
import exalsius_api_client
from exalsius_api_client.models.cluster_deploy_response import ClusterDeployResponse
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
    api_instance = exalsius_api_client.ClustersApi(api_client)
    cluster_id = 'cluster_id_example' # str | 

    try:
        # Deploy a new cluster
        api_response = api_instance.deploy_cluster(cluster_id)
        print("The response of ClustersApi->deploy_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->deploy_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

### Return type

[**ClusterDeployResponse**](ClusterDeployResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Cluster deployment response |  -  |
**400** | Error response |  -  |
**404** | Error response |  -  |
**409** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **describe_cluster**
> ClusterResponse describe_cluster(cluster_id)

Get details of a single cluster

**Retrieve the details of a single cluster**

Fetch comprehensive metadata for a specific cluster, including its status, node configuration, 
Kubernetes version, associated services, cost information, and lifecycle timestamps. This information 
helps you understand the cluster's current state and configuration.


### Example

* OAuth Authentication (OAuth2):

```python
import exalsius_api_client
from exalsius_api_client.models.cluster_response import ClusterResponse
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
    api_instance = exalsius_api_client.ClustersApi(api_client)
    cluster_id = 'cluster_id_example' # str | ID of the cluster to describe

    try:
        # Get details of a single cluster
        api_response = api_instance.describe_cluster(cluster_id)
        print("The response of ClustersApi->describe_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->describe_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| ID of the cluster to describe | 

### Return type

[**ClusterResponse**](ClusterResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cluster details |  -  |
**404** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_kubeconfig**
> ClusterKubeconfigResponse get_cluster_kubeconfig(cluster_id)

Get the kubeconfig for a cluster

**Get the kubeconfig for a cluster**

Retrieve the kubeconfig file that provides access to the cluster. The kubeconfig contains 
authentication credentials and cluster connection information, allowing you to manage the 
cluster using standard Kubernetes tools (kubectl, etc.).

**Usage:**
- Save the kubeconfig to a file and set it as your `KUBECONFIG` environment variable
- Use `kubectl` or other Kubernetes tools to interact with the cluster directly
- This is useful for advanced cluster management and debugging
- The kubeconfig is cluster-specific and provides full access to the cluster


### Example

* OAuth Authentication (OAuth2):

```python
import exalsius_api_client
from exalsius_api_client.models.cluster_kubeconfig_response import ClusterKubeconfigResponse
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
    api_instance = exalsius_api_client.ClustersApi(api_client)
    cluster_id = 'cluster_id_example' # str | The ID of the cluster to get the kubeconfig for

    try:
        # Get the kubeconfig for a cluster
        api_response = api_instance.get_cluster_kubeconfig(cluster_id)
        print("The response of ClustersApi->get_cluster_kubeconfig:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->get_cluster_kubeconfig: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The ID of the cluster to get the kubeconfig for | 

### Return type

[**ClusterKubeconfigResponse**](ClusterKubeconfigResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The kubeconfig file for a cluster |  -  |
**404** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_logs**
> ClusterEventPayload get_cluster_logs(cluster_id)

Get cluster logs

**Retrieve the cluster logs**

Retrieve the logs for a specific cluster. The logs are returned in real-time as they are generated. This endpoint returns a NDJSON stream, so individual log objects are separated by a newline character.


### Example

* OAuth Authentication (OAuth2):

```python
import exalsius_api_client
from exalsius_api_client.models.cluster_event_payload import ClusterEventPayload
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
    api_instance = exalsius_api_client.ClustersApi(api_client)
    cluster_id = 'cluster_id_example' # str | The ID of the cluster to get the logs for

    try:
        # Get cluster logs
        api_response = api_instance.get_cluster_logs(cluster_id)
        print("The response of ClustersApi->get_cluster_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->get_cluster_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The ID of the cluster to get the logs for | 

### Return type

[**ClusterEventPayload**](ClusterEventPayload.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/x-ndjson, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cluster logs response |  -  |
**404** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_resources**
> ClusterResourcesListResponse get_cluster_resources(cluster_id)

List available / occupied resources in the cluster

**List available / occupied resources in the cluster**

Retrieve detailed resource information for all nodes in the cluster, showing both available and 
occupied resources (CPU, memory, storage, GPU). This information helps you understand cluster 
capacity, utilization, and plan for workload placement.

**Response:**
Returns a list of nodes with their resource information, including:
- Available resources: CPU cores, memory (GB), storage (GB), GPU count and type
- Occupied resources: Currently used resources on each node
- Total resource counts across the cluster


### Example

* OAuth Authentication (OAuth2):

```python
import exalsius_api_client
from exalsius_api_client.models.cluster_resources_list_response import ClusterResourcesListResponse
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
    api_instance = exalsius_api_client.ClustersApi(api_client)
    cluster_id = 'cluster_id_example' # str | ID of the cluster to list resources for

    try:
        # List available / occupied resources in the cluster
        api_response = api_instance.get_cluster_resources(cluster_id)
        print("The response of ClustersApi->get_cluster_resources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->get_cluster_resources: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| ID of the cluster to list resources for | 

### Return type

[**ClusterResourcesListResponse**](ClusterResourcesListResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of available / occupied resources in the cluster |  -  |
**404** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboard_auth**
> get_dashboard_auth(cluster_id)

Get dashboard authentication

**Retrieve the dashboard authentication**

Enables access to observability dashboards for a specific cluster. Each dashboard provides a visual representation 
of cluster performance metrics, resource utilization, and operational insights.


### Example

* OAuth Authentication (OAuth2):

```python
import exalsius_api_client
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
    api_instance = exalsius_api_client.ClustersApi(api_client)
    cluster_id = 'cluster_id_example' # str | The ID of the cluster to get the dashboard authentication for

    try:
        # Get dashboard authentication
        api_instance.get_dashboard_auth(cluster_id)
    except Exception as e:
        print("Exception when calling ClustersApi->get_dashboard_auth: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The ID of the cluster to get the dashboard authentication for | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dashboard authentication |  * X-WEBAUTH-USER - User ID of the user <br>  * X-WEBAUTH-TEAM - Team ID of the user <br>  * X-WEBAUTH-CLUSTER - Cluster ID of the cluster <br>  * X-WEBAUTH-ROLE - Grafana role of the user <br>  * X-WEBAUTH-BEARER - Bearer token of the user <br>  |
**404** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboard_url**
> ClusterDashboardUrlResponse get_dashboard_url(cluster_id)

Get dashboard URL

**Retrieve the URL to cluster-scoped Grafana dashboards**

Returns the URL to cluster-scoped Grafana dashboards for a specific cluster.


### Example

* OAuth Authentication (OAuth2):

```python
import exalsius_api_client
from exalsius_api_client.models.cluster_dashboard_url_response import ClusterDashboardUrlResponse
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
    api_instance = exalsius_api_client.ClustersApi(api_client)
    cluster_id = 'cluster_id_example' # str | ID of the cluster to get the dashboard URL for

    try:
        # Get dashboard URL
        api_response = api_instance.get_dashboard_url(cluster_id)
        print("The response of ClustersApi->get_dashboard_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->get_dashboard_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| ID of the cluster to get the dashboard URL for | 

### Return type

[**ClusterDashboardUrlResponse**](ClusterDashboardUrlResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cluster dashboard URL response |  -  |
**404** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nodes**
> ClusterNodesResponse get_nodes(cluster_id)

Get nodes of a cluster

**Retrieve the nodes of a cluster**

Fetch all nodes that are part of a specific cluster, including both control plane and worker nodes. 
This endpoint provides information about the cluster's node composition, which is useful for 
understanding cluster capacity and configuration.

**Examples**

Here's an example of how to retrieve all nodes of a cluster:
  ```
  /cluster/123e4567-e89b-12d3-a456-426614174000/nodes
  ```


### Example

* OAuth Authentication (OAuth2):

```python
import exalsius_api_client
from exalsius_api_client.models.cluster_nodes_response import ClusterNodesResponse
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
    api_instance = exalsius_api_client.ClustersApi(api_client)
    cluster_id = 'cluster_id_example' # str | ID of the cluster to retrieve nodes from

    try:
        # Get nodes of a cluster
        api_response = api_instance.get_nodes(cluster_id)
        print("The response of ClustersApi->get_nodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->get_nodes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| ID of the cluster to retrieve nodes from | 

### Return type

[**ClusterNodesResponse**](ClusterNodesResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of nodes in the cluster |  -  |
**404** | Cluster not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_clusters**
> ClustersListResponse list_clusters(cluster_status=cluster_status)

List all clusters

**List all clusters**

Retrieve all clusters associated with your account. You can filter clusters by their status to find 
clusters in specific states (PENDING, DEPLOYING, READY, or FAILED). This endpoint is useful for 
monitoring cluster health and managing your infrastructure.

**Examples**

Here's an example of how to filter by status:
  ```
  /clusters?cluster_status=READY
  ```


### Example

* OAuth Authentication (OAuth2):

```python
import exalsius_api_client
from exalsius_api_client.models.clusters_list_response import ClustersListResponse
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
    api_instance = exalsius_api_client.ClustersApi(api_client)
    cluster_status = 'cluster_status_example' # str | Only return clusters of this status. Possible values: - `PENDING` - clusters that are pending (not yet deployed) - `DEPLOYING` - clusters that are being deployed - `READY` - clusters that are ready - `FAILED` - clusters that failed  (optional)

    try:
        # List all clusters
        api_response = api_instance.list_clusters(cluster_status=cluster_status)
        print("The response of ClustersApi->list_clusters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->list_clusters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_status** | **str**| Only return clusters of this status. Possible values: - &#x60;PENDING&#x60; - clusters that are pending (not yet deployed) - &#x60;DEPLOYING&#x60; - clusters that are being deployed - &#x60;READY&#x60; - clusters that are ready - &#x60;FAILED&#x60; - clusters that failed  | [optional] 

### Return type

[**ClustersListResponse**](ClustersListResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of clusters |  -  |
**404** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

