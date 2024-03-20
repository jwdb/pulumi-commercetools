// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Commercetools.Inputs
{

    public sealed class CartDiscountValueGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Channel must have the role ProductDistribution. Optional when value type is giftLineItem
        /// </summary>
        [Input("distributionChannelId")]
        public Input<string>? DistributionChannelId { get; set; }

        [Input("monies")]
        private InputList<Inputs.CartDiscountValueMoneyGetArgs>? _monies;

        /// <summary>
        /// Absolute discount specific fields
        /// </summary>
        public InputList<Inputs.CartDiscountValueMoneyGetArgs> Monies
        {
            get => _monies ?? (_monies = new InputList<Inputs.CartDiscountValueMoneyGetArgs>());
            set => _monies = value;
        }

        /// <summary>
        /// Relative discount specific fields
        /// </summary>
        [Input("permyriad")]
        public Input<int>? Permyriad { get; set; }

        /// <summary>
        /// ResourceIdentifier of a Product. Required when value type is giftLineItem
        /// </summary>
        [Input("productId")]
        public Input<string>? ProductId { get; set; }

        /// <summary>
        /// Channel must have the role InventorySupply. Optional when value type is giftLineItem
        /// </summary>
        [Input("supplyChannelId")]
        public Input<string>? SupplyChannelId { get; set; }

        /// <summary>
        /// Currently supports absolute/relative/giftLineItem
        /// </summary>
        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        /// <summary>
        /// ProductVariant of the Product. Required when value type is giftLineItem
        /// </summary>
        [Input("variantId")]
        public Input<int>? VariantId { get; set; }

        public CartDiscountValueGetArgs()
        {
        }
        public static new CartDiscountValueGetArgs Empty => new CartDiscountValueGetArgs();
    }
}
