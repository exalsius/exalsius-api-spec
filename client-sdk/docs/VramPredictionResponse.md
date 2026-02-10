# VramPredictionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_vram** | **float** | The total predicted vram | 
**model_vram** | **float** | The vram used by the model | 
**optimizer_vram** | **float** | The vram used by the optimizer | 
**optimizer_intermediate_vram** | **float** | The vram used by the optimizer intermediate | 
**gradients_vram** | **float** | The vram used by the optimizer | 
**activations_vram** | **float** | The vram used by the activations | 

## Example

```python
from exalsius_api_client.models.vram_prediction_response import VramPredictionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VramPredictionResponse from a JSON string
vram_prediction_response_instance = VramPredictionResponse.from_json(json)
# print the JSON string representation of the object
print(VramPredictionResponse.to_json())

# convert the object into a dict
vram_prediction_response_dict = vram_prediction_response_instance.to_dict()
# create an instance of VramPredictionResponse from a dict
vram_prediction_response_from_dict = VramPredictionResponse.from_dict(vram_prediction_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


