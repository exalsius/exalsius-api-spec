# ClusterAdoptRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the cluster | 
**colony_id** | **str** | The ID of the colony to add the cluster to (optional). If not provided, the cluster will be added to the default colony. | [optional] 
**kubeconfig_b64** | **str** | The kubeconfig of the cluster in base64 encoded string format | [optional] 
**k8s_version** | **str** | The Kubernetes version of the cluster | [optional] 

## Example

```python
from exalsius_api_client.models.cluster_adopt_request import ClusterAdoptRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAdoptRequest from a JSON string
cluster_adopt_request_instance = ClusterAdoptRequest.from_json(json)
# print the JSON string representation of the object
print(ClusterAdoptRequest.to_json())

# convert the object into a dict
cluster_adopt_request_dict = cluster_adopt_request_instance.to_dict()
# create an instance of ClusterAdoptRequest from a dict
cluster_adopt_request_from_dict = ClusterAdoptRequest.from_dict(cluster_adopt_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


