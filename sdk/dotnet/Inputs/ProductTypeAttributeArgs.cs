// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Commercetools.Inputs
{

    public sealed class ProductTypeAttributeArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Describes how an attribute or a set of attributes should be validated across all variants of a product. See also [Attribute Constraint](https://docs.commercetools.com/api/projects/productTypes#attributeconstraint-enum)
        /// </summary>
        [Input("constraint")]
        public Input<string>? Constraint { get; set; }

        /// <summary>
        /// Provides a visual representation type for this attribute. only relevant for text-based attribute types like TextType and LocalizableTextType
        /// </summary>
        [Input("inputHint")]
        public Input<string>? InputHint { get; set; }

        [Input("inputTip")]
        private InputMap<object>? _inputTip;

        /// <summary>
        /// Additional information about the attribute that aids content managers when setting product details
        /// </summary>
        public InputMap<object> InputTip
        {
            get => _inputTip ?? (_inputTip = new InputMap<object>());
            set => _inputTip = value;
        }

        [Input("label", required: true)]
        private InputMap<object>? _label;

        /// <summary>
        /// A human-readable label for the attribute
        /// </summary>
        public InputMap<object> Label
        {
            get => _label ?? (_label = new InputMap<object>());
            set => _label = value;
        }

        /// <summary>
        /// The unique name of the attribute used in the API. The name must be between two and 256 characters long and can contain the ASCII letters A to Z in lowercase or uppercase, digits, underscores (_) and the hyphen-minus (-).
        /// When using the same name for an attribute in two or more product types all fields of the AttributeDefinition of this attribute need to be the same across the product types, otherwise an AttributeDefinitionAlreadyExists error code will be returned. An exception to this are the values of an enum or lenum type and sets thereof
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        /// <summary>
        /// Whether the attribute is required to have a value
        /// </summary>
        [Input("required")]
        public Input<bool>? Required { get; set; }

        /// <summary>
        /// Whether the attribute's values should generally be activated in product search
        /// </summary>
        [Input("searchable")]
        public Input<bool>? Searchable { get; set; }

        /// <summary>
        /// [AttributeType](https://docs.commercetools.com/api/projects/productTypes#attributetype)
        /// </summary>
        [Input("type", required: true)]
        public Input<Inputs.ProductTypeAttributeTypeArgs> Type { get; set; } = null!;

        public ProductTypeAttributeArgs()
        {
        }
        public static new ProductTypeAttributeArgs Empty => new ProductTypeAttributeArgs();
    }
}
