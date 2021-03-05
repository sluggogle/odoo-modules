# -*- coding: utf-8 -*-

from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.http import request

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
