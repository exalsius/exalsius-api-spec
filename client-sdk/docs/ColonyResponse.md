# ColonyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**colony** | [**Colony**](Colony.md) |  | 

## Example

```python
from exalsius_api_client.models.colony_response import ColonyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ColonyResponse from a JSON string
colony_response_instance = ColonyResponse.from_json(json)
# print the JSON string representation of the object
print(ColonyResponse.to_json())

# convert the object into a dict
colony_response_dict = colony_response_instance.to_dict()
# create an instance of ColonyResponse from a dict
colony_response_from_dict = ColonyResponse.from_dict(colony_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


