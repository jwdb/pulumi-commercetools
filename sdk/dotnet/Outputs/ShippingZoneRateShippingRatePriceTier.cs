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
    public sealed class ShippingZoneRateShippingRatePriceTier
    {
        public readonly int? MinimumCentAmount;
        public readonly Outputs.ShippingZoneRateShippingRatePriceTierPrice? Price;
        public readonly Outputs.ShippingZoneRateShippingRatePriceTierPriceFunction? PriceFunction;
        public readonly int? Score;
        public readonly string Type;
        public readonly string? Value;

        [OutputConstructor]
        private ShippingZoneRateShippingRatePriceTier(
            int? minimumCentAmount,

            Outputs.ShippingZoneRateShippingRatePriceTierPrice? price,

            Outputs.ShippingZoneRateShippingRatePriceTierPriceFunction? priceFunction,

            int? score,

            string type,

            string? value)
        {
            MinimumCentAmount = minimumCentAmount;
            Price = price;
            PriceFunction = priceFunction;
            Score = score;
            Type = type;
            Value = value;
        }
    }
}
