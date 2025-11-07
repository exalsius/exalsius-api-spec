# ServiceDeploymentCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the service deployment | 
**cluster_id** | **str** | The unique identifier of the associated cluster | 
**template** | [**ServiceTemplate**](ServiceTemplate.md) |  | 
**namespace** | **str** | The namespace in which the service should be deployed in the target cluster | [optional] 
**description** | **str** | The description of the service deployment | [optional] 
**to_be_deleted_at** | **datetime** | The date and time the service deployment will be deleted | [optional] 

## Example

```python
from exalsius_api_client.models.service_deployment_create_request import ServiceDeploymentCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceDeploymentCreateRequest from a JSON string
service_deployment_create_request_instance = ServiceDeploymentCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ServiceDeploymentCreateRequest.to_json())

# convert the object into a dict
service_deployment_create_request_dict = service_deployment_create_request_instance.to_dict()
# create an instance of ServiceDeploymentCreateRequest from a dict
service_deployment_create_request_from_dict = ServiceDeploymentCreateRequest.from_dict(service_deployment_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


