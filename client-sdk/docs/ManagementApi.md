# exalsius_api_client.ManagementApi

All URIs are relative to *https://api.exalsius.ai/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_ssh_key**](ManagementApi.md#add_ssh_key) | **POST** /management/ssh-keys | Add an SSH key
[**delete_ssh_key**](ManagementApi.md#delete_ssh_key) | **DELETE** /management/ssh-key/{ssh_key_id} | Delete an SSH key
[**list_ssh_keys**](ManagementApi.md#list_ssh_keys) | **GET** /management/ssh-keys | List all SSH keys


# **add_ssh_key**
> SshKeyCreateResponse add_ssh_key(ssh_key_create_request)

Add an SSH key

**Add an SSH key**

Add an SSH key to the management cluster.

**Request Body**

- `name`: The name of the SSH key.
- `private_key`: The private key of the SSH key.

**Result**

Returns the SSH key object.


### Example


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


# Enter a context with an instance of the API client
with exalsius_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = exalsius_api_client.ManagementApi(api_client)
    ssh_key_create_request = exalsius_api_client.SshKeyCreateRequest() # SshKeyCreateRequest | 

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | SSH key creation response |  -  |
**400** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ssh_key**
> delete_ssh_key(ssh_key_id)

Delete an SSH key

**Delete an SSH key**

Delete an SSH key from the management cluster.

**Parameters**

- `ssh_key_id`: The ID of the SSH key to delete.


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

No authorization required

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

# **list_ssh_keys**
> SshKeysListResponse list_ssh_keys()

List all SSH keys

**List all SSH keys**

List all SSH keys that are available to the management cluster for the current user.

**Result**

Returns an array of SSH key objects.


### Example


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

No authorization required

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

