# NodeImportSshRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostname** | **str** | The hostname of the node | 
**endpoint** | **str** | IP or hostname reachable over SSH | 
**username** | **str** | Username to access the node | 
**ssh_key_id** | **str** | The ID of the SSH key to use for the node | 
**description** | **str** | Description of the node | [optional] 
**price_per_hour** | **float** | Price per hour for the node, in USD | [optional] [default to 0]

## Example

```python
from exalsius_api_client.models.node_import_ssh_request import NodeImportSshRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NodeImportSshRequest from a JSON string
node_import_ssh_request_instance = NodeImportSshRequest.from_json(json)
# print the JSON string representation of the object
print(NodeImportSshRequest.to_json())

# convert the object into a dict
node_import_ssh_request_dict = node_import_ssh_request_instance.to_dict()
# create an instance of NodeImportSshRequest from a dict
node_import_ssh_request_from_dict = NodeImportSshRequest.from_dict(node_import_ssh_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


