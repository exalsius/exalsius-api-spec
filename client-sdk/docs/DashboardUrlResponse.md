# DashboardUrlResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL to Grafana dashboards | 

## Example

```python
from exalsius_api_client.models.dashboard_url_response import DashboardUrlResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardUrlResponse from a JSON string
dashboard_url_response_instance = DashboardUrlResponse.from_json(json)
# print the JSON string representation of the object
print(DashboardUrlResponse.to_json())

# convert the object into a dict
dashboard_url_response_dict = dashboard_url_response_instance.to_dict()
# create an instance of DashboardUrlResponse from a dict
dashboard_url_response_from_dict = DashboardUrlResponse.from_dict(dashboard_url_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


