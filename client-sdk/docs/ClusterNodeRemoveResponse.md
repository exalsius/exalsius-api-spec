# ClusterNodeRemoveResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **str** |  | 

## Example

```python
from exalsius_api_client.models.cluster_node_remove_response import ClusterNodeRemoveResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterNodeRemoveResponse from a JSON string
cluster_node_remove_response_instance = ClusterNodeRemoveResponse.from_json(json)
# print the JSON string representation of the object
print(ClusterNodeRemoveResponse.to_json())

# convert the object into a dict
cluster_node_remove_response_dict = cluster_node_remove_response_instance.to_dict()
# create an instance of ClusterNodeRemoveResponse from a dict
cluster_node_remove_response_from_dict = ClusterNodeRemoveResponse.from_dict(cluster_node_remove_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


