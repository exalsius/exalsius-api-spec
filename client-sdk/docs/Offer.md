# Offer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the offer | 
**provider** | **str** | The cloud provider of the offer | 
**location** | **str** | The location of the offer | 
**region** | **str** | The region of the offer | 
**availability_zone** | **str** | The availability zone of the offer | 
**instance_type** | **str** | The instance type of the offer | 
**gpu_count** | **int** | The number of GPUs in the offer | 
**gpu_vendor** | **str** | The vendor of the GPU | 
**gpu_type** | **str** | The type of the GPU | 
**gpu_memory** | **int** | The memory of the GPU in GB | 
**price_per_hour** | **float** | The price per hour for the offer | 
**scrape_time** | **datetime** | The time the offer was scraped | 

## Example

```python
from exalsius_api_client.models.offer import Offer

# TODO update the JSON string below
json = "{}"
# create an instance of Offer from a JSON string
offer_instance = Offer.from_json(json)
# print the JSON string representation of the object
print(Offer.to_json())

# convert the object into a dict
offer_dict = offer_instance.to_dict()
# create an instance of Offer from a dict
offer_from_dict = Offer.from_dict(offer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


