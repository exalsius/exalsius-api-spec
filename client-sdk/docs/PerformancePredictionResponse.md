# PerformancePredictionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**performance_prediction** | [**PerformancePrediction**](PerformancePrediction.md) |  | 

## Example

```python
from exalsius_api_client.models.performance_prediction_response import PerformancePredictionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PerformancePredictionResponse from a JSON string
performance_prediction_response_instance = PerformancePredictionResponse.from_json(json)
# print the JSON string representation of the object
print(PerformancePredictionResponse.to_json())

# convert the object into a dict
performance_prediction_response_dict = performance_prediction_response_instance.to_dict()
# create an instance of PerformancePredictionResponse from a dict
performance_prediction_response_from_dict = PerformancePredictionResponse.from_dict(performance_prediction_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


