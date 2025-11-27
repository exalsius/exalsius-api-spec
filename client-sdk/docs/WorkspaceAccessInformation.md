# WorkspaceAccessInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_type** | **str** | The type of access information. - &#x60;NODE_PORT&#x60;: Node port access information  | 
**access_description** | **str** | A description for the access type | [optional] 
**access_protocol** | **str** | The protocol of the access type - &#x60;TCP&#x60;: TCP protocol, e.g. for SSH access - &#x60;HTTP&#x60;: HTTP protocol, e.g. for Jupyter Notebook UI access - &#x60;HTTPS&#x60;: HTTPS protocol, e.g. for Jupyter Notebook UI access  | 
**port_name** | **str** | The port name | [optional] 
**port_number** | **int** | The port number | 
**external_ip** | **str** | The external IP address associated with the port | [optional] 

## Example

```python
from exalsius_api_client.models.workspace_access_information import WorkspaceAccessInformation

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceAccessInformation from a JSON string
workspace_access_information_instance = WorkspaceAccessInformation.from_json(json)
# print the JSON string representation of the object
print(WorkspaceAccessInformation.to_json())

# convert the object into a dict
workspace_access_information_dict = workspace_access_information_instance.to_dict()
# create an instance of WorkspaceAccessInformation from a dict
workspace_access_information_from_dict = WorkspaceAccessInformation.from_dict(workspace_access_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


