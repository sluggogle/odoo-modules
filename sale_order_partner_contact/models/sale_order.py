# -*- coding: utf-8 -*-

import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    partner_contact_id = fields.Many2one(
        'res.partner', string='Contact',
        readonly=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
        required=False, track_visibility='always',
        help=_("Personne à charge de la demande chez le client."))

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        if (self.partner_id):
            return {
                'domain': {
                    'partner_contact_id': [
                        '&',
                        ('parent_id', '=', self.partner_id.id),
                        ('type', '=', 'contact')
                    ]
                }
            }
