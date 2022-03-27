# -*- coding: utf-8 -*-

from odoo import _, fields, models

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    custom_ref = fields.Boolean('Réf. manuelle ?', default=False)
