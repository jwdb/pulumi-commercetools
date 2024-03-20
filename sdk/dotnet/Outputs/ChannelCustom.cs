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
    public sealed class ChannelCustom
    {
        /// <summary>
        /// Custom fields for this resource. Note that the values need to be provided as JSON encoded strings: `my-value = jsonencode({"key": "value"})`
        /// </summary>
        public readonly ImmutableDictionary<string, object>? Fields;
        public readonly string TypeId;

        [OutputConstructor]
        private ChannelCustom(
            ImmutableDictionary<string, object>? fields,

            string typeId)
        {
            Fields = fields;
            TypeId = typeId;
        }
    }
}