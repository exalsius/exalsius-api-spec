# ColonyKubeconfigResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kubeconfig** | **str** | The kubeconfig for all clusters of the colony | 

## Example

```python
from exalsius_api_client.models.colony_kubeconfig_response import ColonyKubeconfigResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ColonyKubeconfigResponse from a JSON string
colony_kubeconfig_response_instance = ColonyKubeconfigResponse.from_json(json)
# print the JSON string representation of the object
print(ColonyKubeconfigResponse.to_json())

# convert the object into a dict
colony_kubeconfig_response_dict = colony_kubeconfig_response_instance.to_dict()
# create an instance of ColonyKubeconfigResponse from a dict
colony_kubeconfig_response_from_dict = ColonyKubeconfigResponse.from_dict(colony_kubeconfig_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


