# NodeImportResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_ids** | **List[str]** |  | 
**total** | **int** | The total number of nodes that were imported | 

## Example

```python
from exalsius_api_client.models.node_import_response import NodeImportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NodeImportResponse from a JSON string
node_import_response_instance = NodeImportResponse.from_json(json)
# print the JSON string representation of the object
print(NodeImportResponse.to_json())

# convert the object into a dict
node_import_response_dict = node_import_response_instance.to_dict()
# create an instance of NodeImportResponse from a dict
node_import_response_from_dict = NodeImportResponse.from_dict(node_import_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


