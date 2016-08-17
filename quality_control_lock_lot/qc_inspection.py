# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.tools.translate import _

import logging
_logger = logging.getLogger(__name__)

######################################
# QcInpection
# - inherite qc.inpection
# - lock lot in creation
# - unlock at the end of the workflow
######################################
#
# TODO
#
# - Find a solution for stock_moves (multiple lots)
#
######################################
class QcInspection(models.Model):
    _inherit = 'qc.inspection'

    @api.one
    @api.depends('object_id')
    def get_lot(self):
        self.lot = False
        if self.object_id:
            if self.object_id._name == 'stock.pack.operation':
                self.lot = self.object_id.lot_id
            elif self.object_id._name == 'stock.move':
                self.lot = self.object_id.lot_ids[:1]
            elif self.object_id._name == 'stock.production.lot':
                self.lot = self.object_id.id

    @api.model
    def create(self, vals):
        new_id = super(QcInspection, self).create(vals)
        new_id.get_lot()
        if new_id.lot and vals.get('state', 'draft') == 'ready':
            _logger.info('QcInspection2: lot = %s', new_id.lot.name)
            new_id.lot.write({'locked': True})
        return new_id

    @api.multi
    def action_todo(self):
        super(QcInspection, self).action_todo()
        self.get_lot()
        if self.lot:
            self.lot.write({'locked': True})

    @api.multi
    def action_confirm(self):
        super(QcInspection, self).action_confirm()
        for inspection in self:
            inspection.get_lot()
            if inspection.lot and inspection.success:
                inspection.lot.write({'locked': False})

    @api.multi
    def action_approve(self):
        super(QcInspection, self).action_approve()
        for inspection in self:
            inspection.get_lot()
            if inspection.lot:
                inspection.lot.write({'locked': False})

    @api.multi
    def action_cancel(self):
        super(QcInspection, self).action_cancel()
        for inspection in self:
            inspection.get_lot()
            if inspection.lot:
                inspection.lot.write({'locked': False})
