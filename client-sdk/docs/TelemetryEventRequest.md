# TelemetryEventRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_name** | **str** | The telemetry event name. | 
**additional_properties** | **List[str]** |  | [optional] 

## Example

```python
from exalsius_api_client.models.telemetry_event_request import TelemetryEventRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TelemetryEventRequest from a JSON string
telemetry_event_request_instance = TelemetryEventRequest.from_json(json)
# print the JSON string representation of the object
print(TelemetryEventRequest.to_json())

# convert the object into a dict
telemetry_event_request_dict = telemetry_event_request_instance.to_dict()
# create an instance of TelemetryEventRequest from a dict
telemetry_event_request_from_dict = TelemetryEventRequest.from_dict(telemetry_event_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


