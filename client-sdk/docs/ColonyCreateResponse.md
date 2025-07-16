# ColonyCreateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**colony_id** | **str** | The ID of the created colony | 

## Example

```python
from exalsius_api_client.models.colony_create_response import ColonyCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ColonyCreateResponse from a JSON string
colony_create_response_instance = ColonyCreateResponse.from_json(json)
# print the JSON string representation of the object
print(ColonyCreateResponse.to_json())

# convert the object into a dict
colony_create_response_dict = colony_create_response_instance.to_dict()
# create an instance of ColonyCreateResponse from a dict
colony_create_response_from_dict = ColonyCreateResponse.from_dict(colony_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


