# WorkspaceCreateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** | The ID of the created workspace | 

## Example

```python
from exalsius_api_client.models.workspace_create_response import WorkspaceCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceCreateResponse from a JSON string
workspace_create_response_instance = WorkspaceCreateResponse.from_json(json)
# print the JSON string representation of the object
print(WorkspaceCreateResponse.to_json())

# convert the object into a dict
workspace_create_response_dict = workspace_create_response_instance.to_dict()
# create an instance of WorkspaceCreateResponse from a dict
workspace_create_response_from_dict = WorkspaceCreateResponse.from_dict(workspace_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


