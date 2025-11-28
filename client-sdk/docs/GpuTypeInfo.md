# GpuTypeInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gpu_type** | **str** | Normalized GPU type identifier. | 
**gpu_vendor** | **str** | The vendor/manufacturer for the GPU type. | 

## Example

```python
from exalsius_api_client.models.gpu_type_info import GpuTypeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GpuTypeInfo from a JSON string
gpu_type_info_instance = GpuTypeInfo.from_json(json)
# print the JSON string representation of the object
print(GpuTypeInfo.to_json())

# convert the object into a dict
gpu_type_info_dict = gpu_type_info_instance.to_dict()
# create an instance of GpuTypeInfo from a dict
gpu_type_info_from_dict = GpuTypeInfo.from_dict(gpu_type_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


