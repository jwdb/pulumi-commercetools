// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Commercetools.Inputs
{

    public sealed class ProjectSettingsExternalOauthGetArgs : global::Pulumi.ResourceArgs
    {
        [Input("authorizationHeader")]
        public Input<string>? AuthorizationHeader { get; set; }

        [Input("url")]
        private Input<string>? _url;
        public Input<string>? Url
        {
            get => _url;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _url = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        public ProjectSettingsExternalOauthGetArgs()
        {
        }
        public static new ProjectSettingsExternalOauthGetArgs Empty => new ProjectSettingsExternalOauthGetArgs();
    }
}
