# Kubeconfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kubeconfig** | **str** | The kubeconfig for the cluster | [optional] 

## Example

```python
from exalsius_api_client.models.kubeconfig import Kubeconfig

# TODO update the JSON string below
json = "{}"
# create an instance of Kubeconfig from a JSON string
kubeconfig_instance = Kubeconfig.from_json(json)
# print the JSON string representation of the object
print(Kubeconfig.to_json())

# convert the object into a dict
kubeconfig_dict = kubeconfig_instance.to_dict()
# create an instance of Kubeconfig from a dict
kubeconfig_from_dict = Kubeconfig.from_dict(kubeconfig_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


