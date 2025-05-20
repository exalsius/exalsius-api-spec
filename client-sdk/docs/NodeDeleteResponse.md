# NodeDeleteResponse

Node delete response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **int** |  | 

## Example

```python
from exalsius_api_client.models.node_delete_response import NodeDeleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NodeDeleteResponse from a JSON string
node_delete_response_instance = NodeDeleteResponse.from_json(json)
# print the JSON string representation of the object
print(NodeDeleteResponse.to_json())

# convert the object into a dict
node_delete_response_dict = node_delete_response_instance.to_dict()
# create an instance of NodeDeleteResponse from a dict
node_delete_response_from_dict = NodeDeleteResponse.from_dict(node_delete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


