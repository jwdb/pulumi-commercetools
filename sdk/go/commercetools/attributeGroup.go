// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package commercetools

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-commercetools/sdk/go/commercetools/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type AttributeGroup struct {
	pulumi.CustomResourceState

	// Attributes with unique values.
	Attributes AttributeGroupAttributeArrayOutput `pulumi:"attributes"`
	// Description of the State as localized string.
	Description pulumi.StringMapOutput `pulumi:"description"`
	// User-defined unique identifier of the AttributeGroup.
	Key pulumi.StringPtrOutput `pulumi:"key"`
	// Name of the State as localized string.
	Name pulumi.StringMapOutput `pulumi:"name"`
	// Current version of the AttributeGroup.
	Version pulumi.IntOutput `pulumi:"version"`
}

// NewAttributeGroup registers a new resource with the given unique name, arguments, and options.
func NewAttributeGroup(ctx *pulumi.Context,
	name string, args *AttributeGroupArgs, opts ...pulumi.ResourceOption) (*AttributeGroup, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Name == nil {
		return nil, errors.New("invalid value for required argument 'Name'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource AttributeGroup
	err := ctx.RegisterResource("commercetools:index/attributeGroup:AttributeGroup", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetAttributeGroup gets an existing AttributeGroup resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetAttributeGroup(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *AttributeGroupState, opts ...pulumi.ResourceOption) (*AttributeGroup, error) {
	var resource AttributeGroup
	err := ctx.ReadResource("commercetools:index/attributeGroup:AttributeGroup", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering AttributeGroup resources.
type attributeGroupState struct {
	// Attributes with unique values.
	Attributes []AttributeGroupAttribute `pulumi:"attributes"`
	// Description of the State as localized string.
	Description map[string]string `pulumi:"description"`
	// User-defined unique identifier of the AttributeGroup.
	Key *string `pulumi:"key"`
	// Name of the State as localized string.
	Name map[string]string `pulumi:"name"`
	// Current version of the AttributeGroup.
	Version *int `pulumi:"version"`
}

type AttributeGroupState struct {
	// Attributes with unique values.
	Attributes AttributeGroupAttributeArrayInput
	// Description of the State as localized string.
	Description pulumi.StringMapInput
	// User-defined unique identifier of the AttributeGroup.
	Key pulumi.StringPtrInput
	// Name of the State as localized string.
	Name pulumi.StringMapInput
	// Current version of the AttributeGroup.
	Version pulumi.IntPtrInput
}

func (AttributeGroupState) ElementType() reflect.Type {
	return reflect.TypeOf((*attributeGroupState)(nil)).Elem()
}

type attributeGroupArgs struct {
	// Attributes with unique values.
	Attributes []AttributeGroupAttribute `pulumi:"attributes"`
	// Description of the State as localized string.
	Description map[string]string `pulumi:"description"`
	// User-defined unique identifier of the AttributeGroup.
	Key *string `pulumi:"key"`
	// Name of the State as localized string.
	Name map[string]string `pulumi:"name"`
}

// The set of arguments for constructing a AttributeGroup resource.
type AttributeGroupArgs struct {
	// Attributes with unique values.
	Attributes AttributeGroupAttributeArrayInput
	// Description of the State as localized string.
	Description pulumi.StringMapInput
	// User-defined unique identifier of the AttributeGroup.
	Key pulumi.StringPtrInput
	// Name of the State as localized string.
	Name pulumi.StringMapInput
}

func (AttributeGroupArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*attributeGroupArgs)(nil)).Elem()
}

type AttributeGroupInput interface {
	pulumi.Input

	ToAttributeGroupOutput() AttributeGroupOutput
	ToAttributeGroupOutputWithContext(ctx context.Context) AttributeGroupOutput
}

func (*AttributeGroup) ElementType() reflect.Type {
	return reflect.TypeOf((**AttributeGroup)(nil)).Elem()
}

func (i *AttributeGroup) ToAttributeGroupOutput() AttributeGroupOutput {
	return i.ToAttributeGroupOutputWithContext(context.Background())
}

func (i *AttributeGroup) ToAttributeGroupOutputWithContext(ctx context.Context) AttributeGroupOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AttributeGroupOutput)
}

// AttributeGroupArrayInput is an input type that accepts AttributeGroupArray and AttributeGroupArrayOutput values.
// You can construct a concrete instance of `AttributeGroupArrayInput` via:
//
//	AttributeGroupArray{ AttributeGroupArgs{...} }
type AttributeGroupArrayInput interface {
	pulumi.Input

	ToAttributeGroupArrayOutput() AttributeGroupArrayOutput
	ToAttributeGroupArrayOutputWithContext(context.Context) AttributeGroupArrayOutput
}

type AttributeGroupArray []AttributeGroupInput

func (AttributeGroupArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*AttributeGroup)(nil)).Elem()
}

func (i AttributeGroupArray) ToAttributeGroupArrayOutput() AttributeGroupArrayOutput {
	return i.ToAttributeGroupArrayOutputWithContext(context.Background())
}

func (i AttributeGroupArray) ToAttributeGroupArrayOutputWithContext(ctx context.Context) AttributeGroupArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AttributeGroupArrayOutput)
}

// AttributeGroupMapInput is an input type that accepts AttributeGroupMap and AttributeGroupMapOutput values.
// You can construct a concrete instance of `AttributeGroupMapInput` via:
//
//	AttributeGroupMap{ "key": AttributeGroupArgs{...} }
type AttributeGroupMapInput interface {
	pulumi.Input

	ToAttributeGroupMapOutput() AttributeGroupMapOutput
	ToAttributeGroupMapOutputWithContext(context.Context) AttributeGroupMapOutput
}

type AttributeGroupMap map[string]AttributeGroupInput

func (AttributeGroupMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*AttributeGroup)(nil)).Elem()
}

func (i AttributeGroupMap) ToAttributeGroupMapOutput() AttributeGroupMapOutput {
	return i.ToAttributeGroupMapOutputWithContext(context.Background())
}

func (i AttributeGroupMap) ToAttributeGroupMapOutputWithContext(ctx context.Context) AttributeGroupMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AttributeGroupMapOutput)
}

type AttributeGroupOutput struct{ *pulumi.OutputState }

func (AttributeGroupOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**AttributeGroup)(nil)).Elem()
}

func (o AttributeGroupOutput) ToAttributeGroupOutput() AttributeGroupOutput {
	return o
}

func (o AttributeGroupOutput) ToAttributeGroupOutputWithContext(ctx context.Context) AttributeGroupOutput {
	return o
}

// Attributes with unique values.
func (o AttributeGroupOutput) Attributes() AttributeGroupAttributeArrayOutput {
	return o.ApplyT(func(v *AttributeGroup) AttributeGroupAttributeArrayOutput { return v.Attributes }).(AttributeGroupAttributeArrayOutput)
}

// Description of the State as localized string.
func (o AttributeGroupOutput) Description() pulumi.StringMapOutput {
	return o.ApplyT(func(v *AttributeGroup) pulumi.StringMapOutput { return v.Description }).(pulumi.StringMapOutput)
}

// User-defined unique identifier of the AttributeGroup.
func (o AttributeGroupOutput) Key() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *AttributeGroup) pulumi.StringPtrOutput { return v.Key }).(pulumi.StringPtrOutput)
}

// Name of the State as localized string.
func (o AttributeGroupOutput) Name() pulumi.StringMapOutput {
	return o.ApplyT(func(v *AttributeGroup) pulumi.StringMapOutput { return v.Name }).(pulumi.StringMapOutput)
}

// Current version of the AttributeGroup.
func (o AttributeGroupOutput) Version() pulumi.IntOutput {
	return o.ApplyT(func(v *AttributeGroup) pulumi.IntOutput { return v.Version }).(pulumi.IntOutput)
}

type AttributeGroupArrayOutput struct{ *pulumi.OutputState }

func (AttributeGroupArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*AttributeGroup)(nil)).Elem()
}

func (o AttributeGroupArrayOutput) ToAttributeGroupArrayOutput() AttributeGroupArrayOutput {
	return o
}

func (o AttributeGroupArrayOutput) ToAttributeGroupArrayOutputWithContext(ctx context.Context) AttributeGroupArrayOutput {
	return o
}

func (o AttributeGroupArrayOutput) Index(i pulumi.IntInput) AttributeGroupOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *AttributeGroup {
		return vs[0].([]*AttributeGroup)[vs[1].(int)]
	}).(AttributeGroupOutput)
}

type AttributeGroupMapOutput struct{ *pulumi.OutputState }

func (AttributeGroupMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*AttributeGroup)(nil)).Elem()
}

func (o AttributeGroupMapOutput) ToAttributeGroupMapOutput() AttributeGroupMapOutput {
	return o
}

func (o AttributeGroupMapOutput) ToAttributeGroupMapOutputWithContext(ctx context.Context) AttributeGroupMapOutput {
	return o
}

func (o AttributeGroupMapOutput) MapIndex(k pulumi.StringInput) AttributeGroupOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *AttributeGroup {
		return vs[0].(map[string]*AttributeGroup)[vs[1].(string)]
	}).(AttributeGroupOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*AttributeGroupInput)(nil)).Elem(), &AttributeGroup{})
	pulumi.RegisterInputType(reflect.TypeOf((*AttributeGroupArrayInput)(nil)).Elem(), AttributeGroupArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*AttributeGroupMapInput)(nil)).Elem(), AttributeGroupMap{})
	pulumi.RegisterOutputType(AttributeGroupOutput{})
	pulumi.RegisterOutputType(AttributeGroupArrayOutput{})
	pulumi.RegisterOutputType(AttributeGroupMapOutput{})
}
