// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

export class Type extends pulumi.CustomResource {
    /**
     * Get an existing Type resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TypeState, opts?: pulumi.CustomResourceOptions): Type {
        return new Type(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'commercetools:index/type:Type';

    /**
     * Returns true if the given object is an instance of Type.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Type {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Type.__pulumiType;
    }

    /**
     * [LocalizedString](https://docs.commercetools.com/api/types#localizedstring)
     */
    public readonly description!: pulumi.Output<{[key: string]: any} | undefined>;
    /**
     * [Field definition](https://docs.commercetools.com/api/projects/types#fielddefinition)
     */
    public readonly fields!: pulumi.Output<outputs.TypeField[] | undefined>;
    /**
     * Identifier for the type (max. 256 characters)
     */
    public readonly key!: pulumi.Output<string>;
    /**
     * [LocalizedString](https://docs.commercetools.com/api/types#localizedstring)
     */
    public readonly name!: pulumi.Output<{[key: string]: any}>;
    /**
     * Defines for which [resources](https://docs.commercetools.com/api/projects/custom-fields#customizable-resources) the type
     * is valid
     */
    public readonly resourceTypeIds!: pulumi.Output<string[]>;
    public /*out*/ readonly version!: pulumi.Output<number>;

    /**
     * Create a Type resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: TypeArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: TypeArgs | TypeState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as TypeState | undefined;
            resourceInputs["description"] = state ? state.description : undefined;
            resourceInputs["fields"] = state ? state.fields : undefined;
            resourceInputs["key"] = state ? state.key : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["resourceTypeIds"] = state ? state.resourceTypeIds : undefined;
            resourceInputs["version"] = state ? state.version : undefined;
        } else {
            const args = argsOrState as TypeArgs | undefined;
            if ((!args || args.key === undefined) && !opts.urn) {
                throw new Error("Missing required property 'key'");
            }
            if ((!args || args.name === undefined) && !opts.urn) {
                throw new Error("Missing required property 'name'");
            }
            if ((!args || args.resourceTypeIds === undefined) && !opts.urn) {
                throw new Error("Missing required property 'resourceTypeIds'");
            }
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["fields"] = args ? args.fields : undefined;
            resourceInputs["key"] = args ? args.key : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["resourceTypeIds"] = args ? args.resourceTypeIds : undefined;
            resourceInputs["version"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Type.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Type resources.
 */
export interface TypeState {
    /**
     * [LocalizedString](https://docs.commercetools.com/api/types#localizedstring)
     */
    description?: pulumi.Input<{[key: string]: any}>;
    /**
     * [Field definition](https://docs.commercetools.com/api/projects/types#fielddefinition)
     */
    fields?: pulumi.Input<pulumi.Input<inputs.TypeField>[]>;
    /**
     * Identifier for the type (max. 256 characters)
     */
    key?: pulumi.Input<string>;
    /**
     * [LocalizedString](https://docs.commercetools.com/api/types#localizedstring)
     */
    name?: pulumi.Input<{[key: string]: any}>;
    /**
     * Defines for which [resources](https://docs.commercetools.com/api/projects/custom-fields#customizable-resources) the type
     * is valid
     */
    resourceTypeIds?: pulumi.Input<pulumi.Input<string>[]>;
    version?: pulumi.Input<number>;
}

/**
 * The set of arguments for constructing a Type resource.
 */
export interface TypeArgs {
    /**
     * [LocalizedString](https://docs.commercetools.com/api/types#localizedstring)
     */
    description?: pulumi.Input<{[key: string]: any}>;
    /**
     * [Field definition](https://docs.commercetools.com/api/projects/types#fielddefinition)
     */
    fields?: pulumi.Input<pulumi.Input<inputs.TypeField>[]>;
    /**
     * Identifier for the type (max. 256 characters)
     */
    key: pulumi.Input<string>;
    /**
     * [LocalizedString](https://docs.commercetools.com/api/types#localizedstring)
     */
    name: pulumi.Input<{[key: string]: any}>;
    /**
     * Defines for which [resources](https://docs.commercetools.com/api/projects/custom-fields#customizable-resources) the type
     * is valid
     */
    resourceTypeIds: pulumi.Input<pulumi.Input<string>[]>;
}
