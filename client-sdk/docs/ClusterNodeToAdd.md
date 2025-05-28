# ClusterNodeToAdd


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **str** | The ID of the node to add | 
**node_role** | **str** | The role of the node to add | 

## Example

```python
from exalsius_api_client.models.cluster_node_to_add import ClusterNodeToAdd

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterNodeToAdd from a JSON string
cluster_node_to_add_instance = ClusterNodeToAdd.from_json(json)
# print the JSON string representation of the object
print(ClusterNodeToAdd.to_json())

# convert the object into a dict
cluster_node_to_add_dict = cluster_node_to_add_instance.to_dict()
# create an instance of ClusterNodeToAdd from a dict
cluster_node_to_add_from_dict = ClusterNodeToAdd.from_dict(cluster_node_to_add_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


