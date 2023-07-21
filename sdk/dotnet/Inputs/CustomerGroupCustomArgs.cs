// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Commercetools.Inputs
{

    public sealed class CustomerGroupCustomArgs : global::Pulumi.ResourceArgs
    {
        [Input("fields")]
        private InputMap<object>? _fields;
        public InputMap<object> Fields
        {
            get => _fields ?? (_fields = new InputMap<object>());
            set => _fields = value;
        }

        [Input("typeId", required: true)]
        public Input<string> TypeId { get; set; } = null!;

        public CustomerGroupCustomArgs()
        {
        }
        public static new CustomerGroupCustomArgs Empty => new CustomerGroupCustomArgs();
    }
}
