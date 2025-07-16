# ClusterCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the cluster | 
**colony_id** | **str** | The ID of the colony to add the cluster to (optional). If not provided, the cluster will be added to the default colony. | [optional] 
**k8s_version** | **str** | The Kubernetes version of the cluster | 
**to_be_deleted_at** | **datetime** | The date and time the cluster will be deleted (optional). | [optional] 
**control_plane_node_ids** | **List[str]** | The IDs of the control plane nodes (optional). | [optional] 
**worker_node_ids** | **List[str]** | The IDs of the worker nodes (optional). | [optional] 
**service_deployments** | [**List[ServiceDeployment]**](ServiceDeployment.md) | The services to deploy in the cluster (optional). | [optional] 

## Example

```python
from exalsius_api_client.models.cluster_create_request import ClusterCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterCreateRequest from a JSON string
cluster_create_request_instance = ClusterCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ClusterCreateRequest.to_json())

# convert the object into a dict
cluster_create_request_dict = cluster_create_request_instance.to_dict()
# create an instance of ClusterCreateRequest from a dict
cluster_create_request_from_dict = ClusterCreateRequest.from_dict(cluster_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


