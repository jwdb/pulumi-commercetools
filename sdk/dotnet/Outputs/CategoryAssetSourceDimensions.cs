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
    public sealed class CategoryAssetSourceDimensions
    {
        /// <summary>
        /// The height of the asset source
        /// </summary>
        public readonly int H;
        /// <summary>
        /// The width of the asset source
        /// </summary>
        public readonly int W;

        [OutputConstructor]
        private CategoryAssetSourceDimensions(
            int h,

            int w)
        {
            H = h;
            W = w;
        }
    }
}
