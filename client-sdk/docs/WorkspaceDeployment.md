# WorkspaceDeployment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** | The ID of the workspace | 
**workspace_name** | **str** | The name of the workspace | 
**workspace_template** | **str** | The name of the workspace template | 
**owner** | **str** | The owner of the workspace | 

## Example

```python
from exalsius_api_client.models.workspace_deployment import WorkspaceDeployment

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceDeployment from a JSON string
workspace_deployment_instance = WorkspaceDeployment.from_json(json)
# print the JSON string representation of the object
print(WorkspaceDeployment.to_json())

# convert the object into a dict
workspace_deployment_dict = workspace_deployment_instance.to_dict()
# create an instance of WorkspaceDeployment from a dict
workspace_deployment_from_dict = WorkspaceDeployment.from_dict(workspace_deployment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


