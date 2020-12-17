// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export class Channel extends pulumi.CustomResource {
    /**
     * Get an existing Channel resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ChannelState, opts?: pulumi.CustomResourceOptions): Channel {
        return new Channel(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'commercetools:index/channel:Channel';

    /**
     * Returns true if the given object is an instance of Channel.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Channel {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Channel.__pulumiType;
    }

    public readonly description!: pulumi.Output<{[key: string]: any} | undefined>;
    public readonly key!: pulumi.Output<string>;
    public readonly name!: pulumi.Output<{[key: string]: any}>;
    public readonly roles!: pulumi.Output<string[]>;
    public /*out*/ readonly version!: pulumi.Output<number>;

    /**
     * Create a Channel resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ChannelArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ChannelArgs | ChannelState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as ChannelState | undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["key"] = state ? state.key : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["roles"] = state ? state.roles : undefined;
            inputs["version"] = state ? state.version : undefined;
        } else {
            const args = argsOrState as ChannelArgs | undefined;
            if (!args || args.key === undefined) {
                throw new Error("Missing required property 'key'");
            }
            if (!args || args.roles === undefined) {
                throw new Error("Missing required property 'roles'");
            }
            inputs["description"] = args ? args.description : undefined;
            inputs["key"] = args ? args.key : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["roles"] = args ? args.roles : undefined;
            inputs["version"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(Channel.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Channel resources.
 */
export interface ChannelState {
    readonly description?: pulumi.Input<{[key: string]: any}>;
    readonly key?: pulumi.Input<string>;
    readonly name?: pulumi.Input<{[key: string]: any}>;
    readonly roles?: pulumi.Input<pulumi.Input<string>[]>;
    readonly version?: pulumi.Input<number>;
}

/**
 * The set of arguments for constructing a Channel resource.
 */
export interface ChannelArgs {
    readonly description?: pulumi.Input<{[key: string]: any}>;
    readonly key: pulumi.Input<string>;
    readonly name?: pulumi.Input<{[key: string]: any}>;
    readonly roles: pulumi.Input<pulumi.Input<string>[]>;
}