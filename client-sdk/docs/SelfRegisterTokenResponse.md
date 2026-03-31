# SelfRegisterTokenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**register_token** | **str** | The token used by a node agent to call &#x60;POST /node/self-register&#x60;. | 

## Example

```python
from exalsius_api_client.models.self_register_token_response import SelfRegisterTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SelfRegisterTokenResponse from a JSON string
self_register_token_response_instance = SelfRegisterTokenResponse.from_json(json)
# print the JSON string representation of the object
print(SelfRegisterTokenResponse.to_json())

# convert the object into a dict
self_register_token_response_dict = self_register_token_response_instance.to_dict()
# create an instance of SelfRegisterTokenResponse from a dict
self_register_token_response_from_dict = SelfRegisterTokenResponse.from_dict(self_register_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


