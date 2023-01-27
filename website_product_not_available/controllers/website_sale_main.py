# -*- coding: utf-8 -*-

from odoo.addons.website_sale.controllers.main import WebsiteSale

from odoo import http
from odoo.http import request, Response

class CustomWebsiteSale(WebsiteSale):

    @http.route(['/shop/cart/update'], type='http', auth="public", methods=['POST'], website=True)
    def cart_update(self, product_id, add_qty=1, set_qty=0, **kw):
        try:
            if product_id:
                product_id = int(product_id)
        except ValueError:
            return Response(status=204)
        product = request.env['product.product'].sudo().browse(product_id)
        if not product.website_availability:
            return Response(status=204)
        return super().cart_update(product_id, add_qty, set_qty, **kw)

    @http.route(['/shop/cart/update_json'], type='json', auth="public", methods=['POST'], website=True, csrf=False)
    def cart_update_json(self, product_id, line_id=None, add_qty=None, set_qty=None, display=True, **kw):
        try:
            if product_id:
                product_id = int(product_id)
        except ValueError:
            return Response(status=204)
        product = request.env['product.product'].sudo().browse(product_id)
        if not product.website_availability:
            return Response(status=204)
        return super().cart_update_json(product_id, line_id, add_qty, set_qty, display, **kw)
