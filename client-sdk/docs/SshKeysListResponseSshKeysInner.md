# SshKeysListResponseSshKeysInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the SSH key | [optional] 
**name** | **str** | The name of the SSH key | [optional] 

## Example

```python
from exalsius_api_client.models.ssh_keys_list_response_ssh_keys_inner import SshKeysListResponseSshKeysInner

# TODO update the JSON string below
json = "{}"
# create an instance of SshKeysListResponseSshKeysInner from a JSON string
ssh_keys_list_response_ssh_keys_inner_instance = SshKeysListResponseSshKeysInner.from_json(json)
# print the JSON string representation of the object
print(SshKeysListResponseSshKeysInner.to_json())

# convert the object into a dict
ssh_keys_list_response_ssh_keys_inner_dict = ssh_keys_list_response_ssh_keys_inner_instance.to_dict()
# create an instance of SshKeysListResponseSshKeysInner from a dict
ssh_keys_list_response_ssh_keys_inner_from_dict = SshKeysListResponseSshKeysInner.from_dict(ssh_keys_list_response_ssh_keys_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


