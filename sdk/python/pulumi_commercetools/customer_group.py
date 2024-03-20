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

__all__ = ['CustomerGroupArgs', 'CustomerGroup']

@pulumi.input_type
class CustomerGroupArgs:
    def __init__(__self__, *,
                 custom: Optional[pulumi.Input['CustomerGroupCustomArgs']] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a CustomerGroup resource.
        :param pulumi.Input[str] key: User-specific unique identifier for the customer group
        :param pulumi.Input[str] name: Unique within the project
        """
        if custom is not None:
            pulumi.set(__self__, "custom", custom)
        if key is not None:
            pulumi.set(__self__, "key", key)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def custom(self) -> Optional[pulumi.Input['CustomerGroupCustomArgs']]:
        return pulumi.get(self, "custom")

    @custom.setter
    def custom(self, value: Optional[pulumi.Input['CustomerGroupCustomArgs']]):
        pulumi.set(self, "custom", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        """
        User-specific unique identifier for the customer group
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Unique within the project
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _CustomerGroupState:
    def __init__(__self__, *,
                 custom: Optional[pulumi.Input['CustomerGroupCustomArgs']] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering CustomerGroup resources.
        :param pulumi.Input[str] key: User-specific unique identifier for the customer group
        :param pulumi.Input[str] name: Unique within the project
        """
        if custom is not None:
            pulumi.set(__self__, "custom", custom)
        if key is not None:
            pulumi.set(__self__, "key", key)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def custom(self) -> Optional[pulumi.Input['CustomerGroupCustomArgs']]:
        return pulumi.get(self, "custom")

    @custom.setter
    def custom(self, value: Optional[pulumi.Input['CustomerGroupCustomArgs']]):
        pulumi.set(self, "custom", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        """
        User-specific unique identifier for the customer group
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Unique within the project
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "version", value)


class CustomerGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 custom: Optional[pulumi.Input[pulumi.InputType['CustomerGroupCustomArgs']]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a CustomerGroup resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] key: User-specific unique identifier for the customer group
        :param pulumi.Input[str] name: Unique within the project
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[CustomerGroupArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a CustomerGroup resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param CustomerGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CustomerGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 custom: Optional[pulumi.Input[pulumi.InputType['CustomerGroupCustomArgs']]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CustomerGroupArgs.__new__(CustomerGroupArgs)

            __props__.__dict__["custom"] = custom
            __props__.__dict__["key"] = key
            __props__.__dict__["name"] = name
            __props__.__dict__["version"] = None
        super(CustomerGroup, __self__).__init__(
            'commercetools:index/customerGroup:CustomerGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            custom: Optional[pulumi.Input[pulumi.InputType['CustomerGroupCustomArgs']]] = None,
            key: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            version: Optional[pulumi.Input[int]] = None) -> 'CustomerGroup':
        """
        Get an existing CustomerGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] key: User-specific unique identifier for the customer group
        :param pulumi.Input[str] name: Unique within the project
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CustomerGroupState.__new__(_CustomerGroupState)

        __props__.__dict__["custom"] = custom
        __props__.__dict__["key"] = key
        __props__.__dict__["name"] = name
        __props__.__dict__["version"] = version
        return CustomerGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def custom(self) -> pulumi.Output[Optional['outputs.CustomerGroupCustom']]:
        return pulumi.get(self, "custom")

    @property
    @pulumi.getter
    def key(self) -> pulumi.Output[Optional[str]]:
        """
        User-specific unique identifier for the customer group
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Unique within the project
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[int]:
        return pulumi.get(self, "version")
