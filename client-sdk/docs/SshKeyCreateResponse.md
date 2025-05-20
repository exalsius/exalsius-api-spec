# SshKeyCreateResponse

SSH key creation response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ssh_key_id** | **int** | The ID of the created SSH key | 

## Example

```python
from exalsius_api_client.models.ssh_key_create_response import SshKeyCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SshKeyCreateResponse from a JSON string
ssh_key_create_response_instance = SshKeyCreateResponse.from_json(json)
# print the JSON string representation of the object
print(SshKeyCreateResponse.to_json())

# convert the object into a dict
ssh_key_create_response_dict = ssh_key_create_response_instance.to_dict()
# create an instance of SshKeyCreateResponse from a dict
ssh_key_create_response_from_dict = SshKeyCreateResponse.from_dict(ssh_key_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


