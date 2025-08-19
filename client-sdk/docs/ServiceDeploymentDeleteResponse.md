# ServiceDeploymentDeleteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_deployment_id** | **str** | The ID of the deleted service deployment | 

## Example

```python
from exalsius_api_client.models.service_deployment_delete_response import ServiceDeploymentDeleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceDeploymentDeleteResponse from a JSON string
service_deployment_delete_response_instance = ServiceDeploymentDeleteResponse.from_json(json)
# print the JSON string representation of the object
print(ServiceDeploymentDeleteResponse.to_json())

# convert the object into a dict
service_deployment_delete_response_dict = service_deployment_delete_response_instance.to_dict()
# create an instance of ServiceDeploymentDeleteResponse from a dict
service_deployment_delete_response_from_dict = ServiceDeploymentDeleteResponse.from_dict(service_deployment_delete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


