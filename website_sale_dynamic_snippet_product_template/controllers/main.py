# -*- coding: utf-8 -*-
# Copyright Monweblocal 2020

from odoo import http, _
from odoo.http import request
from odoo.osv import expression

class WebsiteSaleProductFilter(http.Controller):

    # --------------------------------------------------------------------------
    # Website Snippet Filters
    # --------------------------------------------------------------------------

    @http.route('/website_sale_dynamic_snippet_product_template/snippet/options_filters', type='json', auth='user', website=True)
    def get_dynamic_snippet_filters(self):
        domain = expression.AND([
            request.website.website_domain(),
            [
                '|', '|',
                ('filter_id.model_id', '=', 'product.product'), ('action_server_id.model_id.model', '=', 'product.product'),
                '|',
                ('filter_id.model_id', '=', 'product.template'), ('action_server_id.model_id.model', '=', 'product.template')
            ]
        ])

        filters = request.env['website.snippet.filter'].sudo().search_read(
            domain, ['id', 'name', 'limit']
        )
        return filters
