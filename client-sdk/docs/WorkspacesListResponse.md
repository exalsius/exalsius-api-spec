# WorkspacesListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspaces** | [**List[Workspace]**](Workspace.md) |  | 
**total** | **int** | The total number of workspaces | [optional] 

## Example

```python
from exalsius_api_client.models.workspaces_list_response import WorkspacesListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspacesListResponse from a JSON string
workspaces_list_response_instance = WorkspacesListResponse.from_json(json)
# print the JSON string representation of the object
print(WorkspacesListResponse.to_json())

# convert the object into a dict
workspaces_list_response_dict = workspaces_list_response_instance.to_dict()
# create an instance of WorkspacesListResponse from a dict
workspaces_list_response_from_dict = WorkspacesListResponse.from_dict(workspaces_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


