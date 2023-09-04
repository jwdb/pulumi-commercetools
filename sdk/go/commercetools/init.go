// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package commercetools

import (
	"fmt"

	"github.com/blang/semver"
	"github.com/pulumi/pulumi-commercetools/sdk/go/commercetools/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type module struct {
	version semver.Version
}

func (m *module) Version() semver.Version {
	return m.version
}

func (m *module) Construct(ctx *pulumi.Context, name, typ, urn string) (r pulumi.Resource, err error) {
	switch typ {
	case "commercetools:index/apiClient:ApiClient":
		r = &ApiClient{}
	case "commercetools:index/apiExtension:ApiExtension":
		r = &ApiExtension{}
	case "commercetools:index/associateRole:AssociateRole":
		r = &AssociateRole{}
	case "commercetools:index/attributeGroup:AttributeGroup":
		r = &AttributeGroup{}
	case "commercetools:index/cartDiscount:CartDiscount":
		r = &CartDiscount{}
	case "commercetools:index/category:Category":
		r = &Category{}
	case "commercetools:index/channel:Channel":
		r = &Channel{}
	case "commercetools:index/customObject:CustomObject":
		r = &CustomObject{}
	case "commercetools:index/customerGroup:CustomerGroup":
		r = &CustomerGroup{}
	case "commercetools:index/discountCode:DiscountCode":
		r = &DiscountCode{}
	case "commercetools:index/productDiscount:ProductDiscount":
		r = &ProductDiscount{}
	case "commercetools:index/productType:ProductType":
		r = &ProductType{}
	case "commercetools:index/projectSettings:ProjectSettings":
		r = &ProjectSettings{}
	case "commercetools:index/shippingMethod:ShippingMethod":
		r = &ShippingMethod{}
	case "commercetools:index/shippingZone:ShippingZone":
		r = &ShippingZone{}
	case "commercetools:index/shippingZoneRate:ShippingZoneRate":
		r = &ShippingZoneRate{}
	case "commercetools:index/state:State":
		r = &State{}
	case "commercetools:index/stateTransitions:StateTransitions":
		r = &StateTransitions{}
	case "commercetools:index/store:Store":
		r = &Store{}
	case "commercetools:index/subscription:Subscription":
		r = &Subscription{}
	case "commercetools:index/taxCategory:TaxCategory":
		r = &TaxCategory{}
	case "commercetools:index/taxCategoryRate:TaxCategoryRate":
		r = &TaxCategoryRate{}
	case "commercetools:index/type:Type":
		r = &Type{}
	default:
		return nil, fmt.Errorf("unknown resource type: %s", typ)
	}

	err = ctx.RegisterResource(typ, name, nil, r, pulumi.URN_(urn))
	return
}

type pkg struct {
	version semver.Version
}

func (p *pkg) Version() semver.Version {
	return p.version
}

func (p *pkg) ConstructProvider(ctx *pulumi.Context, name, typ, urn string) (pulumi.ProviderResource, error) {
	if typ != "pulumi:providers:commercetools" {
		return nil, fmt.Errorf("unknown provider type: %s", typ)
	}

	r := &Provider{}
	err := ctx.RegisterResource(typ, name, nil, r, pulumi.URN_(urn))
	return r, err
}

func init() {
	version, err := internal.PkgVersion()
	if err != nil {
		version = semver.Version{Major: 1}
	}
	pulumi.RegisterResourceModule(
		"commercetools",
		"index/apiClient",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"commercetools",
		"index/apiExtension",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"commercetools",
		"index/associateRole",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"commercetools",
		"index/attributeGroup",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"commercetools",
		"index/cartDiscount",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"commercetools",
		"index/category",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"commercetools",
		"index/channel",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"commercetools",
		"index/customObject",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"commercetools",
		"index/customerGroup",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"commercetools",
		"index/discountCode",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"commercetools",
		"index/productDiscount",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"commercetools",
		"index/productType",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"commercetools",
		"index/projectSettings",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"commercetools",
		"index/shippingMethod",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"commercetools",
		"index/shippingZone",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"commercetools",
		"index/shippingZoneRate",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"commercetools",
		"index/state",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"commercetools",
		"index/stateTransitions",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"commercetools",
		"index/store",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"commercetools",
		"index/subscription",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"commercetools",
		"index/taxCategory",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"commercetools",
		"index/taxCategoryRate",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"commercetools",
		"index/type",
		&module{version},
	)
	pulumi.RegisterResourcePackage(
		"commercetools",
		&pkg{version},
	)
}
