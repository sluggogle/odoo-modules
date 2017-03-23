# coding: utf-8
from openerp.osv import osv, fields


class MrpProduction(osv.Model):
    _inherit = 'mrp.production'

    def _preview_lot(self, cr, uid, ids, name, args, context=None):
        sequence_obj = self.pool.get('ir.sequence')
        res = dict.fromkeys(ids)
        for element in self.browse(cr, uid, ids, context=context):
            if element.state in ('confirmed', 'ready', 'in_production'):
                product_lot_id = element.product_id.categ_id.x_lot_id.id
                lot = sequence_obj.preview_next_by_id(cr, uid, product_lot_id)
                res[element.id] = lot
        return res

    _columns = {
        'temp_lot': fields.function(_preview_lot, method=True, type="char", string="Potential Lot"),
    }
