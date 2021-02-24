odoo.define('website_sale_dynamic_snippet_product_template.s_dynamic_snippet_products_options', function (require) {
    'use strict';

    const oldDynamicSnippetProductsOptions = require('website_sale.s_dynamic_snippet_products_options');
    
    const dynamicSnippetProductsOptions = oldDynamicSnippetProductsOptions.include({

        // Don't remote the filter_opt field in the snippet options
        _computeWidgetVisibility: function (widgetName, params) {
            return this._super.apply(this, arguments);
        },

        // Only fetch product.product or product.template filter (see controller)
        _fetchDynamicFilters: function () {
            return this._rpc({route: '/website_sale_dynamic_snippet_product_template/snippet/options_filters'});
        },
        
        // No need to set the filter_opt field as we can do it manually
        onBuilt: function () {
            this._super.apply(this, arguments);
        },
    });

    return dynamicSnippetProductsOptions;
});
    