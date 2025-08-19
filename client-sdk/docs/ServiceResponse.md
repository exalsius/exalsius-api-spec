# ServiceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_deployment** | [**Service**](Service.md) |  | 

## Example

```python
from exalsius_api_client.models.service_response import ServiceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceResponse from a JSON string
service_response_instance = ServiceResponse.from_json(json)
# print the JSON string representation of the object
print(ServiceResponse.to_json())

# convert the object into a dict
service_response_dict = service_response_instance.to_dict()
# create an instance of ServiceResponse from a dict
service_response_from_dict = ServiceResponse.from_dict(service_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


