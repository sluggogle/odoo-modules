# -*- coding: utf-8 -*-

import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)

class SaleOrderAmountText(models.Model):
    _inherit = 'sale.order'

    @api.depends('amount_total')
    def _compute_amount_total_words(self):
        for order in self:
            order.amount_total_words = order.currency_id.amount_to_text(order.amount_total)

    amount_total_words = fields.Char("Total (In Words)", compute="_compute_amount_total_words", store=True)
