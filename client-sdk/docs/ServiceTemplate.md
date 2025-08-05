# ServiceTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the service template | 
**description** | **str** | The description of the service template | [optional] 
**variables** | **Dict[str, str]** | The variables of the service template | 

## Example

```python
from exalsius_api_client.models.service_template import ServiceTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceTemplate from a JSON string
service_template_instance = ServiceTemplate.from_json(json)
# print the JSON string representation of the object
print(ServiceTemplate.to_json())

# convert the object into a dict
service_template_dict = service_template_instance.to_dict()
# create an instance of ServiceTemplate from a dict
service_template_from_dict = ServiceTemplate.from_dict(service_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


