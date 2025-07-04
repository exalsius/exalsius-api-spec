# coding: utf-8

"""
exalsius API

The exalsius REST API provides programmatic access to the core functionality of the exalsius ecosystem It is consumed directly by the exls CLI tool and can also be integrated into custom applications or scripts. Key points: * **CLI & Programmatic Access**   All operations are available via the `exls` command-line application or through standard HTTP requests.  * **GPU Market Offers** Retrieve and compare GPU instance pricing across public cloud providers and hyperscalers to identify the most cost-effective options. * **Operator Integration**   Works in conjunction with the [exalsius-operator](https://github.com/exalsius/exalsius-operator) deployed in a management Kubernetes cluster, to manage infrastructure and node lifecycles.  * **Node Management**   Import self-managed (SSH) and cloud-provider instances into your node pool with dedicated endpoints.  * **Cluster Provisioning**   Create and manage Kubernetes clusters across supported cloud providers and self-managed (bare-metal) nodes.  * **Service Deployment**   Deploy additional services—such as the NVIDIA GPU Operator, KubeRay, Flyte, or Kubeflow—using the API’s service-deployment endpoints.

The version of the OpenAPI document: 1.7.0
Contact: support@exalsius.ai
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import json
import pprint
import re  # noqa: F401
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing_extensions import Self

from exalsius_api_client.models.offer import Offer


class OffersListResponse(BaseModel):
    """
    OffersListResponse
    """  # noqa: E501

    offers: List[Offer]
    total: StrictInt = Field(
        description="The total number of offers matching the filters"
    )
    next_cursor: Optional[StrictStr] = Field(
        default=None,
        description="The cursor for the next page. If null, there are no more results.",
    )
    prev_cursor: Optional[StrictStr] = Field(
        default=None,
        description="The cursor for the previous page. If null, this is the first page.",
    )
    __properties: ClassVar[List[str]] = [
        "offers",
        "total",
        "next_cursor",
        "prev_cursor",
    ]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of OffersListResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in offers (list)
        _items = []
        if self.offers:
            for _item_offers in self.offers:
                if _item_offers:
                    _items.append(_item_offers.to_dict())
            _dict["offers"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OffersListResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "offers": (
                    [Offer.from_dict(_item) for _item in obj["offers"]]
                    if obj.get("offers") is not None
                    else None
                ),
                "total": obj.get("total"),
                "next_cursor": obj.get("next_cursor"),
                "prev_cursor": obj.get("prev_cursor"),
            }
        )
        return _obj
