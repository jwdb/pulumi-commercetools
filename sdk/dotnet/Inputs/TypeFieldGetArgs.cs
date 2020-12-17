// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Commercetools.Inputs
{

    public sealed class TypeFieldGetArgs : Pulumi.ResourceArgs
    {
        [Input("inputHint")]
        public Input<string>? InputHint { get; set; }

        [Input("label", required: true)]
        private InputMap<object>? _label;
        public InputMap<object> Label
        {
            get => _label ?? (_label = new InputMap<object>());
            set => _label = value;
        }

        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        [Input("required")]
        public Input<bool>? Required { get; set; }

        [Input("type", required: true)]
        public Input<Inputs.TypeFieldTypeGetArgs> Type { get; set; } = null!;

        public TypeFieldGetArgs()
        {
        }
    }
}