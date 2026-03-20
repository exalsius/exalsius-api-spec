# SshKeyCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the SSH key | 
**private_key_b64** | **str** | The private key of the SSH key b64 encoded | 
**scope** | **str** | The visibility scope of the SSH key. &#39;private&#39; keys are only accessible by the owner. &#39;org&#39; keys are accessible by all members of the organization. | [optional] [default to 'private']

## Example

```python
from exalsius_api_client.models.ssh_key_create_request import SshKeyCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SshKeyCreateRequest from a JSON string
ssh_key_create_request_instance = SshKeyCreateRequest.from_json(json)
# print the JSON string representation of the object
print(SshKeyCreateRequest.to_json())

# convert the object into a dict
ssh_key_create_request_dict = ssh_key_create_request_instance.to_dict()
# create an instance of SshKeyCreateRequest from a dict
ssh_key_create_request_from_dict = SshKeyCreateRequest.from_dict(ssh_key_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


