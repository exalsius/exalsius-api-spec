# NodeSystem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**os** | **str** | The operating system running on the node | [optional] 
**kernel** | **str** | The kernel version | [optional] 

## Example

```python
from exalsius_api_client.models.node_system import NodeSystem

# TODO update the JSON string below
json = "{}"
# create an instance of NodeSystem from a JSON string
node_system_instance = NodeSystem.from_json(json)
# print the JSON string representation of the object
print(NodeSystem.to_json())

# convert the object into a dict
node_system_dict = node_system_instance.to_dict()
# create an instance of NodeSystem from a dict
node_system_from_dict = NodeSystem.from_dict(node_system_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


