# ClusterTemplateListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_templates** | [**List[ClusterTemplate]**](ClusterTemplate.md) |  | 
**total** | **int** | The total number of available cluster templates | [optional] 

## Example

```python
from exalsius_api_client.models.cluster_template_list_response import ClusterTemplateListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterTemplateListResponse from a JSON string
cluster_template_list_response_instance = ClusterTemplateListResponse.from_json(json)
# print the JSON string representation of the object
print(ClusterTemplateListResponse.to_json())

# convert the object into a dict
cluster_template_list_response_dict = cluster_template_list_response_instance.to_dict()
# create an instance of ClusterTemplateListResponse from a dict
cluster_template_list_response_from_dict = ClusterTemplateListResponse.from_dict(cluster_template_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


