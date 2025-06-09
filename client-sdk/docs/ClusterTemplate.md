# ClusterTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the cluster template | 
**description** | **str** | The description of the cluster template | 
**k8s_version** | **str** | The Kubernetes version of the cluster template | 

## Example

```python
from exalsius_api_client.models.cluster_template import ClusterTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterTemplate from a JSON string
cluster_template_instance = ClusterTemplate.from_json(json)
# print the JSON string representation of the object
print(ClusterTemplate.to_json())

# convert the object into a dict
cluster_template_dict = cluster_template_instance.to_dict()
# create an instance of ClusterTemplate from a dict
cluster_template_from_dict = ClusterTemplate.from_dict(cluster_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


