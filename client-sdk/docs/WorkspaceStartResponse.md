# WorkspaceStartResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** | The ID of the started workspace | 

## Example

```python
from exalsius_api_client.models.workspace_start_response import WorkspaceStartResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceStartResponse from a JSON string
workspace_start_response_instance = WorkspaceStartResponse.from_json(json)
# print the JSON string representation of the object
print(WorkspaceStartResponse.to_json())

# convert the object into a dict
workspace_start_response_dict = workspace_start_response_instance.to_dict()
# create an instance of WorkspaceStartResponse from a dict
workspace_start_response_from_dict = WorkspaceStartResponse.from_dict(workspace_start_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


