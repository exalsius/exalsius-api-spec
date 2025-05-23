# CloudNode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** | The cloud provider of the node | [optional] 
**region** | **str** | The region of the node | [optional] 
**availability_zone** | **str** | The availability zone of the node | [optional] 
**instance_type** | **str** | The instance type of the node | [optional] 
**price_per_hour** | **float** | The price per hour for the node | [optional] 

## Example

```python
from exalsius_api_client.models.cloud_node import CloudNode

# TODO update the JSON string below
json = "{}"
# create an instance of CloudNode from a JSON string
cloud_node_instance = CloudNode.from_json(json)
# print the JSON string representation of the object
print(CloudNode.to_json())

# convert the object into a dict
cloud_node_dict = cloud_node_instance.to_dict()
# create an instance of CloudNode from a dict
cloud_node_from_dict = CloudNode.from_dict(cloud_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


