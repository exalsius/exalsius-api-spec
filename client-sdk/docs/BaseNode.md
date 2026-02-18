# BaseNode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the node | 
**node_type** | **str** | The type of the node. - &#x60;CLOUD&#x60;: Cloud node - &#x60;SELF_MANAGED&#x60;: Self-managed node  | 
**namespace** | **str** | The namespace of the node (e.g. the namespace of the user that added the node) | [optional] 
**hostname** | **str** | The hostname of the node | [optional] 
**description** | **str** | Description of the node | [optional] 
**location** | **str** | The location of the node (e.g. city, data center, server rack, etc.) | [optional] 
**import_time** | **datetime** | The time the node was imported | [optional] 
**price_per_hour** | **float** | The price per hour for the node | 
**node_status** | **str** | The status of the node. - &#x60;PENDING&#x60;: Node is pending, e.g. because it wasn&#39;t launched yet (CloudNode) or because it wasn&#39;t discovered yet (SelfManagedNode) - &#x60;DISCOVERING&#x60;: Node is being discovered (SSH is checked for SelfManagedNode, Availability for CloudNodes) - &#x60;AVAILABLE&#x60;: Node is available to be added to a cluster - &#x60;ADDED&#x60;: Node is added to a cluster - &#x60;DEPLOYED&#x60;: Node is deployed in a cluster - &#x60;FAILED&#x60;: The discovering process of the node failed - &#x60;WARNING&#x60;: Node is in a warning state, e.g., pre-installed software hinders the deployment of the node  | 
**warning_message** | **str** | Provides additional information on the warning status, e.g., if software such as Docker, cuda, or rocm is pre-installed on the node | [optional] 
**hardware** | [**NodeHardware**](NodeHardware.md) |  | [optional] 
**software** | [**NodeSoftware**](NodeSoftware.md) |  | [optional] 
**system** | [**NodeSystem**](NodeSystem.md) |  | [optional] 

## Example

```python
from exalsius_api_client.models.base_node import BaseNode

# TODO update the JSON string below
json = "{}"
# create an instance of BaseNode from a JSON string
base_node_instance = BaseNode.from_json(json)
# print the JSON string representation of the object
print(BaseNode.to_json())

# convert the object into a dict
base_node_dict = base_node_instance.to_dict()
# create an instance of BaseNode from a dict
base_node_from_dict = BaseNode.from_dict(base_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


