# ClusterAddServiceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_deployments** | [**List[ServiceDeployment]**](ServiceDeployment.md) |  | 

## Example

```python
from exalsius_api_client.models.cluster_add_service_request import ClusterAddServiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAddServiceRequest from a JSON string
cluster_add_service_request_instance = ClusterAddServiceRequest.from_json(json)
# print the JSON string representation of the object
print(ClusterAddServiceRequest.to_json())

# convert the object into a dict
cluster_add_service_request_dict = cluster_add_service_request_instance.to_dict()
# create an instance of ClusterAddServiceRequest from a dict
cluster_add_service_request_from_dict = ClusterAddServiceRequest.from_dict(cluster_add_service_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


