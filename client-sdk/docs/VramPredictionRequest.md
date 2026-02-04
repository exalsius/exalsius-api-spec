# VramPredictionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** | Define the model for which you want a performance prediction. | 
**batch_size** | **int** | The batch size. | 
**sequence_length** | **int** | The sequence length. | 

## Example

```python
from exalsius_api_client.models.vram_prediction_request import VramPredictionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VramPredictionRequest from a JSON string
vram_prediction_request_instance = VramPredictionRequest.from_json(json)
# print the JSON string representation of the object
print(VramPredictionRequest.to_json())

# convert the object into a dict
vram_prediction_request_dict = vram_prediction_request_instance.to_dict()
# create an instance of VramPredictionRequest from a dict
vram_prediction_request_from_dict = VramPredictionRequest.from_dict(vram_prediction_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


