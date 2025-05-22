# exalsius_api_client.ClustersApi

All URIs are relative to *https://api.exalsius.ai/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_cluster_services**](ClustersApi.md#add_cluster_services) | **POST** /cluster/{cluster_id}/services | Add service deployments to a cluster
[**add_nodes**](ClustersApi.md#add_nodes) | **POST** /cluster/{cluster_id}/nodes | Add nodes to a cluster
[**create_cluster**](ClustersApi.md#create_cluster) | **POST** /clusters | Create a cluster
[**delete_cluster**](ClustersApi.md#delete_cluster) | **DELETE** /cluster/{cluster_id} | Delete (tear-down) a cluster
[**delete_node_from_cluster**](ClustersApi.md#delete_node_from_cluster) | **DELETE** /cluster/{cluster_id}/nodes/{node_id} | Delete a node from a cluster
[**deploy_cluster**](ClustersApi.md#deploy_cluster) | **POST** /cluster/{cluster_id}/deploy | Deploy a new cluster
[**describe_cluster**](ClustersApi.md#describe_cluster) | **GET** /cluster/{cluster_id} | Get details of a single cluster
[**get_cluster_kubeconfig**](ClustersApi.md#get_cluster_kubeconfig) | **GET** /cluster/{cluster_id}/kubeconfig | Get the kubeconfig for a cluster
[**get_cluster_services**](ClustersApi.md#get_cluster_services) | **GET** /cluster/{cluster_id}/services | Get services of a cluster
[**get_nodes**](ClustersApi.md#get_nodes) | **GET** /cluster/{cluster_id}/nodes | Get nodes of a cluster
[**list_clusters**](ClustersApi.md#list_clusters) | **GET** /clusters | List all clusters


# **add_cluster_services**
> ClusterServicesResponse add_cluster_services(cluster_id, cluster_add_service_request)

Add service deployments to a cluster

**Add services to a cluster**

Add services to a cluster.

**Parameters**

- `clusterId`: The ID of the cluster to add services to.

**Request Body**

- `serviceDeployments`: An array of service deployments to be deployed to the cluster.    


### Example


```python
import exalsius_api_client
from exalsius_api_client.models.cluster_add_service_request import ClusterAddServiceRequest
from exalsius_api_client.models.cluster_services_response import ClusterServicesResponse
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
    api_instance = exalsius_api_client.ClustersApi(api_client)
    cluster_id = 56 # int | 
    cluster_add_service_request = exalsius_api_client.ClusterAddServiceRequest() # ClusterAddServiceRequest | 

    try:
        # Add service deployments to a cluster
        api_response = api_instance.add_cluster_services(cluster_id, cluster_add_service_request)
        print("The response of ClustersApi->add_cluster_services:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->add_cluster_services: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **cluster_add_service_request** | [**ClusterAddServiceRequest**](ClusterAddServiceRequest.md)|  | 

### Return type

[**ClusterServicesResponse**](ClusterServicesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | List of services in the cluster |  -  |
**400** | Invalid service deployments |  -  |
**404** | Cluster not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_nodes**
> ClusterNodesResponse add_nodes(cluster_id, node_ids, node_role=node_role)

Add nodes to a cluster

**Add nodes to a cluster**

Add nodes to a cluster.

**Parameters**

- `cluster_id`: The ID of the cluster to add nodes to
- `node_ids`: The IDs of the nodes to add
- `node_role`: The role of the nodes to add (optional). Possible values:
  - `control_plane` - only control plane nodes
  - `worker` - only worker nodes

If no `nodeRole` is provided, the nodes will be added as workers.

**Examples**

Here's an example of how to add a control plane node to a cluster:
  ```
  /clusters/123/nodes?node_ids=123&node_role=control_plane
  ```

**Note**

In the current version, only nodes of the same type (e.g. self-managed or from the same cloud region)
can be added to a cluster. Also, only nodes that are in the `available` state can be added to a cluster.

The nodes will be added to the cluster as soon as possible. However, it may take a few minutes
for the nodes to be fully deployed. The cluster will be in the `pending` state
until all nodes are fully deployed.

**Behavior**

In case the cluster is already deployed, the nodes will be added to the running cluster, otherwise the
cluster stays in the `pending` state until all the `/cluster/{clusterId}/deploy` operation is called.


### Example


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


# Enter a context with an instance of the API client
with exalsius_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = exalsius_api_client.ClustersApi(api_client)
    cluster_id = 56 # int | 
    node_ids = [56] # List[int] | 
    node_role = 'node_role_example' # str |  (optional)

    try:
        # Add nodes to a cluster
        api_response = api_instance.add_nodes(cluster_id, node_ids, node_role=node_role)
        print("The response of ClustersApi->add_nodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->add_nodes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **node_ids** | [**List[int]**](int.md)|  | 
 **node_role** | **str**|  | [optional] 

### Return type

[**ClusterNodesResponse**](ClusterNodesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of nodes in the cluster |  -  |
**400** | Invalid node_ids |  -  |
**404** | Cluster not found |  -  |
**409** | Nodes already in cluster |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cluster**
> ClusterCreateResponse create_cluster(cluster_create_request)

Create a cluster

**Create a cluster**

Create a new cluster.

**Parameters**

- `name`: The name of the cluster
- `k8s_version`: The Kubernetes version of the cluster
- `to_be_deleted_at`: The date and time the cluster will be deleted (optional)
- `control_plane_node_ids`: The IDs of the control plane nodes (optional)
- `worker_node_ids`: The IDs of the worker nodes (optional)
- `services`: The IDs of the services to deploy in the cluster (optional)

If `to_be_deleted_at` is provided, the cluster will automatically be deleted at the specified date and time.
If `control_plane_node_ids` or `worker_node_ids` are provided, the nodes will be added to the cluster.
If `services` are provided, the services will be deployed in the cluster.

**Behavior**

Creating a new cluster will result in a new cluster resource being created. The cluster will be in 
the `pending` state until the `POST /clusters/{cluster_id}/deploy` operation is called.


### Example


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


# Enter a context with an instance of the API client
with exalsius_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = exalsius_api_client.ClustersApi(api_client)
    cluster_create_request = exalsius_api_client.ClusterCreateRequest() # ClusterCreateRequest | 

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Cluster creation response |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cluster**
> delete_cluster(cluster_id)

Delete (tear-down) a cluster

**Delete a cluster**

Permanently delete a cluster. Once deleted, the cluster is no longer part of your 
account and cannot be used in any further deployments. When a cluster is deleted, the
nodes are returned to the node pool and can be used in future deployments.

**Note**

This operation is irreversible.

**Behavior**

The cluster will be deleted as soon as possible. However, it may take a few minutes
for the cluster to be fully deleted. The cluster will be in the `deleting` state
until it is fully deleted.


### Example


```python
import exalsius_api_client
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
    api_instance = exalsius_api_client.ClustersApi(api_client)
    cluster_id = 56 # int | ID of the cluster to delete

    try:
        # Delete (tear-down) a cluster
        api_instance.delete_cluster(cluster_id)
    except Exception as e:
        print("Exception when calling ClustersApi->delete_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**| ID of the cluster to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Cluster deleted; nodes returned to pool |  -  |
**404** | Cluster not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_node_from_cluster**
> ClusterNodeRemoveResponse delete_node_from_cluster(cluster_id, node_id)

Delete a node from a cluster

**Delete a node from a cluster**

Permanently delete a node from a cluster. Once deleted, the node is no longer part of the cluster
and is returned to the node pool.


### Example


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


# Enter a context with an instance of the API client
with exalsius_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = exalsius_api_client.ClustersApi(api_client)
    cluster_id = 56 # int | 
    node_id = 56 # int | 

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
 **cluster_id** | **int**|  | 
 **node_id** | **int**|  | 

### Return type

[**ClusterNodeRemoveResponse**](ClusterNodeRemoveResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Node removed from cluster |  -  |
**404** | Cluster not found |  -  |
**409** | Node not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deploy_cluster**
> ClusterDeployResponse deploy_cluster(cluster_id)

Deploy a new cluster

**Deploy a new cluster**

Deploy a cluster that is in the `staging` state.

**Note**

Only clusters with at least one node in the `controlPlaneNodeIds` and `workerNodeIds`
arrays can be deployed.

**Behavior**

The cluster will be deployed as soon as possible. However, it may take a few minutes
for the cluster to be fully deployed. The cluster will be in the `deploying` state
until it is fully deployed.

**Result**

Returns the cluster object with the `deploying` state.


### Example


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


# Enter a context with an instance of the API client
with exalsius_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = exalsius_api_client.ClustersApi(api_client)
    cluster_id = 56 # int | 

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
 **cluster_id** | **int**|  | 

### Return type

[**ClusterDeployResponse**](ClusterDeployResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Cluster deployment response |  -  |
**400** | Bad Request |  -  |
**404** | Cluster not found |  -  |
**409** | No nodes staged |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **describe_cluster**
> ClusterResponse describe_cluster(cluster_id)

Get details of a single cluster

**Retrieve the details of a single cluster**

Fetch all metadata for one cluster.


### Example


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


# Enter a context with an instance of the API client
with exalsius_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = exalsius_api_client.ClustersApi(api_client)
    cluster_id = 56 # int | ID of the cluster to describe

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
 **cluster_id** | **int**| ID of the cluster to describe | 

### Return type

[**ClusterResponse**](ClusterResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cluster details |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_kubeconfig**
> ClusterKubeconfigResponse get_cluster_kubeconfig(cluster_id)

Get the kubeconfig for a cluster

**Get the kubeconfig for a cluster**

Get the kubeconfig file for a cluster.


### Example


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


# Enter a context with an instance of the API client
with exalsius_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = exalsius_api_client.ClustersApi(api_client)
    cluster_id = 56 # int | The ID of the cluster to get the kubeconfig for

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
 **cluster_id** | **int**| The ID of the cluster to get the kubeconfig for | 

### Return type

[**ClusterKubeconfigResponse**](ClusterKubeconfigResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The kubeconfig file for a cluster |  -  |
**404** | Cluster not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_services**
> ClusterServicesResponse get_cluster_services(cluster_id)

Get services of a cluster

**Get services of a cluster**

Get all services deployed in a cluster.

**Result**

Returns an array of service IDs deployed in the cluster
To gather more information about a service, call the `GET /services/{serviceId}` endpoint.


### Example


```python
import exalsius_api_client
from exalsius_api_client.models.cluster_services_response import ClusterServicesResponse
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
    api_instance = exalsius_api_client.ClustersApi(api_client)
    cluster_id = 56 # int | 

    try:
        # Get services of a cluster
        api_response = api_instance.get_cluster_services(cluster_id)
        print("The response of ClustersApi->get_cluster_services:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->get_cluster_services: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 

### Return type

[**ClusterServicesResponse**](ClusterServicesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of services in the cluster |  -  |
**404** | Cluster not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nodes**
> ClusterNodesResponse get_nodes(cluster_id, node_role=node_role)

Get nodes of a cluster

**Retrieve the nodes of a cluster**

Fetch all nodes that are part of a cluster.

**Parameters**

- `cluster_id`: The ID of the cluster to retrieve nodes from
- `node_role`: Only return nodes of this role (optional). Possible values:
  - `control_plane`: only control plane nodes
  - `worker`: only worker nodes

**Examples**

Here's an example of how to retrieve all nodes of a cluster:
  ```
  /clusters/123/nodes
  ```

Here's an example of how to retrieve all control plane nodes of a cluster:
  ```
  /clusters/123/nodes?node_role=control_plane
  ```


### Example


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


# Enter a context with an instance of the API client
with exalsius_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = exalsius_api_client.ClustersApi(api_client)
    cluster_id = 56 # int | ID of the cluster to retrieve nodes from
    node_role = 'node_role_example' # str | Only return nodes of this role. Possible values: - `control_plane` - only control plane nodes - `worker` - only worker nodes  (optional)

    try:
        # Get nodes of a cluster
        api_response = api_instance.get_nodes(cluster_id, node_role=node_role)
        print("The response of ClustersApi->get_nodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->get_nodes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**| ID of the cluster to retrieve nodes from | 
 **node_role** | **str**| Only return nodes of this role. Possible values: - &#x60;control_plane&#x60; - only control plane nodes - &#x60;worker&#x60; - only worker nodes  | [optional] 

### Return type

[**ClusterNodesResponse**](ClusterNodesResponse.md)

### Authorization

No authorization required

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

Retrieve all clusters, with optional filters:
- `status`: pending,running, deleting, deleted, failed

**Examples**

Here's an example of how to filter by status:
  ```
  /clusters?cluster_status=running
  ```


### Example


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


# Enter a context with an instance of the API client
with exalsius_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = exalsius_api_client.ClustersApi(api_client)
    cluster_status = 'cluster_status_example' # str | Only return clusters of this status. Possible values: - `pending` - clusters that are pending - `running` - clusters that are running - `deleting` - clusters that are deleting - `deleted` - clusters that are deleted - `failed` - clusters that failed  (optional)

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
 **cluster_status** | **str**| Only return clusters of this status. Possible values: - &#x60;pending&#x60; - clusters that are pending - &#x60;running&#x60; - clusters that are running - &#x60;deleting&#x60; - clusters that are deleting - &#x60;deleted&#x60; - clusters that are deleted - &#x60;failed&#x60; - clusters that failed  | [optional] 

### Return type

[**ClustersListResponse**](ClustersListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of clusters |  -  |
**404** | Cluster not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

