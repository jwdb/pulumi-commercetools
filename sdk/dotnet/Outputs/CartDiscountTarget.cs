// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Commercetools.Outputs
{

    [OutputType]
    public sealed class CartDiscountTarget
    {
        public readonly int? DiscountedQuantity;
        public readonly int? MaxOccurrence;
        public readonly string? Predicate;
        public readonly string? SelectionMode;
        public readonly int? TriggerQuantity;
        public readonly string Type;

        [OutputConstructor]
        private CartDiscountTarget(
            int? discountedQuantity,

            int? maxOccurrence,

            string? predicate,

            string? selectionMode,

            int? triggerQuantity,

            string type)
        {
            DiscountedQuantity = discountedQuantity;
            MaxOccurrence = maxOccurrence;
            Predicate = predicate;
            SelectionMode = selectionMode;
            TriggerQuantity = triggerQuantity;
            Type = type;
        }
    }
}
