# NodeResponse

A single node, either self-managed or cloud

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the node | 
**node_type** | **str** | The type of the node. - &#x60;CLOUD&#x60;: Cloud node - &#x60;SELF_MANAGED&#x60;: Self-managed node  | 
**description** | **str** | Description of the node | [optional] 
**location** | **str** | The location of the node (e.g. city, data center, server rack, etc.) | [optional] 
**gpu_count** | **int** | The number of GPUs | [optional] 
**gpu_vendor** | **str** | The vendor of the GPU | [optional] 
**gpu_type** | **str** | The type of the GPU | [optional] 
**gpu_memory** | **int** | The memory of the GPU in GB | [optional] 
**cpu_cores** | **int** | The number of CPU cores | [optional] 
**memory_gb** | **int** | The memory of the node in GB | [optional] 
**storage_gb** | **int** | The storage of the node in GB | [optional] 
**import_time** | **datetime** | The time the node was imported | [optional] 
**node_status** | **str** | The status of the node. - &#x60;PENDING&#x60;: Node is pending, e.g. because it wasn&#39;t launched yet (CloudNode) or because it wasn&#39;t discovered yet (SelfManagedNode) - &#x60;AVAILABLE&#x60;: Node is available to be added to a cluster - &#x60;STAGED&#x60;: Node is staged in a cluster - &#x60;OCCUPIED&#x60;: Node is occupied in a cluster  | 
**endpoint** | **str** | The endpoint of the node (IP or hostname) and port | [optional] 
**username** | **str** | The username to connect to the node | [optional] 
**ssh_key_id** | **str** | The ID of the private SSH key to connect to the node | [optional] 

## Example

```python
from exalsius_api_client.models.node_response import NodeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NodeResponse from a JSON string
node_response_instance = NodeResponse.from_json(json)
# print the JSON string representation of the object
print(NodeResponse.to_json())

# convert the object into a dict
node_response_dict = node_response_instance.to_dict()
# create an instance of NodeResponse from a dict
node_response_from_dict = NodeResponse.from_dict(node_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


