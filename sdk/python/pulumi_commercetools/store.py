# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['StoreArgs', 'Store']

@pulumi.input_type
class StoreArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 countries: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 custom: Optional[pulumi.Input['StoreCustomArgs']] = None,
                 distribution_channels: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 languages: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 product_selections: Optional[pulumi.Input[Sequence[pulumi.Input['StoreProductSelectionArgs']]]] = None,
                 supply_channels: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Store resource.
        :param pulumi.Input[str] key: User-specific unique identifier for the store. The key is mandatory and immutable. It is used to reference the store
        :param pulumi.Input[Sequence[pulumi.Input[str]]] countries: A two-digit country code as per [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)
        :param pulumi.Input[Sequence[pulumi.Input[str]]] distribution_channels: Set of ResourceIdentifier to a Channel with ProductDistribution
        :param pulumi.Input[Sequence[pulumi.Input[str]]] languages: [IETF Language Tag](https://en.wikipedia.org/wiki/IETF_language_tag)
        :param pulumi.Input[Mapping[str, Any]] name: [LocalizedString](https://docs.commercetools.com/api/types#localizedstring)
        :param pulumi.Input[Sequence[pulumi.Input['StoreProductSelectionArgs']]] product_selections: Controls availability of Products for this Store via Product Selections
        :param pulumi.Input[Sequence[pulumi.Input[str]]] supply_channels: Set of ResourceIdentifier of Channels with InventorySupply
        """
        pulumi.set(__self__, "key", key)
        if countries is not None:
            pulumi.set(__self__, "countries", countries)
        if custom is not None:
            pulumi.set(__self__, "custom", custom)
        if distribution_channels is not None:
            pulumi.set(__self__, "distribution_channels", distribution_channels)
        if languages is not None:
            pulumi.set(__self__, "languages", languages)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if product_selections is not None:
            pulumi.set(__self__, "product_selections", product_selections)
        if supply_channels is not None:
            pulumi.set(__self__, "supply_channels", supply_channels)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        User-specific unique identifier for the store. The key is mandatory and immutable. It is used to reference the store
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def countries(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A two-digit country code as per [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)
        """
        return pulumi.get(self, "countries")

    @countries.setter
    def countries(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "countries", value)

    @property
    @pulumi.getter
    def custom(self) -> Optional[pulumi.Input['StoreCustomArgs']]:
        return pulumi.get(self, "custom")

    @custom.setter
    def custom(self, value: Optional[pulumi.Input['StoreCustomArgs']]):
        pulumi.set(self, "custom", value)

    @property
    @pulumi.getter(name="distributionChannels")
    def distribution_channels(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Set of ResourceIdentifier to a Channel with ProductDistribution
        """
        return pulumi.get(self, "distribution_channels")

    @distribution_channels.setter
    def distribution_channels(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "distribution_channels", value)

    @property
    @pulumi.getter
    def languages(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        [IETF Language Tag](https://en.wikipedia.org/wiki/IETF_language_tag)
        """
        return pulumi.get(self, "languages")

    @languages.setter
    def languages(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "languages", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        [LocalizedString](https://docs.commercetools.com/api/types#localizedstring)
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="productSelections")
    def product_selections(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['StoreProductSelectionArgs']]]]:
        """
        Controls availability of Products for this Store via Product Selections
        """
        return pulumi.get(self, "product_selections")

    @product_selections.setter
    def product_selections(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['StoreProductSelectionArgs']]]]):
        pulumi.set(self, "product_selections", value)

    @property
    @pulumi.getter(name="supplyChannels")
    def supply_channels(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Set of ResourceIdentifier of Channels with InventorySupply
        """
        return pulumi.get(self, "supply_channels")

    @supply_channels.setter
    def supply_channels(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "supply_channels", value)


@pulumi.input_type
class _StoreState:
    def __init__(__self__, *,
                 countries: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 custom: Optional[pulumi.Input['StoreCustomArgs']] = None,
                 distribution_channels: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 languages: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 product_selections: Optional[pulumi.Input[Sequence[pulumi.Input['StoreProductSelectionArgs']]]] = None,
                 supply_channels: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 version: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering Store resources.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] countries: A two-digit country code as per [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)
        :param pulumi.Input[Sequence[pulumi.Input[str]]] distribution_channels: Set of ResourceIdentifier to a Channel with ProductDistribution
        :param pulumi.Input[str] key: User-specific unique identifier for the store. The key is mandatory and immutable. It is used to reference the store
        :param pulumi.Input[Sequence[pulumi.Input[str]]] languages: [IETF Language Tag](https://en.wikipedia.org/wiki/IETF_language_tag)
        :param pulumi.Input[Mapping[str, Any]] name: [LocalizedString](https://docs.commercetools.com/api/types#localizedstring)
        :param pulumi.Input[Sequence[pulumi.Input['StoreProductSelectionArgs']]] product_selections: Controls availability of Products for this Store via Product Selections
        :param pulumi.Input[Sequence[pulumi.Input[str]]] supply_channels: Set of ResourceIdentifier of Channels with InventorySupply
        """
        if countries is not None:
            pulumi.set(__self__, "countries", countries)
        if custom is not None:
            pulumi.set(__self__, "custom", custom)
        if distribution_channels is not None:
            pulumi.set(__self__, "distribution_channels", distribution_channels)
        if key is not None:
            pulumi.set(__self__, "key", key)
        if languages is not None:
            pulumi.set(__self__, "languages", languages)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if product_selections is not None:
            pulumi.set(__self__, "product_selections", product_selections)
        if supply_channels is not None:
            pulumi.set(__self__, "supply_channels", supply_channels)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def countries(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A two-digit country code as per [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)
        """
        return pulumi.get(self, "countries")

    @countries.setter
    def countries(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "countries", value)

    @property
    @pulumi.getter
    def custom(self) -> Optional[pulumi.Input['StoreCustomArgs']]:
        return pulumi.get(self, "custom")

    @custom.setter
    def custom(self, value: Optional[pulumi.Input['StoreCustomArgs']]):
        pulumi.set(self, "custom", value)

    @property
    @pulumi.getter(name="distributionChannels")
    def distribution_channels(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Set of ResourceIdentifier to a Channel with ProductDistribution
        """
        return pulumi.get(self, "distribution_channels")

    @distribution_channels.setter
    def distribution_channels(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "distribution_channels", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        """
        User-specific unique identifier for the store. The key is mandatory and immutable. It is used to reference the store
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def languages(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        [IETF Language Tag](https://en.wikipedia.org/wiki/IETF_language_tag)
        """
        return pulumi.get(self, "languages")

    @languages.setter
    def languages(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "languages", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        [LocalizedString](https://docs.commercetools.com/api/types#localizedstring)
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="productSelections")
    def product_selections(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['StoreProductSelectionArgs']]]]:
        """
        Controls availability of Products for this Store via Product Selections
        """
        return pulumi.get(self, "product_selections")

    @product_selections.setter
    def product_selections(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['StoreProductSelectionArgs']]]]):
        pulumi.set(self, "product_selections", value)

    @property
    @pulumi.getter(name="supplyChannels")
    def supply_channels(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Set of ResourceIdentifier of Channels with InventorySupply
        """
        return pulumi.get(self, "supply_channels")

    @supply_channels.setter
    def supply_channels(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "supply_channels", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "version", value)


class Store(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 countries: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 custom: Optional[pulumi.Input[pulumi.InputType['StoreCustomArgs']]] = None,
                 distribution_channels: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 languages: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 product_selections: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StoreProductSelectionArgs']]]]] = None,
                 supply_channels: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Create a Store resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] countries: A two-digit country code as per [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)
        :param pulumi.Input[Sequence[pulumi.Input[str]]] distribution_channels: Set of ResourceIdentifier to a Channel with ProductDistribution
        :param pulumi.Input[str] key: User-specific unique identifier for the store. The key is mandatory and immutable. It is used to reference the store
        :param pulumi.Input[Sequence[pulumi.Input[str]]] languages: [IETF Language Tag](https://en.wikipedia.org/wiki/IETF_language_tag)
        :param pulumi.Input[Mapping[str, Any]] name: [LocalizedString](https://docs.commercetools.com/api/types#localizedstring)
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StoreProductSelectionArgs']]]] product_selections: Controls availability of Products for this Store via Product Selections
        :param pulumi.Input[Sequence[pulumi.Input[str]]] supply_channels: Set of ResourceIdentifier of Channels with InventorySupply
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: StoreArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Store resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param StoreArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(StoreArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 countries: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 custom: Optional[pulumi.Input[pulumi.InputType['StoreCustomArgs']]] = None,
                 distribution_channels: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 languages: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 product_selections: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StoreProductSelectionArgs']]]]] = None,
                 supply_channels: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = StoreArgs.__new__(StoreArgs)

            __props__.__dict__["countries"] = countries
            __props__.__dict__["custom"] = custom
            __props__.__dict__["distribution_channels"] = distribution_channels
            if key is None and not opts.urn:
                raise TypeError("Missing required property 'key'")
            __props__.__dict__["key"] = key
            __props__.__dict__["languages"] = languages
            __props__.__dict__["name"] = name
            __props__.__dict__["product_selections"] = product_selections
            __props__.__dict__["supply_channels"] = supply_channels
            __props__.__dict__["version"] = None
        super(Store, __self__).__init__(
            'commercetools:index/store:Store',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            countries: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            custom: Optional[pulumi.Input[pulumi.InputType['StoreCustomArgs']]] = None,
            distribution_channels: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            key: Optional[pulumi.Input[str]] = None,
            languages: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            name: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            product_selections: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StoreProductSelectionArgs']]]]] = None,
            supply_channels: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            version: Optional[pulumi.Input[int]] = None) -> 'Store':
        """
        Get an existing Store resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] countries: A two-digit country code as per [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)
        :param pulumi.Input[Sequence[pulumi.Input[str]]] distribution_channels: Set of ResourceIdentifier to a Channel with ProductDistribution
        :param pulumi.Input[str] key: User-specific unique identifier for the store. The key is mandatory and immutable. It is used to reference the store
        :param pulumi.Input[Sequence[pulumi.Input[str]]] languages: [IETF Language Tag](https://en.wikipedia.org/wiki/IETF_language_tag)
        :param pulumi.Input[Mapping[str, Any]] name: [LocalizedString](https://docs.commercetools.com/api/types#localizedstring)
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StoreProductSelectionArgs']]]] product_selections: Controls availability of Products for this Store via Product Selections
        :param pulumi.Input[Sequence[pulumi.Input[str]]] supply_channels: Set of ResourceIdentifier of Channels with InventorySupply
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _StoreState.__new__(_StoreState)

        __props__.__dict__["countries"] = countries
        __props__.__dict__["custom"] = custom
        __props__.__dict__["distribution_channels"] = distribution_channels
        __props__.__dict__["key"] = key
        __props__.__dict__["languages"] = languages
        __props__.__dict__["name"] = name
        __props__.__dict__["product_selections"] = product_selections
        __props__.__dict__["supply_channels"] = supply_channels
        __props__.__dict__["version"] = version
        return Store(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def countries(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A two-digit country code as per [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)
        """
        return pulumi.get(self, "countries")

    @property
    @pulumi.getter
    def custom(self) -> pulumi.Output[Optional['outputs.StoreCustom']]:
        return pulumi.get(self, "custom")

    @property
    @pulumi.getter(name="distributionChannels")
    def distribution_channels(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Set of ResourceIdentifier to a Channel with ProductDistribution
        """
        return pulumi.get(self, "distribution_channels")

    @property
    @pulumi.getter
    def key(self) -> pulumi.Output[str]:
        """
        User-specific unique identifier for the store. The key is mandatory and immutable. It is used to reference the store
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def languages(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        [IETF Language Tag](https://en.wikipedia.org/wiki/IETF_language_tag)
        """
        return pulumi.get(self, "languages")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        [LocalizedString](https://docs.commercetools.com/api/types#localizedstring)
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="productSelections")
    def product_selections(self) -> pulumi.Output[Optional[Sequence['outputs.StoreProductSelection']]]:
        """
        Controls availability of Products for this Store via Product Selections
        """
        return pulumi.get(self, "product_selections")

    @property
    @pulumi.getter(name="supplyChannels")
    def supply_channels(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Set of ResourceIdentifier of Channels with InventorySupply
        """
        return pulumi.get(self, "supply_channels")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[int]:
        return pulumi.get(self, "version")

