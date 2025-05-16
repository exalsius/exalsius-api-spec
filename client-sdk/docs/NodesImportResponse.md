# NodesImportResponse

Nodes successfully imported

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_ids** | **List[str]** |  | [optional] 
**total** | **int** | The total number of nodes that were imported | [optional] 

## Example

```python
from exalsius_api_client.models.nodes_import_response import NodesImportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NodesImportResponse from a JSON string
nodes_import_response_instance = NodesImportResponse.from_json(json)
# print the JSON string representation of the object
print(NodesImportResponse.to_json())

# convert the object into a dict
nodes_import_response_dict = nodes_import_response_instance.to_dict()
# create an instance of NodesImportResponse from a dict
nodes_import_response_from_dict = NodesImportResponse.from_dict(nodes_import_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


