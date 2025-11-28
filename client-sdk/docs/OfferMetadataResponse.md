# OfferMetadataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gpu_types** | [**List[GpuTypeInfo]**](GpuTypeInfo.md) | Distinct GPU types currently available in offers. | 
**gpu_vendors** | **List[str]** |  | 
**cloud_providers** | **List[str]** |  | 
**regions** | **List[str]** |  | 
**availability_zones** | **List[str]** |  | 
**locations** | **List[str]** |  | 
**cpu_vendors** | **List[str]** |  | 
**cpu_architectures** | **List[str]** |  | 
**pricing_units** | **List[str]** |  | 
**price_types** | **List[str]** |  | 
**currencies** | **List[str]** |  | 
**gpu_count_min** | **int** | Minimum GPU count observed across offers. | 
**gpu_count_max** | **int** | Maximum GPU count observed across offers. | 
**gpu_memory_mib_min** | **int** | Minimum per-GPU memory (MiB) observed across offers. | 
**gpu_memory_mib_max** | **int** | Maximum per-GPU memory (MiB) observed across offers. | 
**total_gpu_memory_mib_min** | **int** | Minimum total GPU memory (MiB) observed across offers. | 
**total_gpu_memory_mib_max** | **int** | Maximum total GPU memory (MiB) observed across offers. | 
**main_memory_mib_min** | **int** | Minimum system memory (MiB) observed across offers. | 
**main_memory_mib_max** | **int** | Maximum system memory (MiB) observed across offers. | 
**num_vcpus_min** | **int** | Minimum vCPU count observed across offers. | 
**num_vcpus_max** | **int** | Maximum vCPU count observed across offers. | 
**price_min** | **float** | Minimum raw price observed across offers. | 
**price_max** | **float** | Maximum raw price observed across offers. | 
**hourly_cost_min** | **float** | Minimum normalized hourly cost observed across offers. | 
**hourly_cost_max** | **float** | Maximum normalized hourly cost observed across offers. | 

## Example

```python
from exalsius_api_client.models.offer_metadata_response import OfferMetadataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OfferMetadataResponse from a JSON string
offer_metadata_response_instance = OfferMetadataResponse.from_json(json)
# print the JSON string representation of the object
print(OfferMetadataResponse.to_json())

# convert the object into a dict
offer_metadata_response_dict = offer_metadata_response_instance.to_dict()
# create an instance of OfferMetadataResponse from a dict
offer_metadata_response_from_dict = OfferMetadataResponse.from_dict(offer_metadata_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


