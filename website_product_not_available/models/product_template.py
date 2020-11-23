# -*- coding: utf-8 -*-
# Copyright Monweblocal 2020

from odoo import _, api, fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    inventory_availability = fields.Selection(selection_add=[('not_available', 'The product is not available for sale')])
    