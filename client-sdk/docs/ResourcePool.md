# ResourcePool


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gpu_count** | **int** | The number of GPUs | [optional] 
**gpu_vendor** | **str** | The vendor of the GPU | [optional] 
**gpu_type** | **str** | The type of the GPU | [optional] 
**cpu_cores** | **int** | The number of CPU cores | [optional] 
**memory_gb** | **int** | The memory of the node in GB | [optional] 
**storage_gb** | **int** | The storage of the node in GB | [optional] 

## Example

```python
from exalsius_api_client.models.resource_pool import ResourcePool

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcePool from a JSON string
resource_pool_instance = ResourcePool.from_json(json)
# print the JSON string representation of the object
print(ResourcePool.to_json())

# convert the object into a dict
resource_pool_dict = resource_pool_instance.to_dict()
# create an instance of ResourcePool from a dict
resource_pool_from_dict = ResourcePool.from_dict(resource_pool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


