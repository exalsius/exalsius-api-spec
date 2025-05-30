# OffersListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offers** | [**List[Offer]**](Offer.md) |  | 
**total** | **int** | The total number of offers matching the filters | 
**next_cursor** | **str** | The cursor for the next page. If null, there are no more results. | [optional] 
**prev_cursor** | **str** | The cursor for the previous page. If null, this is the first page. | [optional] 

## Example

```python
from exalsius_api_client.models.offers_list_response import OffersListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OffersListResponse from a JSON string
offers_list_response_instance = OffersListResponse.from_json(json)
# print the JSON string representation of the object
print(OffersListResponse.to_json())

# convert the object into a dict
offers_list_response_dict = offers_list_response_instance.to_dict()
# create an instance of OffersListResponse from a dict
offers_list_response_from_dict = OffersListResponse.from_dict(offers_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


