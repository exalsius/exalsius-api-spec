# ClusterDeleteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **str** | The ID of the deleted cluster | 
**node_ids** | **List[str]** | The IDs of the nodes that were returned to the pool | 

## Example

```python
from exalsius_api_client.models.cluster_delete_response import ClusterDeleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterDeleteResponse from a JSON string
cluster_delete_response_instance = ClusterDeleteResponse.from_json(json)
# print the JSON string representation of the object
print(ClusterDeleteResponse.to_json())

# convert the object into a dict
cluster_delete_response_dict = cluster_delete_response_instance.to_dict()
# create an instance of ClusterDeleteResponse from a dict
cluster_delete_response_from_dict = ClusterDeleteResponse.from_dict(cluster_delete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


