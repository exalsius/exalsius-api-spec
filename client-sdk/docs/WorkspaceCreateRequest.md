# WorkspaceCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the workspace | 
**cluster_id** | **str** | The unique identifier of the associated cluster | 
**template** | [**WorkspaceTemplate**](WorkspaceTemplate.md) |  | 
**resources** | [**ResourcePool**](ResourcePool.md) | The resources allocated to the workspace | 
**description** | **str** | The description of the workspace | [optional] 
**to_be_deleted_at** | **datetime** | The date and time the workspace will be deleted | [optional] 

## Example

```python
from exalsius_api_client.models.workspace_create_request import WorkspaceCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceCreateRequest from a JSON string
workspace_create_request_instance = WorkspaceCreateRequest.from_json(json)
# print the JSON string representation of the object
print(WorkspaceCreateRequest.to_json())

# convert the object into a dict
workspace_create_request_dict = workspace_create_request_instance.to_dict()
# create an instance of WorkspaceCreateRequest from a dict
workspace_create_request_from_dict = WorkspaceCreateRequest.from_dict(workspace_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


