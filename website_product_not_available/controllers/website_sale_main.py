# -*- coding: utf-8 -*-

from odoo.addons.website_sale.controllers.main import WebsiteSale

from odoo import http
from odoo.http import request, Response

class CustomWebsiteSale(WebsiteSale):
    def _get_products_recently_viewed(self):
        res = super(CustomWebsiteSale, self)._get_products_recently_viewed()

        key = 'products'

        if len(res.get(key, {})) > 0:
            for product in res['products']:
                # TODO: Do better ?
                tmpl = request.env['product.template'].browse(product['product_template_id'])[0]
                product['product_type'] = tmpl.type
                product['inventory_availability'] = tmpl.inventory_availability
                if (tmpl.website_ribbon_id):
                    product['website_ribbon_id'] = tmpl.website_ribbon_id
                    product['ribbon_class'] = tmpl.website_ribbon_id.html_class
                    product['ribbon_html'] = tmpl.website_ribbon_id.html
        return res

    @http.route(['/shop/cart/update'], type='http', auth="public", methods=['POST'], website=True)
    def cart_update(self, product_id, add_qty=1, set_qty=0, **kw):
        try:
            if product_id:
                product_id = int(product_id)
        except ValueError:
            return Response(status=204)
        product = request.env['product.product'].sudo().browse(product_id)
        if product.type == 'product' and product.inventory_availability == 'not_available':
            return Response(status=204)
        return super().cart_update(product_id, add_qty, set_qty, **kw)

