# NodeDeletedResponse

Node deleted from cluster

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **str** |  | 

## Example

```python
from exalsius_api_client.models.node_deleted_response import NodeDeletedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NodeDeletedResponse from a JSON string
node_deleted_response_instance = NodeDeletedResponse.from_json(json)
# print the JSON string representation of the object
print(NodeDeletedResponse.to_json())

# convert the object into a dict
node_deleted_response_dict = node_deleted_response_instance.to_dict()
# create an instance of NodeDeletedResponse from a dict
node_deleted_response_from_dict = NodeDeletedResponse.from_dict(node_deleted_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


