odoo.define('website_sale_better_dynamic_products_snippet.s_dynamic_snippet_products_options', function (require) {
    'use strict';

    const oldDynamicSnippetProductsOptions = require('website_sale.s_dynamic_snippet_products_options');
    
    const dynamicSnippetProductsOptions = oldDynamicSnippetProductsOptions.include({

        // Don't remote the filter_opt field in the snippet options
        _computeWidgetVisibility: function (widgetName, params) {
            if (widgetName === 'filter_opt') {
                return true;
            }
            return this._super.apply(this, arguments);
        },

        // Only fetch product.product or product.template filter (see controller)
        _fetchDynamicFilters: function () {
            return this._rpc({route: '/website_sale_better_dynamic_products_snippet/snippet/options_filters'});
        },
        
        // No need to set the filter_opt field as we can do it manually
        onBuilt: function () {
            this._super.apply(this, arguments);
        },
    });

    return dynamicSnippetProductsOptions;
});
    