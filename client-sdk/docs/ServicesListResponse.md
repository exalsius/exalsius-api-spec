# ServicesListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**services** | [**List[ServiceDeployment]**](ServiceDeployment.md) |  | 
**total** | **int** | The total number of services | [optional] 

## Example

```python
from exalsius_api_client.models.services_list_response import ServicesListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ServicesListResponse from a JSON string
services_list_response_instance = ServicesListResponse.from_json(json)
# print the JSON string representation of the object
print(ServicesListResponse.to_json())

# convert the object into a dict
services_list_response_dict = services_list_response_instance.to_dict()
# create an instance of ServicesListResponse from a dict
services_list_response_from_dict = ServicesListResponse.from_dict(services_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


