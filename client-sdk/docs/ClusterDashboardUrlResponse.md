# ClusterDashboardUrlResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL to cluster-scoped Grafana dashboards | 

## Example

```python
from exalsius_api_client.models.cluster_dashboard_url_response import ClusterDashboardUrlResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterDashboardUrlResponse from a JSON string
cluster_dashboard_url_response_instance = ClusterDashboardUrlResponse.from_json(json)
# print the JSON string representation of the object
print(ClusterDashboardUrlResponse.to_json())

# convert the object into a dict
cluster_dashboard_url_response_dict = cluster_dashboard_url_response_instance.to_dict()
# create an instance of ClusterDashboardUrlResponse from a dict
cluster_dashboard_url_response_from_dict = ClusterDashboardUrlResponse.from_dict(cluster_dashboard_url_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


