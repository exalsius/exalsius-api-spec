# ClusterResourcesListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resources** | [**List[ClusterResourcesListResponseResourcesInner]**](ClusterResourcesListResponseResourcesInner.md) |  | 
**total** | **int** | The total number of available / occupied resources in the cluster | [optional] 

## Example

```python
from exalsius_api_client.models.cluster_resources_list_response import ClusterResourcesListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterResourcesListResponse from a JSON string
cluster_resources_list_response_instance = ClusterResourcesListResponse.from_json(json)
# print the JSON string representation of the object
print(ClusterResourcesListResponse.to_json())

# convert the object into a dict
cluster_resources_list_response_dict = cluster_resources_list_response_instance.to_dict()
# create an instance of ClusterResourcesListResponse from a dict
cluster_resources_list_response_from_dict = ClusterResourcesListResponse.from_dict(cluster_resources_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


