# ColonyCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the colony | 

## Example

```python
from exalsius_api_client.models.colony_create_request import ColonyCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ColonyCreateRequest from a JSON string
colony_create_request_instance = ColonyCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ColonyCreateRequest.to_json())

# convert the object into a dict
colony_create_request_dict = colony_create_request_instance.to_dict()
# create an instance of ColonyCreateRequest from a dict
colony_create_request_from_dict = ColonyCreateRequest.from_dict(colony_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


