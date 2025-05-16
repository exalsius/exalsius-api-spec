# ClusterServicesResponse

List of services in the cluster

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **str** | The unique identifier of the cluster | 
**services_deployments** | [**List[ServiceDeployment]**](ServiceDeployment.md) |  | 

## Example

```python
from exalsius_api_client.models.cluster_services_response import ClusterServicesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterServicesResponse from a JSON string
cluster_services_response_instance = ClusterServicesResponse.from_json(json)
# print the JSON string representation of the object
print(ClusterServicesResponse.to_json())

# convert the object into a dict
cluster_services_response_dict = cluster_services_response_instance.to_dict()
# create an instance of ClusterServicesResponse from a dict
cluster_services_response_from_dict = ClusterServicesResponse.from_dict(cluster_services_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


