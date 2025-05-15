# SelfManagedNode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for the node | 
**node_type** | **str** |  | 
**description** | **str** | Description of the node | [optional] 
**location** | **str** | The location of the node (e.g. city, data center, server rack, etc.) | 
**gpu_count** | **int** | The number of GPUs | [optional] 
**gpu_vendor** | **str** | The vendor of the GPU | [optional] 
**gpu_type** | **str** | The type of the GPU | [optional] 
**gpu_memory** | **int** | The memory of the GPU in GB | [optional] 
**cpu_cores** | **int** | The number of CPU cores | [optional] 
**memory_gb** | **int** | The memory of the node in GB | [optional] 
**storage_gb** | **int** | The storage of the node in GB | [optional] 
**import_time** | **datetime** | The time the node was imported | [optional] 
**node_status** | **str** | The status of the node | 
**endpoint** | **str** | The endpoint of the node (IP or hostname) and port | 
**username** | **str** | The username to connect to the node | 
**ssh_key_id** | **str** | The ID of the private SSH key to connect to the node | 

## Example

```python
from exalsius_api_client.models.self_managed_node import SelfManagedNode

# TODO update the JSON string below
json = "{}"
# create an instance of SelfManagedNode from a JSON string
self_managed_node_instance = SelfManagedNode.from_json(json)
# print the JSON string representation of the object
print(SelfManagedNode.to_json())

# convert the object into a dict
self_managed_node_dict = self_managed_node_instance.to_dict()
# create an instance of SelfManagedNode from a dict
self_managed_node_from_dict = SelfManagedNode.from_dict(self_managed_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


