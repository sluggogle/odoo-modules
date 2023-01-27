# -*- coding: utf-8 -*-
# Copyright Monweblocal 2020

from odoo import _, fields, models

class ResCountry(models.Model):
    _inherit = 'res.country'

    is_available_ecommerce = fields.Boolean(default=False)

    def get_website_sale_countries(self, mode='billing'):
        res = super(ResCountry, self).get_website_sale_countries(mode=mode)
        res = res.filtered('is_available_ecommerce')
        return res
    