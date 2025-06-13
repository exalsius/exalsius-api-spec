# SelfManagedNode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_type** | **str** | The type of the node. Must be \&quot;SELF_MANAGED\&quot;. | [optional] 
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


