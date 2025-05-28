# ServiceDeployment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **int** | The ID of the service | 
**service_name** | **str** | The name of the service | [optional] 
**values** | **Dict[str, str]** | The values to set for the service | [optional] 

## Example

```python
from exalsius_api_client.models.service_deployment import ServiceDeployment

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceDeployment from a JSON string
service_deployment_instance = ServiceDeployment.from_json(json)
# print the JSON string representation of the object
print(ServiceDeployment.to_json())

# convert the object into a dict
service_deployment_dict = service_deployment_instance.to_dict()
# create an instance of ServiceDeployment from a dict
service_deployment_from_dict = ServiceDeployment.from_dict(service_deployment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


