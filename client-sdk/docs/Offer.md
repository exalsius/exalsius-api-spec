# Offer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the GPU instance. Format: &#39;{provider}-{instance_type}-{region}-{availability_zone}&#39; This ID must be unique across all instances.  | 
**instance_type** | **str** | The cloud provider&#39;s instance type identifier that represents this GPU configuration. | 
**cloud_provider** | **str** | The cloud service provider offering this GPU instance. Identifies which major cloud platform the instance belongs to. | 
**gpu_count** | **int** | The number of physical GPUs available in this instance type. Must be a positive integer. It is 0 if the number of GPUs is not available. | 
**gpu_memory_mib** | **int** | The amount of memory per GPU in Mebibytes (MiB). Must be a positive integer. It is 0 if the memory is not available. | 
**total_gpu_memory_mib** | **int** | The total amount of memory in Mebibytes (MiB) for all GPUs in the instance. Must be a positive integer. It is 0 if the total memory is not available. | 
**gpu_type** | **str** | The specific GPU model/architecture available in this instance. Represents the actual hardware model of the GPU. | 
**gpu_vendor** | **str** | The manufacturer/vendor of the GPU hardware. Limited to a set of known GPU manufacturers in the cloud computing space. | 
**main_memory_mib** | **int** | The amount of main memory in Mebibytes (MiB). Must be a positive integer. | 
**cpu_vendor** | **str** | The manufacturer/vendor of the CPU hardware. Limited to a set of known CPU manufacturers in the cloud computing space. | 
**cpu_arch** | **str** | The architecture of the CPU hardware. | 
**num_vcpus** | **int** | The number of virtual CPUs available in the instance. Must be a positive integer. It is 0 if the number of vCPUs is not available. | 
**effective_time** | **datetime** | Timestamp indicating when this price becomes valid. Must not be later than scrape_time. | [optional] 
**scrape_time** | **datetime** | Timestamp recording when this price data was collected from the source. | 
**pricing_unit** | **str** | Time unit for the price value (e.g., hourly, monthly, yearly). Also used for normalization. | 
**price** | **float** | The numerical price value with respect to the specified currency and time unit. | [optional] 
**currency** | **str** | The currency of the price value (e.g., USD, EUR). Used for currency conversion. | 
**price_type** | **str** | Type of pricing model (on-demand or spot) | 
**hourly_cost** | **float** | Price normalized to hourly rate for comparison. | 
**location** | **str** | The location of the offer | 
**region** | **str** | The region of the offer | 
**availability_zone** | **str** | The availability zone of the offer | 

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


