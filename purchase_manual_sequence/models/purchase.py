# -*- coding: utf-8 -*-

from odoo import _, fields, models

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    custom_ref = fields.Boolean('Réf. manuelle ?', default=False)
