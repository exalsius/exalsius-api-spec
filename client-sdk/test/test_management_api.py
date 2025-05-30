# coding: utf-8

"""
exalsius API

The exalsius REST API provides programmatic access to the core functionality of the exalsius ecosystem It is consumed directly by the exls CLI tool and can also be integrated into custom applications or scripts. Key points: * **CLI & Programmatic Access**   All operations are available via the `exls` command-line application or through standard HTTP requests.  * **GPU Market Offers** Retrieve and compare GPU instance pricing across public cloud providers and hyperscalers to identify the most cost-effective options. * **Operator Integration**   Works in conjunction with the [exalsius-operator](https://github.com/exalsius/exalsius-operator) deployed in a management Kubernetes cluster, to manage infrastructure and node lifecycles.  * **Node Management**   Import self-managed (SSH) and cloud-provider instances into your node pool with dedicated endpoints.  * **Cluster Provisioning**   Create and manage Kubernetes clusters across supported cloud providers and self-managed (bare-metal) nodes.  * **Service Deployment**   Deploy additional services—such as the NVIDIA GPU Operator, KubeRay, Flyte, or Kubeflow—using the API’s service-deployment endpoints.

The version of the OpenAPI document: 1.0.0
Contact: support@exalsius.ai
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


import unittest

from exalsius_api_client.api.management_api import ManagementApi


class TestManagementApi(unittest.TestCase):
    """ManagementApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ManagementApi()

    def tearDown(self) -> None:
        pass

    def test_add_ssh_key(self) -> None:
        """Test case for add_ssh_key

        Add an SSH key
        """
        pass

    def test_delete_ssh_key(self) -> None:
        """Test case for delete_ssh_key

        Delete an SSH key
        """
        pass

    def test_list_ssh_keys(self) -> None:
        """Test case for list_ssh_keys

        List all SSH keys
        """
        pass


if __name__ == "__main__":
    unittest.main()
