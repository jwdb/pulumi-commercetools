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
    public sealed class StoreProductSelection
    {
        /// <summary>
        /// If true, all Products assigned to this Product Selection are part of the Store's assortment
        /// </summary>
        public readonly bool Active;
        /// <summary>
        /// Resource Identifier of a ProductSelection
        /// </summary>
        public readonly string ProductSelectionId;

        [OutputConstructor]
        private StoreProductSelection(
            bool active,

            string productSelectionId)
        {
            Active = active;
            ProductSelectionId = productSelectionId;
        }
    }
}
