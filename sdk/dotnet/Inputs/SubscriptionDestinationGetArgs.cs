// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Commercetools.Inputs
{

    public sealed class SubscriptionDestinationGetArgs : global::Pulumi.ResourceArgs
    {
        [Input("accessKey")]
        private Input<string>? _accessKey;

        /// <summary>
        /// The access key of the SQS queue, SNS topic or EventBridge topic
        /// </summary>
        public Input<string>? AccessKey
        {
            get => _accessKey;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _accessKey = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        [Input("accessSecret")]
        private Input<string>? _accessSecret;

        /// <summary>
        /// The access secret of the SQS queue, SNS topic or EventBridge topic
        /// </summary>
        public Input<string>? AccessSecret
        {
            get => _accessSecret;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _accessSecret = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        /// <summary>
        /// The AWS account ID of the SNS topic or EventBridge topic
        /// </summary>
        [Input("accountId")]
        public Input<string>? AccountId { get; set; }

        /// <summary>
        /// The acks value of the Confluent Cloud topic
        /// </summary>
        [Input("acks")]
        public Input<string>? Acks { get; set; }

        /// <summary>
        /// The API key of the Confluent Cloud topic
        /// </summary>
        [Input("apiKey")]
        public Input<string>? ApiKey { get; set; }

        /// <summary>
        /// The API secret of the Confluent Cloud topic
        /// </summary>
        [Input("apiSecret")]
        public Input<string>? ApiSecret { get; set; }

        /// <summary>
        /// The bootstrap server of the Confluent Cloud topic
        /// </summary>
        [Input("bootstrapServer")]
        public Input<string>? BootstrapServer { get; set; }

        /// <summary>
        /// The connection string of the Azure Service Bus
        /// </summary>
        [Input("connectionString")]
        public Input<string>? ConnectionString { get; set; }

        /// <summary>
        /// The key of the Confluent Cloud topic
        /// </summary>
        [Input("key")]
        public Input<string>? Key { get; set; }

        /// <summary>
        /// The project ID of the Google Cloud Pub/Sub
        /// </summary>
        [Input("projectId")]
        public Input<string>? ProjectId { get; set; }

        /// <summary>
        /// The URL of the SQS queue
        /// </summary>
        [Input("queueUrl")]
        public Input<string>? QueueUrl { get; set; }

        /// <summary>
        /// The region of the SQS queue, SNS topic or EventBridge topic
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// The topic of the Google Cloud Pub/Sub or Confluent Cloud topic
        /// </summary>
        [Input("topic")]
        public Input<string>? Topic { get; set; }

        /// <summary>
        /// The ARN of the SNS topic
        /// </summary>
        [Input("topicArn")]
        public Input<string>? TopicArn { get; set; }

        /// <summary>
        /// The type of the destination. See [Destination](https://docs.commercetools.com/api/projects/subscriptions#destination) for more information
        /// </summary>
        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        /// <summary>
        /// The URI of the EventGrid topic
        /// </summary>
        [Input("uri")]
        public Input<string>? Uri { get; set; }

        public SubscriptionDestinationGetArgs()
        {
        }
        public static new SubscriptionDestinationGetArgs Empty => new SubscriptionDestinationGetArgs();
    }
}
