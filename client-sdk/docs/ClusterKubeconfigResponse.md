# ClusterKubeconfigResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kubeconfig** | **str** | The kubeconfig for the cluster | 

## Example

```python
from exalsius_api_client.models.cluster_kubeconfig_response import ClusterKubeconfigResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterKubeconfigResponse from a JSON string
cluster_kubeconfig_response_instance = ClusterKubeconfigResponse.from_json(json)
# print the JSON string representation of the object
print(ClusterKubeconfigResponse.to_json())

# convert the object into a dict
cluster_kubeconfig_response_dict = cluster_kubeconfig_response_instance.to_dict()
# create an instance of ClusterKubeconfigResponse from a dict
cluster_kubeconfig_response_from_dict = ClusterKubeconfigResponse.from_dict(cluster_kubeconfig_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


