# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.tools.translate import _

import logging
_logger = logging.getLogger(__name__)

########################################################
## Add the lot_id field to product.category            #
########################################################
class ProductCategory(models.Model):
    _inherit = 'product.category'
    x_lot_id = fields.Many2one(comodel_name='ir.sequence',
                                    string='Product Lot',
                                    help=_("This sequence will be use for products' lot numbers"))

