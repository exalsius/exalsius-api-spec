# NodeResponse

A single node, either self-managed or cloud

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node** | [**NodeResponseNode**](NodeResponseNode.md) |  | [optional] 

## Example

```python
from exalsius_api_client.models.node_response import NodeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NodeResponse from a JSON string
node_response_instance = NodeResponse.from_json(json)
# print the JSON string representation of the object
print(NodeResponse.to_json())

# convert the object into a dict
node_response_dict = node_response_instance.to_dict()
# create an instance of NodeResponse from a dict
node_response_from_dict = NodeResponse.from_dict(node_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


