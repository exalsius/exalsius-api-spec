# Node


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
**provider** | **str** | The cloud provider of the node | 
**region** | **str** | The region of the node | 
**availability_zone** | **str** | The availability zone of the node | [optional] 
**instance_type** | **str** | The instance type of the node | 
**price_per_hour** | **float** | The price per hour for the node | [optional] 
**endpoint** | **str** | The endpoint of the node (IP or hostname) and port | 
**username** | **str** | The username to connect to the node | 
**ssh_key_id** | **str** | The ID of the private SSH key to connect to the node | 

## Example

```python
from exalsius_api_client.models.node import Node

# TODO update the JSON string below
json = "{}"
# create an instance of Node from a JSON string
node_instance = Node.from_json(json)
# print the JSON string representation of the object
print(Node.to_json())

# convert the object into a dict
node_dict = node_instance.to_dict()
# create an instance of Node from a dict
node_from_dict = Node.from_dict(node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


