# WorkspaceLogPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pod_name** | **str** | The name of the pod | 
**pod_namespace** | **str** | The namespace of the pod | [optional] 
**timestamp** | **datetime** | The timestamp of the log | 
**log_message** | **str** | The message of the log | 

## Example

```python
from exalsius_api_client.models.workspace_log_payload import WorkspaceLogPayload

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceLogPayload from a JSON string
workspace_log_payload_instance = WorkspaceLogPayload.from_json(json)
# print the JSON string representation of the object
print(WorkspaceLogPayload.to_json())

# convert the object into a dict
workspace_log_payload_dict = workspace_log_payload_instance.to_dict()
# create an instance of WorkspaceLogPayload from a dict
workspace_log_payload_from_dict = WorkspaceLogPayload.from_dict(workspace_log_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


