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

__all__ = ['ChannelArgs', 'Channel']

@pulumi.input_type
class ChannelArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 roles: pulumi.Input[Sequence[pulumi.Input[str]]],
                 address: Optional[pulumi.Input['ChannelAddressArgs']] = None,
                 custom: Optional[pulumi.Input['ChannelCustomArgs']] = None,
                 description: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 geolocation: Optional[pulumi.Input['ChannelGeolocationArgs']] = None,
                 name: Optional[pulumi.Input[Mapping[str, Any]]] = None):
        """
        The set of arguments for constructing a Channel resource.
        :param pulumi.Input[str] key: Any arbitrary string key that uniquely identifies this channel within the project
        :param pulumi.Input[Sequence[pulumi.Input[str]]] roles: The [roles](https://docs.commercetools.com/api/projects/channels#channelroleenum) of this channel. Each channel must
               have at least one role
        :param pulumi.Input[Mapping[str, Any]] description: [LocalizedString](https://docs.commercetools.com/api/types#localizedstring)
        :param pulumi.Input[Mapping[str, Any]] name: [LocalizedString](https://docs.commercetools.com/api/types#localizedstring)
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "roles", roles)
        if address is not None:
            pulumi.set(__self__, "address", address)
        if custom is not None:
            pulumi.set(__self__, "custom", custom)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if geolocation is not None:
            pulumi.set(__self__, "geolocation", geolocation)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        Any arbitrary string key that uniquely identifies this channel within the project
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def roles(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        The [roles](https://docs.commercetools.com/api/projects/channels#channelroleenum) of this channel. Each channel must
        have at least one role
        """
        return pulumi.get(self, "roles")

    @roles.setter
    def roles(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "roles", value)

    @property
    @pulumi.getter
    def address(self) -> Optional[pulumi.Input['ChannelAddressArgs']]:
        return pulumi.get(self, "address")

    @address.setter
    def address(self, value: Optional[pulumi.Input['ChannelAddressArgs']]):
        pulumi.set(self, "address", value)

    @property
    @pulumi.getter
    def custom(self) -> Optional[pulumi.Input['ChannelCustomArgs']]:
        return pulumi.get(self, "custom")

    @custom.setter
    def custom(self, value: Optional[pulumi.Input['ChannelCustomArgs']]):
        pulumi.set(self, "custom", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        [LocalizedString](https://docs.commercetools.com/api/types#localizedstring)
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def geolocation(self) -> Optional[pulumi.Input['ChannelGeolocationArgs']]:
        return pulumi.get(self, "geolocation")

    @geolocation.setter
    def geolocation(self, value: Optional[pulumi.Input['ChannelGeolocationArgs']]):
        pulumi.set(self, "geolocation", value)

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


@pulumi.input_type
class _ChannelState:
    def __init__(__self__, *,
                 address: Optional[pulumi.Input['ChannelAddressArgs']] = None,
                 custom: Optional[pulumi.Input['ChannelCustomArgs']] = None,
                 description: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 geolocation: Optional[pulumi.Input['ChannelGeolocationArgs']] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 roles: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 version: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering Channel resources.
        :param pulumi.Input[Mapping[str, Any]] description: [LocalizedString](https://docs.commercetools.com/api/types#localizedstring)
        :param pulumi.Input[str] key: Any arbitrary string key that uniquely identifies this channel within the project
        :param pulumi.Input[Mapping[str, Any]] name: [LocalizedString](https://docs.commercetools.com/api/types#localizedstring)
        :param pulumi.Input[Sequence[pulumi.Input[str]]] roles: The [roles](https://docs.commercetools.com/api/projects/channels#channelroleenum) of this channel. Each channel must
               have at least one role
        """
        if address is not None:
            pulumi.set(__self__, "address", address)
        if custom is not None:
            pulumi.set(__self__, "custom", custom)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if geolocation is not None:
            pulumi.set(__self__, "geolocation", geolocation)
        if key is not None:
            pulumi.set(__self__, "key", key)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if roles is not None:
            pulumi.set(__self__, "roles", roles)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def address(self) -> Optional[pulumi.Input['ChannelAddressArgs']]:
        return pulumi.get(self, "address")

    @address.setter
    def address(self, value: Optional[pulumi.Input['ChannelAddressArgs']]):
        pulumi.set(self, "address", value)

    @property
    @pulumi.getter
    def custom(self) -> Optional[pulumi.Input['ChannelCustomArgs']]:
        return pulumi.get(self, "custom")

    @custom.setter
    def custom(self, value: Optional[pulumi.Input['ChannelCustomArgs']]):
        pulumi.set(self, "custom", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        [LocalizedString](https://docs.commercetools.com/api/types#localizedstring)
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def geolocation(self) -> Optional[pulumi.Input['ChannelGeolocationArgs']]:
        return pulumi.get(self, "geolocation")

    @geolocation.setter
    def geolocation(self, value: Optional[pulumi.Input['ChannelGeolocationArgs']]):
        pulumi.set(self, "geolocation", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        """
        Any arbitrary string key that uniquely identifies this channel within the project
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)

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
    @pulumi.getter
    def roles(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The [roles](https://docs.commercetools.com/api/projects/channels#channelroleenum) of this channel. Each channel must
        have at least one role
        """
        return pulumi.get(self, "roles")

    @roles.setter
    def roles(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "roles", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "version", value)


class Channel(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 address: Optional[pulumi.Input[pulumi.InputType['ChannelAddressArgs']]] = None,
                 custom: Optional[pulumi.Input[pulumi.InputType['ChannelCustomArgs']]] = None,
                 description: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 geolocation: Optional[pulumi.Input[pulumi.InputType['ChannelGeolocationArgs']]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 roles: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Create a Channel resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, Any]] description: [LocalizedString](https://docs.commercetools.com/api/types#localizedstring)
        :param pulumi.Input[str] key: Any arbitrary string key that uniquely identifies this channel within the project
        :param pulumi.Input[Mapping[str, Any]] name: [LocalizedString](https://docs.commercetools.com/api/types#localizedstring)
        :param pulumi.Input[Sequence[pulumi.Input[str]]] roles: The [roles](https://docs.commercetools.com/api/projects/channels#channelroleenum) of this channel. Each channel must
               have at least one role
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ChannelArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Channel resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param ChannelArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ChannelArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 address: Optional[pulumi.Input[pulumi.InputType['ChannelAddressArgs']]] = None,
                 custom: Optional[pulumi.Input[pulumi.InputType['ChannelCustomArgs']]] = None,
                 description: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 geolocation: Optional[pulumi.Input[pulumi.InputType['ChannelGeolocationArgs']]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 roles: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ChannelArgs.__new__(ChannelArgs)

            __props__.__dict__["address"] = address
            __props__.__dict__["custom"] = custom
            __props__.__dict__["description"] = description
            __props__.__dict__["geolocation"] = geolocation
            if key is None and not opts.urn:
                raise TypeError("Missing required property 'key'")
            __props__.__dict__["key"] = key
            __props__.__dict__["name"] = name
            if roles is None and not opts.urn:
                raise TypeError("Missing required property 'roles'")
            __props__.__dict__["roles"] = roles
            __props__.__dict__["version"] = None
        super(Channel, __self__).__init__(
            'commercetools:index/channel:Channel',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            address: Optional[pulumi.Input[pulumi.InputType['ChannelAddressArgs']]] = None,
            custom: Optional[pulumi.Input[pulumi.InputType['ChannelCustomArgs']]] = None,
            description: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            geolocation: Optional[pulumi.Input[pulumi.InputType['ChannelGeolocationArgs']]] = None,
            key: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            roles: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            version: Optional[pulumi.Input[int]] = None) -> 'Channel':
        """
        Get an existing Channel resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, Any]] description: [LocalizedString](https://docs.commercetools.com/api/types#localizedstring)
        :param pulumi.Input[str] key: Any arbitrary string key that uniquely identifies this channel within the project
        :param pulumi.Input[Mapping[str, Any]] name: [LocalizedString](https://docs.commercetools.com/api/types#localizedstring)
        :param pulumi.Input[Sequence[pulumi.Input[str]]] roles: The [roles](https://docs.commercetools.com/api/projects/channels#channelroleenum) of this channel. Each channel must
               have at least one role
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ChannelState.__new__(_ChannelState)

        __props__.__dict__["address"] = address
        __props__.__dict__["custom"] = custom
        __props__.__dict__["description"] = description
        __props__.__dict__["geolocation"] = geolocation
        __props__.__dict__["key"] = key
        __props__.__dict__["name"] = name
        __props__.__dict__["roles"] = roles
        __props__.__dict__["version"] = version
        return Channel(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def address(self) -> pulumi.Output[Optional['outputs.ChannelAddress']]:
        return pulumi.get(self, "address")

    @property
    @pulumi.getter
    def custom(self) -> pulumi.Output[Optional['outputs.ChannelCustom']]:
        return pulumi.get(self, "custom")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        """
        [LocalizedString](https://docs.commercetools.com/api/types#localizedstring)
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def geolocation(self) -> pulumi.Output[Optional['outputs.ChannelGeolocation']]:
        return pulumi.get(self, "geolocation")

    @property
    @pulumi.getter
    def key(self) -> pulumi.Output[str]:
        """
        Any arbitrary string key that uniquely identifies this channel within the project
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        """
        [LocalizedString](https://docs.commercetools.com/api/types#localizedstring)
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def roles(self) -> pulumi.Output[Sequence[str]]:
        """
        The [roles](https://docs.commercetools.com/api/projects/channels#channelroleenum) of this channel. Each channel must
        have at least one role
        """
        return pulumi.get(self, "roles")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[int]:
        return pulumi.get(self, "version")

