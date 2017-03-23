from openerp import models, fields, api
from openerp.addons import decimal_precision as dp
from openerp.report import report_sxw
from openerp.tools.translate import _
import os
import logging

_logger = logging.getLogger(__name__)


#######################################
#
# Parse the new keyword: uom_conversion
#   Args: from_uom_id, old_qty, to_uom_id)
#
# Return the new UOM Qty converted
#
#######################################
class uom_conversion_report_parser(report_sxw.rml_parse):
    
    def __init__(self, cr, uid, name, context):
        super(uom_conversion_report_parser, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
            'uom_conversion': self._uom_conversion,
            #'preview_lot': self._preview_lot,
        })

    def _uom_conversion(self, from_uom_id, qty, to_uom_id):
        uom_obj = self.pool.get('product.uom')
        uom_qty = uom_obj._compute_qty_obj(self.cr, self.uid, from_uom_id, qty, to_uom_id, True, 'HALF-UP')
        _logger.info("\nQTY: %s\nFROM UOM: %s\nTO UOM: %s\nUOM QTY: %s\n", qty, from_uom_id, to_uom_id, uom_qty)
        return uom_qty

#    def _preview_lot(self, product_id):
#        sequence_obj = self.pool.get('ir.sequence')
#        product_lot_id = product_id.categ_id.x_lot_id.id
#        lot = sequence_obj.preview_next_by_id(self.cr, self.uid, product_lot_id)
#        _logger.info("\n\nPROD_ID: %s\nPROD_LOT_ID: %s\nLOT: %s\n\n", product_id, product_lot_id, lot)
#        return lot

#
# Class to use the above parser in a report
#
class report_mrporder(models.AbstractModel):
    _name = 'report.mrp.report_mrporder'
    _inherit = 'report.abstract_report'
    _template = 'mrp.report_mrporder'
    _wrapped_report_class = uom_conversion_report_parser

