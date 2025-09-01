# PerformancePrediction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_name** | **str** | Model name | 
**vram** | **Dict[str, float]** |  | 
**runtime** | **Dict[str, float]** |  | 

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


