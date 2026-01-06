# PerformancePrediction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_name** | **str** | Model name | 
**vram** | **Dict[str, float]** | Predicted VRAM (Video RAM) usage in GB for different GPU types. Keys are GPU type identifiers (e.g., \&quot;A100\&quot;, \&quot;H100\&quot;, \&quot;RTX4090\&quot;, \&quot;A6000\&quot;). Values represent the estimated memory consumption in gigabytes.  | 
**step_time** | **Dict[str, float]** | Predicted runtime per training step in seconds for different GPU types. Keys are GPU type identifiers (e.g., \&quot;A100\&quot;, \&quot;H100\&quot;, \&quot;RTX4090\&quot;, \&quot;A6000\&quot;). Values represent the estimated time per step in seconds.  | 
**runtime** | **Dict[str, float]** | Predicted total runtime per epoch in seconds for different GPU types. Keys are GPU type identifiers (e.g., \&quot;A100\&quot;, \&quot;H100\&quot;, \&quot;RTX4090\&quot;, \&quot;A6000\&quot;). Values represent the estimated total training time per epoch in seconds.  | 

## Example

```python
from exalsius_api_client.models.performance_prediction import PerformancePrediction

# TODO update the JSON string below
json = "{}"
# create an instance of PerformancePrediction from a JSON string
performance_prediction_instance = PerformancePrediction.from_json(json)
# print the JSON string representation of the object
print(PerformancePrediction.to_json())

# convert the object into a dict
performance_prediction_dict = performance_prediction_instance.to_dict()
# create an instance of PerformancePrediction from a dict
performance_prediction_from_dict = PerformancePrediction.from_dict(performance_prediction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


