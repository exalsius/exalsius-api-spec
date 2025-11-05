# ClusterCreateRequestLocalStorage

Local storage configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Enable local storage provisioner | [optional] [default to True]
**base_path** | **str** | Base path for local storage. If empty, /var/openebs/local will be used | [optional] 

## Example

```python
from exalsius_api_client.models.cluster_create_request_local_storage import ClusterCreateRequestLocalStorage

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterCreateRequestLocalStorage from a JSON string
cluster_create_request_local_storage_instance = ClusterCreateRequestLocalStorage.from_json(json)
# print the JSON string representation of the object
print(ClusterCreateRequestLocalStorage.to_json())

# convert the object into a dict
cluster_create_request_local_storage_dict = cluster_create_request_local_storage_instance.to_dict()
# create an instance of ClusterCreateRequestLocalStorage from a dict
cluster_create_request_local_storage_from_dict = ClusterCreateRequestLocalStorage.from_dict(cluster_create_request_local_storage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


