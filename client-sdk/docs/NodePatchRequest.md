# NodePatchRequest


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
**description** | **str** | Description of the node | [optional] 

## Example

```python
from exalsius_api_client.models.node_patch_request import NodePatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NodePatchRequest from a JSON string
node_patch_request_instance = NodePatchRequest.from_json(json)
# print the JSON string representation of the object
print(NodePatchRequest.to_json())

# convert the object into a dict
node_patch_request_dict = node_patch_request_instance.to_dict()
# create an instance of NodePatchRequest from a dict
node_patch_request_from_dict = NodePatchRequest.from_dict(node_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


