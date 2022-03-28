# -*- coding: utf-8 -*-

from odoo import _, fields, models

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    date_approve = fields.Datetime(
        'Confirmation Date',
        readonly=1,
        states={'purchase': [('readonly', False)]},
        index=True,
        copy=False
    )
