# WorkspaceTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the workspace template | 
**description** | **str** | The description of the workspace template | [optional] 
**variables** | **Dict[str, str]** | The variables of the workspace template | 

## Example

```python
from exalsius_api_client.models.workspace_template import WorkspaceTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceTemplate from a JSON string
workspace_template_instance = WorkspaceTemplate.from_json(json)
# print the JSON string representation of the object
print(WorkspaceTemplate.to_json())

# convert the object into a dict
workspace_template_dict = workspace_template_instance.to_dict()
# create an instance of WorkspaceTemplate from a dict
workspace_template_from_dict = WorkspaceTemplate.from_dict(workspace_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


