# exalsius-api-client
The exalsius REST API provides programmatic access to the core functionality of the exalsius ecosystem
It is consumed directly by the exls CLI tool and can also be integrated into custom applications or scripts.
Key points:
* **CLI & Programmatic Access**
  All operations are available via the `exls` command-line application or through standard HTTP requests.

* **GPU Market Offers** Retrieve and compare GPU instance pricing across public cloud providers and hyperscalers to identify the most cost-effective options.
* **Operator Integration**
  Works in conjunction with the [exalsius-operator](https://github.com/exalsius/exalsius-operator) deployed in a management Kubernetes cluster, to manage infrastructure and node lifecycles.

* **Node Management**
  Import self-managed (SSH) and cloud-provider instances into your node pool with dedicated endpoints.

* **Cluster Provisioning**
  Create and manage Kubernetes clusters across supported cloud providers and self-managed (bare-metal) nodes.

* **Service Deployment**
  Deploy additional services—such as the NVIDIA GPU Operator, KubeRay, Flyte, or Kubeflow—using the API’s service-deployment endpoints.


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.3.0
- Package version: 1.3.0
- Generator version: 7.13.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://exalsius.ai](https://exalsius.ai)

## Requirements.

Python 3.9+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import exalsius_api_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import exalsius_api_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
    cluster_id = 'cluster_id_example' # str | 
    cluster_add_service_request = exalsius_api_client.ClusterAddServiceRequest() # ClusterAddServiceRequest | 

    try:
        # Add service deployments to a cluster
        api_response = api_instance.add_cluster_services(cluster_id, cluster_add_service_request)
        print("The response of ClustersApi->add_cluster_services:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClustersApi->add_cluster_services: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.exalsius.ai/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ClustersApi* | [**add_cluster_services**](docs/ClustersApi.md#add_cluster_services) | **POST** /cluster/{cluster_id}/services | Add service deployments to a cluster
*ClustersApi* | [**add_nodes**](docs/ClustersApi.md#add_nodes) | **POST** /cluster/{cluster_id}/nodes | Add nodes to a cluster
*ClustersApi* | [**create_cluster**](docs/ClustersApi.md#create_cluster) | **POST** /clusters | Create a cluster
*ClustersApi* | [**delete_cluster**](docs/ClustersApi.md#delete_cluster) | **DELETE** /cluster/{cluster_id} | Delete (tear-down) a cluster
*ClustersApi* | [**delete_node_from_cluster**](docs/ClustersApi.md#delete_node_from_cluster) | **DELETE** /cluster/{cluster_id}/nodes/{node_id} | Delete a node from a cluster
*ClustersApi* | [**deploy_cluster**](docs/ClustersApi.md#deploy_cluster) | **POST** /cluster/{cluster_id}/deploy | Deploy a new cluster
*ClustersApi* | [**describe_cluster**](docs/ClustersApi.md#describe_cluster) | **GET** /cluster/{cluster_id} | Get details of a single cluster
*ClustersApi* | [**get_cluster_kubeconfig**](docs/ClustersApi.md#get_cluster_kubeconfig) | **GET** /cluster/{cluster_id}/kubeconfig | Get the kubeconfig for a cluster
*ClustersApi* | [**get_cluster_services**](docs/ClustersApi.md#get_cluster_services) | **GET** /cluster/{cluster_id}/services | Get services of a cluster
*ClustersApi* | [**get_nodes**](docs/ClustersApi.md#get_nodes) | **GET** /cluster/{cluster_id}/nodes | Get nodes of a cluster
*ClustersApi* | [**list_clusters**](docs/ClustersApi.md#list_clusters) | **GET** /clusters | List all clusters
*ManagementApi* | [**add_ssh_key**](docs/ManagementApi.md#add_ssh_key) | **POST** /management/ssh-keys | Add an SSH key
*ManagementApi* | [**delete_ssh_key**](docs/ManagementApi.md#delete_ssh_key) | **DELETE** /management/ssh-key/{ssh_key_id} | Delete an SSH key
*ManagementApi* | [**list_ssh_keys**](docs/ManagementApi.md#list_ssh_keys) | **GET** /management/ssh-keys | List all SSH keys
*NodesApi* | [**delete_node**](docs/NodesApi.md#delete_node) | **DELETE** /node/{node_id} | Delete a node from the pool
*NodesApi* | [**describe_node**](docs/NodesApi.md#describe_node) | **GET** /node/{node_id} | Get details of a single node in the node pool (self-managed or cloud)
*NodesApi* | [**import_node_from_offer**](docs/NodesApi.md#import_node_from_offer) | **POST** /node/import/offer/{offer_id} | Import a node from an offer
*NodesApi* | [**import_ssh**](docs/NodesApi.md#import_ssh) | **POST** /node/import/ssh | Import a self-managed node via SSH
*NodesApi* | [**list_nodes**](docs/NodesApi.md#list_nodes) | **GET** /nodes | List all imported nodes in the node pool
*OffersApi* | [**get_offers**](docs/OffersApi.md#get_offers) | **GET** /offers | List and filter current GPU on-demand and spot market offers
*ServicesApi* | [**list_available_services**](docs/ServicesApi.md#list_available_services) | **GET** /services | List all available services


## Documentation For Models

 - [BaseNode](docs/BaseNode.md)
 - [CloudNode](docs/CloudNode.md)
 - [Cluster](docs/Cluster.md)
 - [ClusterAddNodeRequest](docs/ClusterAddNodeRequest.md)
 - [ClusterAddServiceRequest](docs/ClusterAddServiceRequest.md)
 - [ClusterCreateRequest](docs/ClusterCreateRequest.md)
 - [ClusterCreateResponse](docs/ClusterCreateResponse.md)
 - [ClusterDeleteResponse](docs/ClusterDeleteResponse.md)
 - [ClusterDeployResponse](docs/ClusterDeployResponse.md)
 - [ClusterKubeconfigResponse](docs/ClusterKubeconfigResponse.md)
 - [ClusterNodeRemoveResponse](docs/ClusterNodeRemoveResponse.md)
 - [ClusterNodeToAdd](docs/ClusterNodeToAdd.md)
 - [ClusterNodesResponse](docs/ClusterNodesResponse.md)
 - [ClusterResponse](docs/ClusterResponse.md)
 - [ClusterServicesResponse](docs/ClusterServicesResponse.md)
 - [ClustersListResponse](docs/ClustersListResponse.md)
 - [Error](docs/Error.md)
 - [Kubeconfig](docs/Kubeconfig.md)
 - [NodeDeleteResponse](docs/NodeDeleteResponse.md)
 - [NodeImportResponse](docs/NodeImportResponse.md)
 - [NodeImportSshRequest](docs/NodeImportSshRequest.md)
 - [NodeResponse](docs/NodeResponse.md)
 - [NodesListResponse](docs/NodesListResponse.md)
 - [Offer](docs/Offer.md)
 - [OffersListResponse](docs/OffersListResponse.md)
 - [SelfManagedNode](docs/SelfManagedNode.md)
 - [Service](docs/Service.md)
 - [ServiceDeployment](docs/ServiceDeployment.md)
 - [ServicesListResponse](docs/ServicesListResponse.md)
 - [SshKey](docs/SshKey.md)
 - [SshKeyCreateRequest](docs/SshKeyCreateRequest.md)
 - [SshKeyCreateResponse](docs/SshKeyCreateResponse.md)
 - [SshKeysListResponse](docs/SshKeysListResponse.md)
 - [SshKeysListResponseSshKeysInner](docs/SshKeysListResponseSshKeysInner.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="ApiKeyAuth"></a>
### ApiKeyAuth

- **Type**: API key
- **API key parameter name**: X-API-Key
- **Location**: HTTP header


## Author

support@exalsius.ai


