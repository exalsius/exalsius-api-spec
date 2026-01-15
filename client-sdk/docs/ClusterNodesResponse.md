# ClusterNodesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **str** | The unique identifier of the cluster | 
**control_plane_node_ids** | **List[str]** |  | 
**worker_node_ids** | **List[str]** |  | 
**total_nodes** | **int** | The total number of nodes in the cluster | [optional] 

## Example

```python
from exalsius_api_client.models.cluster_nodes_response import ClusterNodesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterNodesResponse from a JSON string
cluster_nodes_response_instance = ClusterNodesResponse.from_json(json)
# print the JSON string representation of the object
print(ClusterNodesResponse.to_json())

# convert the object into a dict
cluster_nodes_response_dict = cluster_nodes_response_instance.to_dict()
# create an instance of ClusterNodesResponse from a dict
cluster_nodes_response_from_dict = ClusterNodesResponse.from_dict(cluster_nodes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


