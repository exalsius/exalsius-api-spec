# ClusterEventPayloadInvolvedObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 

## Example

```python
from exalsius_api_client.models.cluster_event_payload_involved_object import ClusterEventPayloadInvolvedObject

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterEventPayloadInvolvedObject from a JSON string
cluster_event_payload_involved_object_instance = ClusterEventPayloadInvolvedObject.from_json(json)
# print the JSON string representation of the object
print(ClusterEventPayloadInvolvedObject.to_json())

# convert the object into a dict
cluster_event_payload_involved_object_dict = cluster_event_payload_involved_object_instance.to_dict()
# create an instance of ClusterEventPayloadInvolvedObject from a dict
cluster_event_payload_involved_object_from_dict = ClusterEventPayloadInvolvedObject.from_dict(cluster_event_payload_involved_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


