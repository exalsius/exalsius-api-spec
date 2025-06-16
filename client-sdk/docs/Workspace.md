# Workspace


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the workspace | [optional] 
**name** | **str** | The name of the workspace | 
**cluster_id** | **str** | The unique identifier of the associated cluster | 
**workspace_status** | **str** | The status of the workspace. - &#x60;PENDING&#x60;: Workspace is pending - &#x60;RUNNING&#x60;: Workspace is running - &#x60;STOPPED&#x60;: Workspace is stopped - &#x60;DELETED&#x60;: Workspace is deleted - &#x60;FAILED&#x60;: Workspace is failed  | [optional] 
**template** | [**WorkspaceTemplate**](WorkspaceTemplate.md) |  | 
**owner** | **str** | The owner of the workspace | [optional] 
**description** | **str** | The description of the workspace | [optional] 
**access_information** | **str** | Information about how to access the workspace | [optional] 
**resources** | [**ResourcePool**](ResourcePool.md) | The resources allocated to the workspace | 
**created_at** | **datetime** | The date and time the workspace was created | [optional] 
**to_be_deleted_at** | **datetime** | The date and time the workspace will be deleted | [optional] 

## Example

```python
from exalsius_api_client.models.workspace import Workspace

# TODO update the JSON string below
json = "{}"
# create an instance of Workspace from a JSON string
workspace_instance = Workspace.from_json(json)
# print the JSON string representation of the object
print(Workspace.to_json())

# convert the object into a dict
workspace_dict = workspace_instance.to_dict()
# create an instance of Workspace from a dict
workspace_from_dict = Workspace.from_dict(workspace_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


