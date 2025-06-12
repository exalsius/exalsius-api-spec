# NodesListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nodes** | [**List[NodeResponse]**](NodeResponse.md) |  | 
**total** | **int** | Total number of nodes in the current result set | 

## Example

```python
from exalsius_api_client.models.nodes_list_response import NodesListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NodesListResponse from a JSON string
nodes_list_response_instance = NodesListResponse.from_json(json)
# print the JSON string representation of the object
print(NodesListResponse.to_json())

# convert the object into a dict
nodes_list_response_dict = nodes_list_response_instance.to_dict()
# create an instance of NodesListResponse from a dict
nodes_list_response_from_dict = NodesListResponse.from_dict(nodes_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


