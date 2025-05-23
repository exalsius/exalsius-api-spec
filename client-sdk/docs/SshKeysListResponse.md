# SshKeysListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ssh_keys** | [**List[SshKeysListResponseSshKeysInner]**](SshKeysListResponseSshKeysInner.md) |  | 
**total** | **int** | The total number of SSH keys | 

## Example

```python
from exalsius_api_client.models.ssh_keys_list_response import SshKeysListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SshKeysListResponse from a JSON string
ssh_keys_list_response_instance = SshKeysListResponse.from_json(json)
# print the JSON string representation of the object
print(SshKeysListResponse.to_json())

# convert the object into a dict
ssh_keys_list_response_dict = ssh_keys_list_response_instance.to_dict()
# create an instance of SshKeysListResponse from a dict
ssh_keys_list_response_from_dict = SshKeysListResponse.from_dict(ssh_keys_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


