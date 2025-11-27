# NodeResponse

A single node, either self-managed or cloud

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the node | 
**node_type** | **str** | The type of the node. Must be \&quot;SELF_MANAGED\&quot;. | 
**namespace** | **str** | The namespace of the node (e.g. the namespace of the user that added the node) | [optional] 
**hostname** | **str** | The hostname of the node | [optional] 
**description** | **str** | Description of the node | [optional] 
**location** | **str** | The location of the node (e.g. city, data center, server rack, etc.) | [optional] 
**import_time** | **datetime** | The time the node was imported | [optional] 
**node_status** | **str** | The status of the node. - &#x60;PENDING&#x60;: Node is pending, e.g. because it wasn&#39;t launched yet (CloudNode) or because it wasn&#39;t discovered yet (SelfManagedNode) - &#x60;DISCOVERING&#x60;: Node is being discovered (SSH is checked for SelfManagedNode, Availability for CloudNodes) - &#x60;AVAILABLE&#x60;: Node is available to be added to a cluster - &#x60;ADDED&#x60;: Node is added to a cluster - &#x60;DEPLOYED&#x60;: Node is deployed in a cluster - &#x60;FAILED&#x60;: The discovering process of the node failed  | 
**hardware** | [**NodeHardware**](NodeHardware.md) |  | [optional] 
**software** | [**NodeSoftware**](NodeSoftware.md) |  | [optional] 
**system** | [**NodeSystem**](NodeSystem.md) |  | [optional] 
**endpoint** | **str** | The endpoint of the node (IP or hostname) and port | 
**username** | **str** | The username to connect to the node | 
**ssh_key_id** | **str** | The ID of the private SSH key to connect to the node | 
**last_heartbeat_date** | **datetime** | The last time a heartbeat was received from the node | [optional] 

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


