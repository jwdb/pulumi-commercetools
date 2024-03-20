// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Commercetools.Inputs
{

    public sealed class SubscriptionMessageGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// [Resource Type ID](https://docs.commercetools.com/api/projects/subscriptions#changesubscription)
        /// </summary>
        [Input("resourceTypeId", required: true)]
        public Input<string> ResourceTypeId { get; set; } = null!;

        [Input("types", required: true)]
        private InputList<string>? _types;

        /// <summary>
        /// types must contain valid message types for this resource, for example for resource type product the message type ProductPublished is valid. If no types of messages are given, the subscription is valid for all messages of this resource
        /// </summary>
        public InputList<string> Types
        {
            get => _types ?? (_types = new InputList<string>());
            set => _types = value;
        }

        public SubscriptionMessageGetArgs()
        {
        }
        public static new SubscriptionMessageGetArgs Empty => new SubscriptionMessageGetArgs();
    }
}
