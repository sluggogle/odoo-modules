# -*- coding: utf-8 -*-

import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)

class InvoiceAmountText(models.Model):
    _inherit = 'account.invoice'

    @api.depends('amount_total')
    def _compute_amount_total_words(self):
        for inv in self:
            inv.amount_total_words = inv.currency_id.amount_to_text(inv.amount_total)

    amount_total_words = fields.Char("Total (In Words)", compute="_compute_amount_total_words", store=True)
