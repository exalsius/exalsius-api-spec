# NodePatchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **str** | The ID of the node | 
**next_access_token** | **str** | The next access token for the node | [optional] 
**next_access_token_expires_in** | **int** | The number of seconds until the next access token expires | [optional] 
**next_access_token_type** | **str** | The type of the next access token | [optional] 

## Example

```python
from exalsius_api_client.models.node_patch_response import NodePatchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NodePatchResponse from a JSON string
node_patch_response_instance = NodePatchResponse.from_json(json)
# print the JSON string representation of the object
print(NodePatchResponse.to_json())

# convert the object into a dict
node_patch_response_dict = node_patch_response_instance.to_dict()
# create an instance of NodePatchResponse from a dict
node_patch_response_from_dict = NodePatchResponse.from_dict(node_patch_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


