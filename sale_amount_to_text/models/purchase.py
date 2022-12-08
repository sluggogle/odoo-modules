# -*- coding: utf-8 -*-

from odoo import _, api, fields, models

class PurchaseOrderAmountText(models.Model):
    _inherit = 'purchase.order'

    @api.depends('amount_total')
    def _compute_amount_total_words(self):
        for order in self:
            order.amount_total_words = order.currency_id.amount_to_text(order.amount_total)

    amount_total_words = fields.Char("Total (In Words)", compute="_compute_amount_total_words", store=True)
