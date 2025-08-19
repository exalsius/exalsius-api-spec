# ServiceCreateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_deployment_id** | **str** | The ID of the created service deployment | 

## Example

```python
from exalsius_api_client.models.service_create_response import ServiceCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCreateResponse from a JSON string
service_create_response_instance = ServiceCreateResponse.from_json(json)
# print the JSON string representation of the object
print(ServiceCreateResponse.to_json())

# convert the object into a dict
service_create_response_dict = service_create_response_instance.to_dict()
# create an instance of ServiceCreateResponse from a dict
service_create_response_from_dict = ServiceCreateResponse.from_dict(service_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


