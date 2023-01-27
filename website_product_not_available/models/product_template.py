# -*- coding: utf-8 -*-
# Copyright Monweblocal 2023

from odoo import _, fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    website_availability = fields.Boolean('Cet article est disponible à la vente', default=True)
    website_not_available_message = fields.Char('Message lorsque l\'article n\'est pas disponible')

    def _can_be_added_to_cart(self):
        return self.sale_ok and self.website_availability

    