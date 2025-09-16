# Hardware


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gpu_count** | **int** | The number of GPUs | [optional] 
**gpu_vendor** | **str** | The vendor of the GPU | [optional] 
**gpu_type** | **str** | The type of the GPU | [optional] 
**gpu_memory** | **int** | The memory of the GPU in GB | [optional] 
**cpu_cores** | **int** | The number of CPU cores | [optional] 
**memory_gb** | **int** | The memory of the node in GB | [optional] 
**storage_gb** | **int** | The storage of the node in GB | [optional] 

## Example

```python
from exalsius_api_client.models.hardware import Hardware

# TODO update the JSON string below
json = "{}"
# create an instance of Hardware from a JSON string
hardware_instance = Hardware.from_json(json)
# print the JSON string representation of the object
print(Hardware.to_json())

# convert the object into a dict
hardware_dict = hardware_instance.to_dict()
# create an instance of Hardware from a dict
hardware_from_dict = Hardware.from_dict(hardware_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


