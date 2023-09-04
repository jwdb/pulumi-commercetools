# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from . import _utilities
import typing
# Export this package's modules as members:
from .api_client import *
from .api_extension import *
from .associate_role import *
from .attribute_group import *
from .cart_discount import *
from .category import *
from .channel import *
from .custom_object import *
from .customer_group import *
from .discount_code import *
from .get_state import *
from .get_type import *
from .product_discount import *
from .product_type import *
from .project_settings import *
from .provider import *
from .shipping_method import *
from .shipping_zone import *
from .shipping_zone_rate import *
from .state import *
from .state_transitions import *
from .store import *
from .subscription import *
from .tax_category import *
from .tax_category_rate import *
from .type import *
from ._inputs import *
from . import outputs

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_commercetools.config as __config
    config = __config
else:
    config = _utilities.lazy_import('pulumi_commercetools.config')

_utilities.register(
    resource_modules="""
[
 {
  "pkg": "commercetools",
  "mod": "index/apiClient",
  "fqn": "pulumi_commercetools",
  "classes": {
   "commercetools:index/apiClient:ApiClient": "ApiClient"
  }
 },
 {
  "pkg": "commercetools",
  "mod": "index/apiExtension",
  "fqn": "pulumi_commercetools",
  "classes": {
   "commercetools:index/apiExtension:ApiExtension": "ApiExtension"
  }
 },
 {
  "pkg": "commercetools",
  "mod": "index/associateRole",
  "fqn": "pulumi_commercetools",
  "classes": {
   "commercetools:index/associateRole:AssociateRole": "AssociateRole"
  }
 },
 {
  "pkg": "commercetools",
  "mod": "index/attributeGroup",
  "fqn": "pulumi_commercetools",
  "classes": {
   "commercetools:index/attributeGroup:AttributeGroup": "AttributeGroup"
  }
 },
 {
  "pkg": "commercetools",
  "mod": "index/cartDiscount",
  "fqn": "pulumi_commercetools",
  "classes": {
   "commercetools:index/cartDiscount:CartDiscount": "CartDiscount"
  }
 },
 {
  "pkg": "commercetools",
  "mod": "index/category",
  "fqn": "pulumi_commercetools",
  "classes": {
   "commercetools:index/category:Category": "Category"
  }
 },
 {
  "pkg": "commercetools",
  "mod": "index/channel",
  "fqn": "pulumi_commercetools",
  "classes": {
   "commercetools:index/channel:Channel": "Channel"
  }
 },
 {
  "pkg": "commercetools",
  "mod": "index/customObject",
  "fqn": "pulumi_commercetools",
  "classes": {
   "commercetools:index/customObject:CustomObject": "CustomObject"
  }
 },
 {
  "pkg": "commercetools",
  "mod": "index/customerGroup",
  "fqn": "pulumi_commercetools",
  "classes": {
   "commercetools:index/customerGroup:CustomerGroup": "CustomerGroup"
  }
 },
 {
  "pkg": "commercetools",
  "mod": "index/discountCode",
  "fqn": "pulumi_commercetools",
  "classes": {
   "commercetools:index/discountCode:DiscountCode": "DiscountCode"
  }
 },
 {
  "pkg": "commercetools",
  "mod": "index/productDiscount",
  "fqn": "pulumi_commercetools",
  "classes": {
   "commercetools:index/productDiscount:ProductDiscount": "ProductDiscount"
  }
 },
 {
  "pkg": "commercetools",
  "mod": "index/productType",
  "fqn": "pulumi_commercetools",
  "classes": {
   "commercetools:index/productType:ProductType": "ProductType"
  }
 },
 {
  "pkg": "commercetools",
  "mod": "index/projectSettings",
  "fqn": "pulumi_commercetools",
  "classes": {
   "commercetools:index/projectSettings:ProjectSettings": "ProjectSettings"
  }
 },
 {
  "pkg": "commercetools",
  "mod": "index/shippingMethod",
  "fqn": "pulumi_commercetools",
  "classes": {
   "commercetools:index/shippingMethod:ShippingMethod": "ShippingMethod"
  }
 },
 {
  "pkg": "commercetools",
  "mod": "index/shippingZone",
  "fqn": "pulumi_commercetools",
  "classes": {
   "commercetools:index/shippingZone:ShippingZone": "ShippingZone"
  }
 },
 {
  "pkg": "commercetools",
  "mod": "index/shippingZoneRate",
  "fqn": "pulumi_commercetools",
  "classes": {
   "commercetools:index/shippingZoneRate:ShippingZoneRate": "ShippingZoneRate"
  }
 },
 {
  "pkg": "commercetools",
  "mod": "index/state",
  "fqn": "pulumi_commercetools",
  "classes": {
   "commercetools:index/state:State": "State"
  }
 },
 {
  "pkg": "commercetools",
  "mod": "index/stateTransitions",
  "fqn": "pulumi_commercetools",
  "classes": {
   "commercetools:index/stateTransitions:StateTransitions": "StateTransitions"
  }
 },
 {
  "pkg": "commercetools",
  "mod": "index/store",
  "fqn": "pulumi_commercetools",
  "classes": {
   "commercetools:index/store:Store": "Store"
  }
 },
 {
  "pkg": "commercetools",
  "mod": "index/subscription",
  "fqn": "pulumi_commercetools",
  "classes": {
   "commercetools:index/subscription:Subscription": "Subscription"
  }
 },
 {
  "pkg": "commercetools",
  "mod": "index/taxCategory",
  "fqn": "pulumi_commercetools",
  "classes": {
   "commercetools:index/taxCategory:TaxCategory": "TaxCategory"
  }
 },
 {
  "pkg": "commercetools",
  "mod": "index/taxCategoryRate",
  "fqn": "pulumi_commercetools",
  "classes": {
   "commercetools:index/taxCategoryRate:TaxCategoryRate": "TaxCategoryRate"
  }
 },
 {
  "pkg": "commercetools",
  "mod": "index/type",
  "fqn": "pulumi_commercetools",
  "classes": {
   "commercetools:index/type:Type": "Type"
  }
 }
]
""",
    resource_packages="""
[
 {
  "pkg": "commercetools",
  "token": "pulumi:providers:commercetools",
  "fqn": "pulumi_commercetools",
  "class": "Provider"
 }
]
"""
)
