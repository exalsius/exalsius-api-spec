# NodeHardware


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
from exalsius_api_client.models.node_hardware import NodeHardware

# TODO update the JSON string below
json = "{}"
# create an instance of NodeHardware from a JSON string
node_hardware_instance = NodeHardware.from_json(json)
# print the JSON string representation of the object
print(NodeHardware.to_json())

# convert the object into a dict
node_hardware_dict = node_hardware_instance.to_dict()
# create an instance of NodeHardware from a dict
node_hardware_from_dict = NodeHardware.from_dict(node_hardware_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


