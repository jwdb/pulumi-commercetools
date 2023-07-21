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
    public sealed class SubscriptionDestination
    {
        public readonly string? AccessKey;
        public readonly string? AccessSecret;
        public readonly string? AccountId;
        public readonly string? ConnectionString;
        public readonly string? ProjectId;
        public readonly string? QueueUrl;
        public readonly string? Region;
        public readonly string? Topic;
        public readonly string? TopicArn;
        public readonly string Type;
        public readonly string? Uri;

        [OutputConstructor]
        private SubscriptionDestination(
            string? accessKey,

            string? accessSecret,

            string? accountId,

            string? connectionString,

            string? projectId,

            string? queueUrl,

            string? region,

            string? topic,

            string? topicArn,

            string type,

            string? uri)
        {
            AccessKey = accessKey;
            AccessSecret = accessSecret;
            AccountId = accountId;
            ConnectionString = connectionString;
            ProjectId = projectId;
            QueueUrl = queueUrl;
            Region = region;
            Topic = topic;
            TopicArn = topicArn;
            Type = type;
            Uri = uri;
        }
    }
}
