# coding: utf-8
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#
#    Copyright (c) 2010 Vauxoo - http://www.vauxoo.com/
#    All Rights Reserved.
#    info Vauxoo (info@vauxoo.com)
############################################################################
#    Coded by: Luis Torres (luis_t@vauxoo.com)
############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp.osv import osv, fields


class MrpProduction(osv.Model):
    _inherit = 'mrp.production'

    def _product_produced(self, cr, uid, ids, field, args, context=None):
        stock_obj = self.pool.get('stock.move')
        res = {}
        for id in ids:
            total = 0.0
            prod_id = self.browse(cr, uid, id)
            loc_dest_prod = prod_id.location_dest_id and\
                prod_id.location_dest_id.id or ''
            product_prod = prod_id.product_id and\
                prod_id.product_id.id or ''
            if prod_id.move_created_ids2:
                for move in prod_id.move_created_ids2:
                    move_id = stock_obj.browse(cr, uid, move.id)
                    product_move = move_id.product_id and\
                        move_id.product_id.id or ''
                    loc_dest_move = move_id.location_dest_id and\
                        move_id.location_dest_id.id or ''
                    state_move = move_id.state or ''
                    if loc_dest_move == loc_dest_prod and\
                        state_move == 'done' and\
                            product_prod == product_move:
                        total_move = move_id.product_qty or 0.0
                        total = total + total_move
            res[id] = total
        return res

    def _product_in_stock(self, cr, uid, ids, field, args, context=None):
        stock_obj = self.pool.get('stock.move')
        res = {}
        for id in ids:
            total_des = 0.0
            total = 0.0
            prod_id = self.browse(cr, uid, id)
            loc_dest_prod = prod_id.location_dest_id and\
                prod_id.location_dest_id.id or ''
            product_prod = prod_id.product_id and prod_id.product_id.id or ''
            if prod_id.move_created_ids2:
                for move in prod_id.move_created_ids2:
                    move_id = stock_obj.browse(cr, uid, move.id)
                    loc_dest_move = move_id.location_dest_id and\
                        move_id.location_dest_id.id or ''
                    state_move = move_id.state or ''
                    product_move = move_id.product_id and\
                        move_id.product_id.id or ''
                    if loc_dest_move != loc_dest_prod and\
                        state_move == 'done' and\
                            product_prod == product_move:
                        total_move = move_id.product_qty or 0.0
                        total_des = total_des + total_move
                    total_produced = prod_id.product_produced or 0.0
                    total = total_produced - total_des
            res[id] = total
        return res

    def _preview_lot(self, cr, uid, ids, name, args, context=None):
        sequence_obj = self.pool.get('ir.sequence')
        res = dict.fromkeys(ids)
        for element in self.browse(cr, uid, ids, context=context):
            product_lot_id = element.product_id.categ_id.x_lot_id.id
            lot = sequence_obj.preview_next_by_id(cr, uid, product_lot_id)
            res[element.id] = lot
        return res

    def _production_ratio(self, cr, uid, ids, name, args, context=None):
        product_in_stock = self._product_in_stock(cr, uid, ids, name, args)
        res = {}
        for id in ids:
            product_uom = self.pool.get('product.uom')
            prod_id = self.browse(cr, uid, id)

            prod_qt = prod_id.product_qty
            from_uom = prod_id.product_uom
            to_uom = prod_id.product_id.uom_id

            if (from_uom != to_uom):
                prod_qt = product_uom._compute_qty_obj(cr, uid, from_uom, prod_qt, to_uom)

            ratio = str(int(round(product_in_stock[id]/prod_qt*100,0))) + '%'
            res[id] = ratio
        return res

    _columns = {
        'temp_lot': fields.function(_preview_lot, method=True, type="char", string="Potential Lot"),
        'production_ratio': fields.function(_production_ratio, method=True, type="char", string="Ratio"),
        'product_produced': fields.function(_product_produced, method=True, type="float", string='Total Produced'),
        'product_in_stock': fields.function(_product_in_stock, method=True, type="float", string='Total In Stock'),
    }
