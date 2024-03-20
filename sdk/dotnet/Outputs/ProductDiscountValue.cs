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
    public sealed class ProductDiscountValue
    {
        /// <summary>
        /// Absolute discount specific fields
        /// </summary>
        public readonly ImmutableArray<Outputs.ProductDiscountValueMoney> Monies;
        /// <summary>
        /// Relative discount specific fields
        /// </summary>
        public readonly int? Permyriad;
        /// <summary>
        /// Currently supports absolute/relative/external
        /// </summary>
        public readonly string Type;

        [OutputConstructor]
        private ProductDiscountValue(
            ImmutableArray<Outputs.ProductDiscountValueMoney> monies,

            int? permyriad,

            string type)
        {
            Monies = monies;
            Permyriad = permyriad;
            Type = type;
        }
    }
}
