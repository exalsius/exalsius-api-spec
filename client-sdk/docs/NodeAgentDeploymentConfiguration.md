# NodeAgentDeploymentConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refresh_token** | **str** | The refresh token for the node agent | 

## Example

```python
from exalsius_api_client.models.node_agent_deployment_configuration import NodeAgentDeploymentConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of NodeAgentDeploymentConfiguration from a JSON string
node_agent_deployment_configuration_instance = NodeAgentDeploymentConfiguration.from_json(json)
# print the JSON string representation of the object
print(NodeAgentDeploymentConfiguration.to_json())

# convert the object into a dict
node_agent_deployment_configuration_dict = node_agent_deployment_configuration_instance.to_dict()
# create an instance of NodeAgentDeploymentConfiguration from a dict
node_agent_deployment_configuration_from_dict = NodeAgentDeploymentConfiguration.from_dict(node_agent_deployment_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


