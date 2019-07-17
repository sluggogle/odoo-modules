# -*- coding: utf-8 -*-

from odoo import api, models, fields

# Modifying the model to accept setting a confirmation date manually
# and keep it if set at `action_confirm`
class SaleOrder(models.Model):
    _inherit = 'sale.order'

    confirmation_date = fields.Datetime(readonly=False)

    @api.multi
    def action_confirm(self):
        if self._get_forbidden_state_confirm() & set(self.mapped('state')):
            raise UserError(_(
                'It is not allowed to confirm an order in the following states: %s'
            ) % (', '.join(self._get_forbidden_state_confirm())))

        for order in self.filtered(lambda order: order.partner_id not in order.message_partner_ids):
            order.message_subscribe([order.partner_id.id])
        self.write({
            'state': 'sale',
            'confirmation_date': self.confirmation_date if self.confirmation_date else fields.Datetime.now()
        })
        self._action_confirm()
        if self.env['ir.config_parameter'].sudo().get_param('sale.auto_done_setting'):
            self.action_done()
        return True