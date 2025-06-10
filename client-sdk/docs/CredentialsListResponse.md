# CredentialsListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | [**List[Credentials]**](Credentials.md) |  | 
**total** | **int** | The total number of available credentials | [optional] 

## Example

```python
from exalsius_api_client.models.credentials_list_response import CredentialsListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialsListResponse from a JSON string
credentials_list_response_instance = CredentialsListResponse.from_json(json)
# print the JSON string representation of the object
print(CredentialsListResponse.to_json())

# convert the object into a dict
credentials_list_response_dict = credentials_list_response_instance.to_dict()
# create an instance of CredentialsListResponse from a dict
credentials_list_response_from_dict = CredentialsListResponse.from_dict(credentials_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


