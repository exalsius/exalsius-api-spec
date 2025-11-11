# exalsius_api_client.ManagementApi

All URIs are relative to *https://api.exalsius.ai/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_ssh_key**](ManagementApi.md#add_ssh_key) | **POST** /management/ssh-keys | Add an SSH key
[**delete_ssh_key**](ManagementApi.md#delete_ssh_key) | **DELETE** /management/ssh-key/{ssh_key_id} | Delete an SSH key
[**get_dashboard_auth**](ManagementApi.md#get_dashboard_auth) | **GET** /management/dashboard-auth | Get dashboard authentication
[**list_cluster_templates**](ManagementApi.md#list_cluster_templates) | **GET** /management/cluster-templates | List all cluster templates
[**list_credentials**](ManagementApi.md#list_credentials) | **GET** /management/credentials | List all cloud provider credentials
[**list_service_templates**](ManagementApi.md#list_service_templates) | **GET** /management/service-templates | List all available service templates
[**list_ssh_keys**](ManagementApi.md#list_ssh_keys) | **GET** /management/ssh-keys | List all SSH keys
[**list_workspace_templates**](ManagementApi.md#list_workspace_templates) | **GET** /management/workspace-templates | List all workspace templates


# **add_ssh_key**
> SshKeyCreateResponse add_ssh_key(ssh_key_create_request)

Add an SSH key

**Add an SSH key**

Add a new SSH key to your account. SSH keys are required for importing self-managed nodes via SSH. 
The private key must be provided in base64-encoded format.

**Request Body:**
- `name`: A descriptive name for the SSH key (e.g., "my-server-key")
- `private_key_b64`: The private SSH key, base64 encoded. This should be the private key that corresponds 
  to a public key installed on the target node(s)

**Result:**
Returns the created SSH key object with its unique identifier. Use this ID when importing self-managed 
nodes via the `POST /node/import/ssh` endpoint.

**Security Note:**
The private key is stored securely and is never returned in subsequent API calls. Only the key ID and 
name are accessible after creation.


### Example

* OAuth Authentication (OAuth2):

```python
import exalsius_api_client
from exalsius_api_client.models.ssh_key_create_request import SshKeyCreateRequest
from exalsius_api_client.models.ssh_key_create_response import SshKeyCreateResponse
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
    api_instance = exalsius_api_client.ManagementApi(api_client)
    ssh_key_create_request = {"name":"my-ssh-key","private_key_b64":"LS0tLS1CRUdJTiBPUEVOU1NIIFBSSVZBVEUgS0VZLS0tLS0KYjNCbGJuTnphQzFyWlhrdGRqRUFBQUFBQkc1dmJtVUFBQUFFYm05..."} # SshKeyCreateRequest | 

    try:
        # Add an SSH key
        api_response = api_instance.add_ssh_key(ssh_key_create_request)
        print("The response of ManagementApi->add_ssh_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementApi->add_ssh_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ssh_key_create_request** | [**SshKeyCreateRequest**](SshKeyCreateRequest.md)|  | 

### Return type

[**SshKeyCreateResponse**](SshKeyCreateResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | SSH key creation response |  -  |
**422** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ssh_key**
> delete_ssh_key(ssh_key_id)

Delete an SSH key

**Delete an SSH key**

Permanently delete an SSH key from your account. This operation is irreversible.

**Warning: This operation is irreversible.**

**Behavior:**
- The SSH key will be permanently removed from your account
- Any nodes that were imported using this SSH key will continue to function, but you won't be able to 
  use this key for future node imports
- If you need to import new nodes, you'll need to create a new SSH key


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
    api_instance = exalsius_api_client.ManagementApi(api_client)
    ssh_key_id = 'ssh_key_id_example' # str | ID of the SSH key to delete

    try:
        # Delete an SSH key
        api_instance.delete_ssh_key(ssh_key_id)
    except Exception as e:
        print("Exception when calling ManagementApi->delete_ssh_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ssh_key_id** | **str**| ID of the SSH key to delete | 

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
**204** | SSH key deleted |  -  |
**404** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboard_auth**
> get_dashboard_auth()

Get dashboard authentication

**Retrieve the dashboard authentication**

Enables access to observability dashboards for all clusters associated with the user. Each dashboard provides a visual representation 
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
    api_instance = exalsius_api_client.ManagementApi(api_client)

    try:
        # Get dashboard authentication
        api_instance.get_dashboard_auth()
    except Exception as e:
        print("Exception when calling ManagementApi->get_dashboard_auth: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**200** | Dashboard authentication |  * X-WEBAUTH-USER - User ID of the user <br>  * X-WEBAUTH-TEAM - Team ID of the user <br>  * X-WEBAUTH-ROLE - Role of the user <br>  * X-WEBAUTH-EMAIL - Email of the user <br>  |
**404** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cluster_templates**
> ClusterTemplateListResponse list_cluster_templates()

List all cluster templates

**List all available cluster templates**

Retrieve all cluster templates available in the management cluster. Cluster templates define the 
configuration and Kubernetes version for new cluster deployments.

**Usage:**
Cluster templates are used when creating new clusters via the `POST /clusters` endpoint. Each template 
specifies the Kubernetes version and deployment configuration that will be applied to new clusters.

**Result:**
Returns an array of cluster template objects, each containing the template name, description, and 
Kubernetes version.


### Example

* OAuth Authentication (OAuth2):

```python
import exalsius_api_client
from exalsius_api_client.models.cluster_template_list_response import ClusterTemplateListResponse
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
    api_instance = exalsius_api_client.ManagementApi(api_client)

    try:
        # List all cluster templates
        api_response = api_instance.list_cluster_templates()
        print("The response of ManagementApi->list_cluster_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementApi->list_cluster_templates: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ClusterTemplateListResponse**](ClusterTemplateListResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of available cluster templates |  -  |
**404** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_credentials**
> CredentialsListResponse list_credentials()

List all cloud provider credentials

**List all available credentials**

Retrieve all cloud provider credentials associated with your account. Credentials are used to authenticate 
with cloud providers when importing nodes or deploying clusters.

**Result:**
Returns an array of credential objects containing metadata (name, description, provider type) but never 
the actual credential values for security reasons.


### Example

* OAuth Authentication (OAuth2):

```python
import exalsius_api_client
from exalsius_api_client.models.credentials_list_response import CredentialsListResponse
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
    api_instance = exalsius_api_client.ManagementApi(api_client)

    try:
        # List all cloud provider credentials
        api_response = api_instance.list_credentials()
        print("The response of ManagementApi->list_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementApi->list_credentials: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CredentialsListResponse**](CredentialsListResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of available credentials |  -  |
**404** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_service_templates**
> ServiceTemplateListResponse list_service_templates()

List all available service templates

**List all available service templates**

Retrieve all service templates available in the management cluster. Service templates define infrastructure 
services (such as Ray clusters, monitoring systems, etc.) that can be deployed on clusters.

**Usage:**
Service templates are used when creating new service deployments via the `POST /services` endpoint. 
Each template specifies the service type and configuration variables that can be customized.

**Note:**
Service templates can be added to the exalsius management cluster using the `exalsius-operator`.

**Result:**
Returns an array of service template objects, each containing the template name, description, and 
available configuration variables.


### Example

* OAuth Authentication (OAuth2):

```python
import exalsius_api_client
from exalsius_api_client.models.service_template_list_response import ServiceTemplateListResponse
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
    api_instance = exalsius_api_client.ManagementApi(api_client)

    try:
        # List all available service templates
        api_response = api_instance.list_service_templates()
        print("The response of ManagementApi->list_service_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementApi->list_service_templates: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ServiceTemplateListResponse**](ServiceTemplateListResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of service templates |  * X-Total-Count - Total number of existing service templates <br>  |
**404** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ssh_keys**
> SshKeysListResponse list_ssh_keys()

List all SSH keys

**List all SSH keys**

Retrieve all SSH keys associated with your account. SSH keys are used to authenticate with self-managed 
nodes when importing them via SSH. Each SSH key has a unique identifier that can be used when importing nodes.

**Result:**
Returns an array of SSH key objects, each containing the key ID and name. The private key itself is never 
returned for security reasons.


### Example

* OAuth Authentication (OAuth2):

```python
import exalsius_api_client
from exalsius_api_client.models.ssh_keys_list_response import SshKeysListResponse
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
    api_instance = exalsius_api_client.ManagementApi(api_client)

    try:
        # List all SSH keys
        api_response = api_instance.list_ssh_keys()
        print("The response of ManagementApi->list_ssh_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementApi->list_ssh_keys: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SshKeysListResponse**](SshKeysListResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of SSH keys |  -  |
**404** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_workspace_templates**
> WorkspaceTemplateListResponse list_workspace_templates()

List all workspace templates

**List all workspace templates**

Retrieve all workspace templates available in the management cluster. Workspace templates define the 
application configuration and environment setup for new workspace deployments.

**Usage:**
Workspace templates are used when creating new workspaces via the `POST /workspaces` endpoint. Each 
template specifies the application type (e.g., Jupyter Notebook, VS Code Server) and configuration 
variables that can be customized.

**Result:**
Returns an array of workspace template objects, each containing the template name, description, and 
available configuration variables.


### Example

* OAuth Authentication (OAuth2):

```python
import exalsius_api_client
from exalsius_api_client.models.workspace_template_list_response import WorkspaceTemplateListResponse
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
    api_instance = exalsius_api_client.ManagementApi(api_client)

    try:
        # List all workspace templates
        api_response = api_instance.list_workspace_templates()
        print("The response of ManagementApi->list_workspace_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementApi->list_workspace_templates: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**WorkspaceTemplateListResponse**](WorkspaceTemplateListResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of workspace templates |  * X-Total-Count - Total number of existing service templates <br>  |
**404** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

