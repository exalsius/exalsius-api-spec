# ServiceDeploymentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_deployment** | [**ServiceDeployment**](ServiceDeployment.md) |  | 

## Example

```python
from exalsius_api_client.models.service_deployment_response import ServiceDeploymentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceDeploymentResponse from a JSON string
service_deployment_response_instance = ServiceDeploymentResponse.from_json(json)
# print the JSON string representation of the object
print(ServiceDeploymentResponse.to_json())

# convert the object into a dict
service_deployment_response_dict = service_deployment_response_instance.to_dict()
# create an instance of ServiceDeploymentResponse from a dict
service_deployment_response_from_dict = ServiceDeploymentResponse.from_dict(service_deployment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


