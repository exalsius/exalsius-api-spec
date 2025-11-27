# NodeSoftware


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**docker** | **str** | The version of Docker installed on the node | [optional] 
**nvidia** | **str** | The version of NVIDIA GPU Manager installed on the node | [optional] 
**amd** | **str** | The version of AMD GPU Manager installed on the node | [optional] 

## Example

```python
from exalsius_api_client.models.node_software import NodeSoftware

# TODO update the JSON string below
json = "{}"
# create an instance of NodeSoftware from a JSON string
node_software_instance = NodeSoftware.from_json(json)
# print the JSON string representation of the object
print(NodeSoftware.to_json())

# convert the object into a dict
node_software_dict = node_software_instance.to_dict()
# create an instance of NodeSoftware from a dict
node_software_from_dict = NodeSoftware.from_dict(node_software_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


