# ClusterCreateResponse

Cluster creation response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **int** | The ID of the created cluster | 

## Example

```python
from exalsius_api_client.models.cluster_create_response import ClusterCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterCreateResponse from a JSON string
cluster_create_response_instance = ClusterCreateResponse.from_json(json)
# print the JSON string representation of the object
print(ClusterCreateResponse.to_json())

# convert the object into a dict
cluster_create_response_dict = cluster_create_response_instance.to_dict()
# create an instance of ClusterCreateResponse from a dict
cluster_create_response_from_dict = ClusterCreateResponse.from_dict(cluster_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


