# -*- coding: utf-8 -*-

from odoo import fields, models

class ResPartner(models.Model):
    _inherit= 'res.partner'

    l10n_ma_ice = fields.Char(string="ICE", size=15)

    @api.multi
    def copy(self, default=None):
        self.ensure_one()
        default = dict(default or {}, l10n_ma_ice="")
        return super(ResPartner, self.copy(default))

