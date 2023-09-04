// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Commercetools.Inputs
{

    public sealed class CartDiscountTargetArgs : global::Pulumi.ResourceArgs
    {
        [Input("discountedQuantity")]
        public Input<int>? DiscountedQuantity { get; set; }

        [Input("maxOccurrence")]
        public Input<int>? MaxOccurrence { get; set; }

        [Input("predicate")]
        public Input<string>? Predicate { get; set; }

        [Input("selectionMode")]
        public Input<string>? SelectionMode { get; set; }

        [Input("triggerQuantity")]
        public Input<int>? TriggerQuantity { get; set; }

        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        public CartDiscountTargetArgs()
        {
        }
        public static new CartDiscountTargetArgs Empty => new CartDiscountTargetArgs();
    }
}
