# -*- coding: utf-8 -*-

from odoo import _, api, fields, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    custom_ref = fields.Boolean('Réf. manuelle ?', default=False)
