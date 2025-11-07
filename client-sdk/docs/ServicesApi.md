# exalsius_api_client.ServicesApi

All URIs are relative to *https://api.exalsius.ai/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_service_deployment**](ServicesApi.md#create_service_deployment) | **POST** /services | Create a service deployment
[**delete_service_deployment**](ServicesApi.md#delete_service_deployment) | **DELETE** /service/{service_deployment_id} | Delete a service deployment
[**describe_service_deployment**](ServicesApi.md#describe_service_deployment) | **GET** /service/{service_deployment_id} | Get details of a single service deployment
[**list_services_deployments**](ServicesApi.md#list_services_deployments) | **GET** /services | List all service deployments


# **create_service_deployment**
> ServiceCreateResponse create_service_deployment(service_deployment_create_request)

Create a service deployment

**Create a service deployment**

Create a new infrastructure service deployment on a cluster. Service deployments are reusable infrastructure
components such as distributed computing frameworks (Ray), monitoring systems (Prometheus), or other
cluster-level services.

**Parameters:**
- `name`: The name of the service deployment (must be unique within the cluster)
- `cluster_id`: The ID of the cluster to deploy the service to
- `template`: The service template to use, including template name and configuration variables

**Behavior:**
Creating a new service deployment will result in a new service resource being created on the specified cluster.
The service will be deployed according to the template configuration and variables provided.


### Example

* OAuth Authentication (OAuth2):

```python
import exalsius_api_client
from exalsius_api_client.models.service_create_response import ServiceCreateResponse
from exalsius_api_client.models.service_deployment_create_request import ServiceDeploymentCreateRequest
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
    api_instance = exalsius_api_client.ServicesApi(api_client)
    service_deployment_create_request = {"name":"my-ray-cluster","cluster_id":"123e4567-e89b-12d3-a456-426614174000","template":{"name":"ray-deployment","variables":{"ray_cluster_name":"my-ray-cluster","config":{"replicas":3,"resources":{"cpu":"2","memory":"4Gi"}},"enabled":true}},"description":"Ray cluster for distributed machine learning","namespace":"default"} # ServiceDeploymentCreateRequest | 

    try:
        # Create a service deployment
        api_response = api_instance.create_service_deployment(service_deployment_create_request)
        print("The response of ServicesApi->create_service_deployment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->create_service_deployment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_deployment_create_request** | [**ServiceDeploymentCreateRequest**](ServiceDeploymentCreateRequest.md)|  | 

### Return type

[**ServiceCreateResponse**](ServiceCreateResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Service deployment creation response |  -  |
**400** | Error response |  -  |
**409** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_service_deployment**
> ServiceDeleteResponse delete_service_deployment(service_deployment_id)

Delete a service deployment

**Delete a service deployment**

Permanently delete a service deployment and remove all associated resources from the cluster.

**Warning: This operation is irreversible.**

**Behavior:**
- The service deployment will be marked for deletion immediately
- All associated Pods, Services, and other Kubernetes resources will be terminated
- The deletion process may take a few minutes to complete
- Once deleted, the service deployment cannot be recovered


### Example

* OAuth Authentication (OAuth2):

```python
import exalsius_api_client
from exalsius_api_client.models.service_delete_response import ServiceDeleteResponse
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
    api_instance = exalsius_api_client.ServicesApi(api_client)
    service_deployment_id = 'service_deployment_id_example' # str | ID of the service deployment to delete

    try:
        # Delete a service deployment
        api_response = api_instance.delete_service_deployment(service_deployment_id)
        print("The response of ServicesApi->delete_service_deployment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->delete_service_deployment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_deployment_id** | **str**| ID of the service deployment to delete | 

### Return type

[**ServiceDeleteResponse**](ServiceDeleteResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Service deployment deletion response |  -  |
**404** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **describe_service_deployment**
> ServiceResponse describe_service_deployment(service_deployment_id)

Get details of a single service deployment

**Retrieve the details of a single service deployment**

Fetch comprehensive metadata for a specific service deployment, including its configuration, template details,
cluster association, owner information, and creation timestamp.


### Example

* OAuth Authentication (OAuth2):

```python
import exalsius_api_client
from exalsius_api_client.models.service_response import ServiceResponse
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
    api_instance = exalsius_api_client.ServicesApi(api_client)
    service_deployment_id = 'service_deployment_id_example' # str | ID of the service deployment to describe

    try:
        # Get details of a single service deployment
        api_response = api_instance.describe_service_deployment(service_deployment_id)
        print("The response of ServicesApi->describe_service_deployment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->describe_service_deployment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_deployment_id** | **str**| ID of the service deployment to describe | 

### Return type

[**ServiceResponse**](ServiceResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A single service deployment |  -  |
**404** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_services_deployments**
> ServicesListResponse list_services_deployments(cluster_id=cluster_id)

List all service deployments

**List all service deployments**

Retrieve all service deployments associated with your account. Service deployments are infrastructure
services (such as Ray clusters, monitoring services, etc.) that are deployed on your clusters.
You can optionally filter service deployments by cluster ID to see only services deployed on a specific cluster.

**Filtering:**
- `cluster_id`: Filter service deployments by the cluster they are deployed on (UUID format)


### Example

* OAuth Authentication (OAuth2):

```python
import exalsius_api_client
from exalsius_api_client.models.services_list_response import ServicesListResponse
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
    api_instance = exalsius_api_client.ServicesApi(api_client)
    cluster_id = 'cluster_id_example' # str | Only return services that are associated with this cluster.  (optional)

    try:
        # List all service deployments
        api_response = api_instance.list_services_deployments(cluster_id=cluster_id)
        print("The response of ServicesApi->list_services_deployments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->list_services_deployments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Only return services that are associated with this cluster.  | [optional] 

### Return type

[**ServicesListResponse**](ServicesListResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of services |  * X-Total-Count - Total number of existing service templates <br>  |
**404** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

