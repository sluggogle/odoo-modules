# -*- coding: utf-8 -*-

from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.http import request

class CustomWebsiteSale(WebsiteSale):
    def _get_products_recently_viewed(self):
        res = super(CustomWebsiteSale, self)._get_products_recently_viewed()
        if len(res['products']) > 0:
            for product in res['products']:
                # TODO: Do better ?
                tmpl = request.env['product.template'].browse(product['product_template_id'])[0]
                product['product_type'] = tmpl.type
                product['inventory_availability'] = tmpl.inventory_availability
        return res