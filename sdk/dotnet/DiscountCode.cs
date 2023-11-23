// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Commercetools
{
    [CommercetoolsResourceType("commercetools:index/discountCode:DiscountCode")]
    public partial class DiscountCode : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The referenced matching cart discounts can be applied to the cart once the DiscountCode is added
        /// </summary>
        [Output("cartDiscounts")]
        public Output<ImmutableArray<string>> CartDiscounts { get; private set; } = null!;

        /// <summary>
        /// Unique identifier of this discount code. This value is added to the cart to enable the related cart discounts in the
        /// cart
        /// </summary>
        [Output("code")]
        public Output<string> Code { get; private set; } = null!;

        [Output("custom")]
        public Output<Outputs.DiscountCodeCustom?> Custom { get; private set; } = null!;

        /// <summary>
        /// [LocalizedString](https://docs.commercetools.com/api/types#localizedstring)
        /// </summary>
        [Output("description")]
        public Output<ImmutableDictionary<string, object>?> Description { get; private set; } = null!;

        /// <summary>
        /// The groups to which this discount code belong
        /// </summary>
        [Output("groups")]
        public Output<ImmutableArray<string>> Groups { get; private set; } = null!;

        [Output("isActive")]
        public Output<bool?> IsActive { get; private set; } = null!;

        /// <summary>
        /// The discount code can only be applied the specified times overallNote that due to an engine constraint 0 cannot be set
        /// for this field, so possible values are either larger than 0 or not set
        /// </summary>
        [Output("maxApplications")]
        public Output<int?> MaxApplications { get; private set; } = null!;

        /// <summary>
        /// The discount code can only be applied the specified times per customer. Note that due to an engine constraint 0 cannot
        /// be set for this field, so possible values are either larger than 0 or not set
        /// </summary>
        [Output("maxApplicationsPerCustomer")]
        public Output<int?> MaxApplicationsPerCustomer { get; private set; } = null!;

        /// <summary>
        /// [LocalizedString](https://docs.commercetools.com/api/types#localizedstring)
        /// </summary>
        [Output("name")]
        public Output<ImmutableDictionary<string, object>> Name { get; private set; } = null!;

        /// <summary>
        /// [Cart Predicate](https://docs.commercetools.com/api/projects/predicates#cart-predicates)
        /// </summary>
        [Output("predicate")]
        public Output<string?> Predicate { get; private set; } = null!;

        /// <summary>
        /// The time from which the discount can be applied on a cart. Before that time the code is invalid
        /// </summary>
        [Output("validFrom")]
        public Output<string?> ValidFrom { get; private set; } = null!;

        /// <summary>
        /// The time until the discount can be applied on a cart. After that time the code is invalid
        /// </summary>
        [Output("validUntil")]
        public Output<string?> ValidUntil { get; private set; } = null!;

        [Output("version")]
        public Output<int> Version { get; private set; } = null!;


        /// <summary>
        /// Create a DiscountCode resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public DiscountCode(string name, DiscountCodeArgs args, CustomResourceOptions? options = null)
            : base("commercetools:index/discountCode:DiscountCode", name, args ?? new DiscountCodeArgs(), MakeResourceOptions(options, ""))
        {
        }

        private DiscountCode(string name, Input<string> id, DiscountCodeState? state = null, CustomResourceOptions? options = null)
            : base("commercetools:index/discountCode:DiscountCode", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing DiscountCode resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static DiscountCode Get(string name, Input<string> id, DiscountCodeState? state = null, CustomResourceOptions? options = null)
        {
            return new DiscountCode(name, id, state, options);
        }
    }

    public sealed class DiscountCodeArgs : global::Pulumi.ResourceArgs
    {
        [Input("cartDiscounts", required: true)]
        private InputList<string>? _cartDiscounts;

        /// <summary>
        /// The referenced matching cart discounts can be applied to the cart once the DiscountCode is added
        /// </summary>
        public InputList<string> CartDiscounts
        {
            get => _cartDiscounts ?? (_cartDiscounts = new InputList<string>());
            set => _cartDiscounts = value;
        }

        /// <summary>
        /// Unique identifier of this discount code. This value is added to the cart to enable the related cart discounts in the
        /// cart
        /// </summary>
        [Input("code", required: true)]
        public Input<string> Code { get; set; } = null!;

        [Input("custom")]
        public Input<Inputs.DiscountCodeCustomArgs>? Custom { get; set; }

        [Input("description")]
        private InputMap<object>? _description;

        /// <summary>
        /// [LocalizedString](https://docs.commercetools.com/api/types#localizedstring)
        /// </summary>
        public InputMap<object> Description
        {
            get => _description ?? (_description = new InputMap<object>());
            set => _description = value;
        }

        [Input("groups")]
        private InputList<string>? _groups;

        /// <summary>
        /// The groups to which this discount code belong
        /// </summary>
        public InputList<string> Groups
        {
            get => _groups ?? (_groups = new InputList<string>());
            set => _groups = value;
        }

        [Input("isActive")]
        public Input<bool>? IsActive { get; set; }

        /// <summary>
        /// The discount code can only be applied the specified times overallNote that due to an engine constraint 0 cannot be set
        /// for this field, so possible values are either larger than 0 or not set
        /// </summary>
        [Input("maxApplications")]
        public Input<int>? MaxApplications { get; set; }

        /// <summary>
        /// The discount code can only be applied the specified times per customer. Note that due to an engine constraint 0 cannot
        /// be set for this field, so possible values are either larger than 0 or not set
        /// </summary>
        [Input("maxApplicationsPerCustomer")]
        public Input<int>? MaxApplicationsPerCustomer { get; set; }

        [Input("name")]
        private InputMap<object>? _name;

        /// <summary>
        /// [LocalizedString](https://docs.commercetools.com/api/types#localizedstring)
        /// </summary>
        public InputMap<object> Name
        {
            get => _name ?? (_name = new InputMap<object>());
            set => _name = value;
        }

        /// <summary>
        /// [Cart Predicate](https://docs.commercetools.com/api/projects/predicates#cart-predicates)
        /// </summary>
        [Input("predicate")]
        public Input<string>? Predicate { get; set; }

        /// <summary>
        /// The time from which the discount can be applied on a cart. Before that time the code is invalid
        /// </summary>
        [Input("validFrom")]
        public Input<string>? ValidFrom { get; set; }

        /// <summary>
        /// The time until the discount can be applied on a cart. After that time the code is invalid
        /// </summary>
        [Input("validUntil")]
        public Input<string>? ValidUntil { get; set; }

        public DiscountCodeArgs()
        {
        }
        public static new DiscountCodeArgs Empty => new DiscountCodeArgs();
    }

    public sealed class DiscountCodeState : global::Pulumi.ResourceArgs
    {
        [Input("cartDiscounts")]
        private InputList<string>? _cartDiscounts;

        /// <summary>
        /// The referenced matching cart discounts can be applied to the cart once the DiscountCode is added
        /// </summary>
        public InputList<string> CartDiscounts
        {
            get => _cartDiscounts ?? (_cartDiscounts = new InputList<string>());
            set => _cartDiscounts = value;
        }

        /// <summary>
        /// Unique identifier of this discount code. This value is added to the cart to enable the related cart discounts in the
        /// cart
        /// </summary>
        [Input("code")]
        public Input<string>? Code { get; set; }

        [Input("custom")]
        public Input<Inputs.DiscountCodeCustomGetArgs>? Custom { get; set; }

        [Input("description")]
        private InputMap<object>? _description;

        /// <summary>
        /// [LocalizedString](https://docs.commercetools.com/api/types#localizedstring)
        /// </summary>
        public InputMap<object> Description
        {
            get => _description ?? (_description = new InputMap<object>());
            set => _description = value;
        }

        [Input("groups")]
        private InputList<string>? _groups;

        /// <summary>
        /// The groups to which this discount code belong
        /// </summary>
        public InputList<string> Groups
        {
            get => _groups ?? (_groups = new InputList<string>());
            set => _groups = value;
        }

        [Input("isActive")]
        public Input<bool>? IsActive { get; set; }

        /// <summary>
        /// The discount code can only be applied the specified times overallNote that due to an engine constraint 0 cannot be set
        /// for this field, so possible values are either larger than 0 or not set
        /// </summary>
        [Input("maxApplications")]
        public Input<int>? MaxApplications { get; set; }

        /// <summary>
        /// The discount code can only be applied the specified times per customer. Note that due to an engine constraint 0 cannot
        /// be set for this field, so possible values are either larger than 0 or not set
        /// </summary>
        [Input("maxApplicationsPerCustomer")]
        public Input<int>? MaxApplicationsPerCustomer { get; set; }

        [Input("name")]
        private InputMap<object>? _name;

        /// <summary>
        /// [LocalizedString](https://docs.commercetools.com/api/types#localizedstring)
        /// </summary>
        public InputMap<object> Name
        {
            get => _name ?? (_name = new InputMap<object>());
            set => _name = value;
        }

        /// <summary>
        /// [Cart Predicate](https://docs.commercetools.com/api/projects/predicates#cart-predicates)
        /// </summary>
        [Input("predicate")]
        public Input<string>? Predicate { get; set; }

        /// <summary>
        /// The time from which the discount can be applied on a cart. Before that time the code is invalid
        /// </summary>
        [Input("validFrom")]
        public Input<string>? ValidFrom { get; set; }

        /// <summary>
        /// The time until the discount can be applied on a cart. After that time the code is invalid
        /// </summary>
        [Input("validUntil")]
        public Input<string>? ValidUntil { get; set; }

        [Input("version")]
        public Input<int>? Version { get; set; }

        public DiscountCodeState()
        {
        }
        public static new DiscountCodeState Empty => new DiscountCodeState();
    }
}
