// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Commercetools.Inputs
{

    public sealed class CategoryAssetSourceDimensionsGetArgs : global::Pulumi.ResourceArgs
    {
        [Input("h", required: true)]
        public Input<int> H { get; set; } = null!;

        [Input("w", required: true)]
        public Input<int> W { get; set; } = null!;

        public CategoryAssetSourceDimensionsGetArgs()
        {
        }
        public static new CategoryAssetSourceDimensionsGetArgs Empty => new CategoryAssetSourceDimensionsGetArgs();
    }
}
