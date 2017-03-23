# -*- coding: utf-8 -*-
from openerp import models, fields, api
import logging
_logger = logging.getLogger(__name__)

import datetime

class automatic_lock(models.Model):
    _name='automatic.lock'

    @api.model
    def detect_and_lock(self):
        now = datetime.datetime.now()
        lots = self.env['stock.production.lot'].search([('life_date', '<', fields.Date.to_string(now))])
        _logger.info('Number of lots Expired: %s', lots)
        for elem in lots:
            elem.button_lock()
