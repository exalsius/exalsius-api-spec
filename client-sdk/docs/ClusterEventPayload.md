# ClusterEventPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**watch_event_type** | **str** | ADDED, MODIFIED, DELETED | 
**namespace** | **str** |  | 
**type** | **str** | Normal, Warning, etc. | [optional] 
**reason** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**last_timestamp** | **datetime** |  | [optional] 
**involved_object** | [**ClusterEventPayloadInvolvedObject**](ClusterEventPayloadInvolvedObject.md) |  | 

## Example

```python
from exalsius_api_client.models.cluster_event_payload import ClusterEventPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterEventPayload from a JSON string
cluster_event_payload_instance = ClusterEventPayload.from_json(json)
# print the JSON string representation of the object
print(ClusterEventPayload.to_json())

# convert the object into a dict
cluster_event_payload_dict = cluster_event_payload_instance.to_dict()
# create an instance of ClusterEventPayload from a dict
cluster_event_payload_from_dict = ClusterEventPayload.from_dict(cluster_event_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


