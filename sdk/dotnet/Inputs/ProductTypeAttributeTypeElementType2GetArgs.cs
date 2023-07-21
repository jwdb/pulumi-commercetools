// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Commercetools.Inputs
{

    public sealed class ProductTypeAttributeTypeElementType2GetArgs : global::Pulumi.ResourceArgs
    {
        [Input("localizedValues")]
        private InputList<Inputs.ProductTypeAttributeTypeElementType2LocalizedValueGetArgs>? _localizedValues;
        public InputList<Inputs.ProductTypeAttributeTypeElementType2LocalizedValueGetArgs> LocalizedValues
        {
            get => _localizedValues ?? (_localizedValues = new InputList<Inputs.ProductTypeAttributeTypeElementType2LocalizedValueGetArgs>());
            set => _localizedValues = value;
        }

        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        [Input("referenceTypeId")]
        public Input<string>? ReferenceTypeId { get; set; }

        [Input("typeReference")]
        public Input<string>? TypeReference { get; set; }

        [Input("values")]
        private InputList<Inputs.ProductTypeAttributeTypeElementType2ValueGetArgs>? _values;
        public InputList<Inputs.ProductTypeAttributeTypeElementType2ValueGetArgs> Values
        {
            get => _values ?? (_values = new InputList<Inputs.ProductTypeAttributeTypeElementType2ValueGetArgs>());
            set => _values = value;
        }

        public ProductTypeAttributeTypeElementType2GetArgs()
        {
        }
        public static new ProductTypeAttributeTypeElementType2GetArgs Empty => new ProductTypeAttributeTypeElementType2GetArgs();
    }
}
