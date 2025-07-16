# ColonyDeleteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**colony_id** | **str** | The ID of the deleted colony | 
**cluster_ids** | **List[str]** | The IDs of the clusters that were deleted | 

## Example

```python
from exalsius_api_client.models.colony_delete_response import ColonyDeleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ColonyDeleteResponse from a JSON string
colony_delete_response_instance = ColonyDeleteResponse.from_json(json)
# print the JSON string representation of the object
print(ColonyDeleteResponse.to_json())

# convert the object into a dict
colony_delete_response_dict = colony_delete_response_instance.to_dict()
# create an instance of ColonyDeleteResponse from a dict
colony_delete_response_from_dict = ColonyDeleteResponse.from_dict(colony_delete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


