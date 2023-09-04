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
        [Input("distributionChannelId")]
        public Input<string>? DistributionChannelId { get; set; }

        [Input("monies")]
        private InputList<Inputs.CartDiscountValueMoneyGetArgs>? _monies;
        public InputList<Inputs.CartDiscountValueMoneyGetArgs> Monies
        {
            get => _monies ?? (_monies = new InputList<Inputs.CartDiscountValueMoneyGetArgs>());
            set => _monies = value;
        }

        [Input("permyriad")]
        public Input<int>? Permyriad { get; set; }

        [Input("productId")]
        public Input<string>? ProductId { get; set; }

        [Input("supplyChannelId")]
        public Input<string>? SupplyChannelId { get; set; }

        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        [Input("variantId")]
        public Input<int>? VariantId { get; set; }

        public CartDiscountValueGetArgs()
        {
        }
        public static new CartDiscountValueGetArgs Empty => new CartDiscountValueGetArgs();
    }
}
