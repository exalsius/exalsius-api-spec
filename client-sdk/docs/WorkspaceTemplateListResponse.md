# WorkspaceTemplateListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_templates** | [**List[WorkspaceTemplate]**](WorkspaceTemplate.md) |  | 
**total** | **int** | The total number of workspace templates | [optional] 

## Example

```python
from exalsius_api_client.models.workspace_template_list_response import WorkspaceTemplateListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceTemplateListResponse from a JSON string
workspace_template_list_response_instance = WorkspaceTemplateListResponse.from_json(json)
# print the JSON string representation of the object
print(WorkspaceTemplateListResponse.to_json())

# convert the object into a dict
workspace_template_list_response_dict = workspace_template_list_response_instance.to_dict()
# create an instance of WorkspaceTemplateListResponse from a dict
workspace_template_list_response_from_dict = WorkspaceTemplateListResponse.from_dict(workspace_template_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


