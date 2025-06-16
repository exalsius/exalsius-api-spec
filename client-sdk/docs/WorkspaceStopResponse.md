# WorkspaceStopResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** | The ID of the stopped workspace | 

## Example

```python
from exalsius_api_client.models.workspace_stop_response import WorkspaceStopResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceStopResponse from a JSON string
workspace_stop_response_instance = WorkspaceStopResponse.from_json(json)
# print the JSON string representation of the object
print(WorkspaceStopResponse.to_json())

# convert the object into a dict
workspace_stop_response_dict = workspace_stop_response_instance.to_dict()
# create an instance of WorkspaceStopResponse from a dict
workspace_stop_response_from_dict = WorkspaceStopResponse.from_dict(workspace_stop_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


