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
    public sealed class TypeFieldTypeValue
    {
        public readonly string Key;
        public readonly string Label;

        [OutputConstructor]
        private TypeFieldTypeValue(
            string key,

            string label)
        {
            Key = key;
            Label = label;
        }
    }
}