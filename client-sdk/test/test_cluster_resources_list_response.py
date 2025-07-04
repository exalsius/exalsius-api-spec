# coding: utf-8

"""
exalsius API

The exalsius REST API provides programmatic access to the core functionality of the exalsius ecosystem It is consumed directly by the exls CLI tool and can also be integrated into custom applications or scripts. Key points: * **CLI & Programmatic Access**   All operations are available via the `exls` command-line application or through standard HTTP requests.  * **GPU Market Offers** Retrieve and compare GPU instance pricing across public cloud providers and hyperscalers to identify the most cost-effective options. * **Operator Integration**   Works in conjunction with the [exalsius-operator](https://github.com/exalsius/exalsius-operator) deployed in a management Kubernetes cluster, to manage infrastructure and node lifecycles.  * **Node Management**   Import self-managed (SSH) and cloud-provider instances into your node pool with dedicated endpoints.  * **Cluster Provisioning**   Create and manage Kubernetes clusters across supported cloud providers and self-managed (bare-metal) nodes.  * **Service Deployment**   Deploy additional services—such as the NVIDIA GPU Operator, KubeRay, Flyte, or Kubeflow—using the API’s service-deployment endpoints.

The version of the OpenAPI document: 1.5.1
Contact: support@exalsius.ai
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


import unittest

from exalsius_api_client.models.cluster_resources_list_response import \
    ClusterResourcesListResponse


class TestClusterResourcesListResponse(unittest.TestCase):
    """ClusterResourcesListResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ClusterResourcesListResponse:
        """Test ClusterResourcesListResponse
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ClusterResourcesListResponse`
        """
        model = ClusterResourcesListResponse()
        if include_optional:
            return ClusterResourcesListResponse(
                resources = [
                    exalsius_api_client.models.cluster_resources_list_response_resources_inner.cluster_resources_list_response_resources_inner(
                        node_id = '123e4567-e89b-12d3-a456-426614174000', 
                        available = exalsius_api_client.models.resource_pool.resource-pool(
                            gpu_count = 1, 
                            gpu_vendor = 'nvidia', 
                            gpu_type = 'a100', 
                            cpu_cores = 4, 
                            memory_gb = 16, 
                            storage_gb = 100, ), 
                        occupied = exalsius_api_client.models.resource_pool.resource-pool(
                            gpu_count = 1, 
                            gpu_vendor = 'nvidia', 
                            gpu_type = 'a100', 
                            cpu_cores = 4, 
                            memory_gb = 16, 
                            storage_gb = 100, ), )
                    ],
                total = 56
            )
        else:
            return ClusterResourcesListResponse(
                resources = [
                    exalsius_api_client.models.cluster_resources_list_response_resources_inner.cluster_resources_list_response_resources_inner(
                        node_id = '123e4567-e89b-12d3-a456-426614174000', 
                        available = exalsius_api_client.models.resource_pool.resource-pool(
                            gpu_count = 1, 
                            gpu_vendor = 'nvidia', 
                            gpu_type = 'a100', 
                            cpu_cores = 4, 
                            memory_gb = 16, 
                            storage_gb = 100, ), 
                        occupied = exalsius_api_client.models.resource_pool.resource-pool(
                            gpu_count = 1, 
                            gpu_vendor = 'nvidia', 
                            gpu_type = 'a100', 
                            cpu_cores = 4, 
                            memory_gb = 16, 
                            storage_gb = 100, ), )
                    ],
        )
        """

    def testClusterResourcesListResponse(self):
        """Test ClusterResourcesListResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
