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

Create a new service deployment.

**Parameters**

- `name`: The name of the service deployment
- `cluster_id`: The ID of the cluster to deploy the service to
- `template`: The service template to use for the service deployment


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
    service_deployment_create_request = exalsius_api_client.ServiceDeploymentCreateRequest() # ServiceDeploymentCreateRequest | 

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

Delete a service deployment.


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
    service_deployment_id = 'service_deployment_id_example' # str | ID of the workspace to describe

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
 **service_deployment_id** | **str**| ID of the workspace to describe | 

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

Retrieve all service deployments, with optional filters:
- `cluster_id`: filter by cluster ID


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
**200** | List of services |  * X-Total-Count - Total number of existing service deployments <br>  |
**404** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

