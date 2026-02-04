# VramPredictionMetadataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**models** | **List[str]** | Distinct LLM models which are available for prediction. | 
**batch_size_min** | **int** | Minimum batch size. | 
**batch_size_max** | **int** | Maximum batch size. | 
**sequence_length_min** | **int** | Minimum sequence length. | 
**sequence_length_max** | **int** | Maximum sequence length. | 

## Example

```python
from exalsius_api_client.models.vram_prediction_metadata_response import VramPredictionMetadataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VramPredictionMetadataResponse from a JSON string
vram_prediction_metadata_response_instance = VramPredictionMetadataResponse.from_json(json)
# print the JSON string representation of the object
print(VramPredictionMetadataResponse.to_json())

# convert the object into a dict
vram_prediction_metadata_response_dict = vram_prediction_metadata_response_instance.to_dict()
# create an instance of VramPredictionMetadataResponse from a dict
vram_prediction_metadata_response_from_dict = VramPredictionMetadataResponse.from_dict(vram_prediction_metadata_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


