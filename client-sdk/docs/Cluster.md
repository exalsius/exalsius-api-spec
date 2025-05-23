# Cluster


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for the cluster | 
**name** | **str** | The name of the cluster | [optional] 
**cluster_status** | **str** | The status of the cluster. - &#x60;STAGING&#x60;: Cluster is staging - &#x60;RUNNING&#x60;: Cluster is running - &#x60;DELETING&#x60;: Cluster is deleting - &#x60;DELETED&#x60;: Cluster is deleted  | 
**created_at** | **datetime** | The date and time the cluster was created | 
**updated_at** | **datetime** | The date and time the cluster was last updated | [optional] 
**to_be_deleted_at** | **datetime** | The date and time the cluster will be deleted | [optional] 
**control_plane_node_ids** | **List[str]** | The node IDs of the control plane nodes in the cluster | [optional] 
**worker_node_ids** | **List[str]** | The node IDs of the worker nodes in the cluster | [optional] 
**service_deployments** | [**List[ServiceDeployment]**](ServiceDeployment.md) | The deployed services in the cluster | [optional] 
**k8s_version** | **str** | The version of Kubernetes deployed in the cluster | [optional] 
**current_costs** | **float** | The total costs of the cluster until now | [optional] 
**costs_per_hour** | **float** | The costs of the cluster per hour | [optional] 

## Example

```python
from exalsius_api_client.models.cluster import Cluster

# TODO update the JSON string below
json = "{}"
# create an instance of Cluster from a JSON string
cluster_instance = Cluster.from_json(json)
# print the JSON string representation of the object
print(Cluster.to_json())

# convert the object into a dict
cluster_dict = cluster_instance.to_dict()
# create an instance of Cluster from a dict
cluster_from_dict = Cluster.from_dict(cluster_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


