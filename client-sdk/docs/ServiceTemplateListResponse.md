# ServiceTemplateListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_templates** | [**List[ServiceTemplate]**](ServiceTemplate.md) |  | 
**total** | **int** | The total number of service templates | [optional] 

## Example

```python
from exalsius_api_client.models.service_template_list_response import ServiceTemplateListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceTemplateListResponse from a JSON string
service_template_list_response_instance = ServiceTemplateListResponse.from_json(json)
# print the JSON string representation of the object
print(ServiceTemplateListResponse.to_json())

# convert the object into a dict
service_template_list_response_dict = service_template_list_response_instance.to_dict()
# create an instance of ServiceTemplateListResponse from a dict
service_template_list_response_from_dict = ServiceTemplateListResponse.from_dict(service_template_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


