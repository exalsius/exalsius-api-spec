# PerformancePredictionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_name** | **str** | Define the model for which you want a performance prediction. | 
**optimizer** | **str** | The optimizer selected for training. | 
**batch_size** | **int** | The batch size. | 
**sequence_length** | **int** | The sequence length. | 
**accumulation_steps** | **int** | The number of gradient accumulation steps. Select 1 for no gradient accumulation. | 
**dataset_size** | **int** | The size of the dataset in tokens. | 

## Example

```python
from exalsius_api_client.models.performance_prediction_request import PerformancePredictionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PerformancePredictionRequest from a JSON string
performance_prediction_request_instance = PerformancePredictionRequest.from_json(json)
# print the JSON string representation of the object
print(PerformancePredictionRequest.to_json())

# convert the object into a dict
performance_prediction_request_dict = performance_prediction_request_instance.to_dict()
# create an instance of PerformancePredictionRequest from a dict
performance_prediction_request_from_dict = PerformancePredictionRequest.from_dict(performance_prediction_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


