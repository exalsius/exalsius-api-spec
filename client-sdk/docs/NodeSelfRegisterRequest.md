# NodeSelfRegisterRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**register_token** | **str** | The token used to register the node | 
**hostname** | **str** | The hostname of the node | 
**endpoint** | **str** | IP or hostname reachable over SSH | 
**username** | **str** | Username to access the node | 
**ssh_key_id** | **str** | The ID of the SSH key to use for the node | 
**price_per_hour** | **float** | Price per hour for the node, in USD | [optional] [default to 0]
**hardware** | [**NodeHardware**](NodeHardware.md) |  | [optional] 
**software** | [**NodeSoftware**](NodeSoftware.md) |  | [optional] 
**system** | [**NodeSystem**](NodeSystem.md) |  | [optional] 

## Example

```python
from exalsius_api_client.models.node_self_register_request import NodeSelfRegisterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NodeSelfRegisterRequest from a JSON string
node_self_register_request_instance = NodeSelfRegisterRequest.from_json(json)
# print the JSON string representation of the object
print(NodeSelfRegisterRequest.to_json())

# convert the object into a dict
node_self_register_request_dict = node_self_register_request_instance.to_dict()
# create an instance of NodeSelfRegisterRequest from a dict
node_self_register_request_from_dict = NodeSelfRegisterRequest.from_dict(node_self_register_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


