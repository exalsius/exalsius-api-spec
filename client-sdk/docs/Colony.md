# Colony


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the colony | [optional] 
**name** | **str** | The name of the colony | 
**netbird_colony** | **bool** | Whether the colony is a Netbird (VPN) colony | [optional] [default to False]
**owner** | **str** | The owner of the colony (user id) | [optional] 
**namespace** | **str** | The namespace of the colony | [optional] 
**cluster_ids** | **List[str]** | The unique identifiers for the clusters in the colony | [optional] 
**created_at** | **datetime** | The date and time the colony was created | [optional] 

## Example

```python
from exalsius_api_client.models.colony import Colony

# TODO update the JSON string below
json = "{}"
# create an instance of Colony from a JSON string
colony_instance = Colony.from_json(json)
# print the JSON string representation of the object
print(Colony.to_json())

# convert the object into a dict
colony_dict = colony_instance.to_dict()
# create an instance of Colony from a dict
colony_from_dict = Colony.from_dict(colony_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


