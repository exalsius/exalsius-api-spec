# SelfRegisterToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**register_token** | **str** | The token used by a node agent to call &#x60;POST /node/self-register&#x60;. | 
**owner** | **str** | The owner of the token | 
**org_namespace** | **str** | The organization namespace of the token | 

## Example

```python
from exalsius_api_client.models.self_register_token import SelfRegisterToken

# TODO update the JSON string below
json = "{}"
# create an instance of SelfRegisterToken from a JSON string
self_register_token_instance = SelfRegisterToken.from_json(json)
# print the JSON string representation of the object
print(SelfRegisterToken.to_json())

# convert the object into a dict
self_register_token_dict = self_register_token_instance.to_dict()
# create an instance of SelfRegisterToken from a dict
self_register_token_from_dict = SelfRegisterToken.from_dict(self_register_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


