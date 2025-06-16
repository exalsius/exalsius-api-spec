# ClusterResourcesListResponseResourcesInner

The available / occupied resources on the node

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **str** | The unique identifier for the node | [optional] 
**available** | [**ResourcePool**](ResourcePool.md) | The available resources on the node | [optional] 
**occupied** | [**ResourcePool**](ResourcePool.md) | The occupied resources on the node | [optional] 

## Example

```python
from exalsius_api_client.models.cluster_resources_list_response_resources_inner import ClusterResourcesListResponseResourcesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterResourcesListResponseResourcesInner from a JSON string
cluster_resources_list_response_resources_inner_instance = ClusterResourcesListResponseResourcesInner.from_json(json)
# print the JSON string representation of the object
print(ClusterResourcesListResponseResourcesInner.to_json())

# convert the object into a dict
cluster_resources_list_response_resources_inner_dict = cluster_resources_list_response_resources_inner_instance.to_dict()
# create an instance of ClusterResourcesListResponseResourcesInner from a dict
cluster_resources_list_response_resources_inner_from_dict = ClusterResourcesListResponseResourcesInner.from_dict(cluster_resources_list_response_resources_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


