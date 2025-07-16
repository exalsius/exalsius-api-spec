# ColoniesListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**colonies** | [**List[Colony]**](Colony.md) |  | 
**total** | **int** | The total number of colonies | [optional] 

## Example

```python
from exalsius_api_client.models.colonies_list_response import ColoniesListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ColoniesListResponse from a JSON string
colonies_list_response_instance = ColoniesListResponse.from_json(json)
# print the JSON string representation of the object
print(ColoniesListResponse.to_json())

# convert the object into a dict
colonies_list_response_dict = colonies_list_response_instance.to_dict()
# create an instance of ColoniesListResponse from a dict
colonies_list_response_from_dict = ColoniesListResponse.from_dict(colonies_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


