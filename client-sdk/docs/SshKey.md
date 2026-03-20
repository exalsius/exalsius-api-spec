# SshKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the SSH key | [optional] 
**name** | **str** | The name of the SSH key | 
**private_key** | **str** | The private key of the SSH key | 
**owner** | **str** | The owner of the SSH key | [optional] 
**namespace** | **str** | The namespace of the SSH key (organization namespace) | [optional] 
**scope** | **str** | The visibility scope of the SSH key. &#39;private&#39; keys are only accessible by the owner. &#39;org&#39; keys are accessible by all members of the organization. | [optional] [default to 'private']

## Example

```python
from exalsius_api_client.models.ssh_key import SshKey

# TODO update the JSON string below
json = "{}"
# create an instance of SshKey from a JSON string
ssh_key_instance = SshKey.from_json(json)
# print the JSON string representation of the object
print(SshKey.to_json())

# convert the object into a dict
ssh_key_dict = ssh_key_instance.to_dict()
# create an instance of SshKey from a dict
ssh_key_from_dict = SshKey.from_dict(ssh_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


