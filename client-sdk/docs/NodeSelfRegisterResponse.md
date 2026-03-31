# NodeSelfRegisterResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **str** | The ID of the node | 
**next_access_token** | **str** | The next access token for the node | [optional] 
**next_access_token_expires_in** | **int** | The number of seconds until the next access token expires | [optional] 
**next_access_token_type** | **str** | The type of the next access token | [optional] 

## Example

```python
from exalsius_api_client.models.node_self_register_response import NodeSelfRegisterResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NodeSelfRegisterResponse from a JSON string
node_self_register_response_instance = NodeSelfRegisterResponse.from_json(json)
# print the JSON string representation of the object
print(NodeSelfRegisterResponse.to_json())

# convert the object into a dict
node_self_register_response_dict = node_self_register_response_instance.to_dict()
# create an instance of NodeSelfRegisterResponse from a dict
node_self_register_response_from_dict = NodeSelfRegisterResponse.from_dict(node_self_register_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


