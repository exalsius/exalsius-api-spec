# ClusterAddNodeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nodes_to_add** | [**List[ClusterNodeToAdd]**](ClusterNodeToAdd.md) |  | 

## Example

```python
from exalsius_api_client.models.cluster_add_node_request import ClusterAddNodeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAddNodeRequest from a JSON string
cluster_add_node_request_instance = ClusterAddNodeRequest.from_json(json)
# print the JSON string representation of the object
print(ClusterAddNodeRequest.to_json())

# convert the object into a dict
cluster_add_node_request_dict = cluster_add_node_request_instance.to_dict()
# create an instance of ClusterAddNodeRequest from a dict
cluster_add_node_request_from_dict = ClusterAddNodeRequest.from_dict(cluster_add_node_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


