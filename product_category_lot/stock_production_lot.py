# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.exceptions import ValidationError
from openerp.tools.translate import _

import logging
_logger = logging.getLogger(__name__)

########################################################
## Add the lot_id field to product.category            #
########################################################
class StockProductionLot(models.Model):
    _inherit = 'stock.production.lot'

    # @api needed to translate from old api to new
    @api.model
    def _findGoodSequence(self, vals):
        _logger.info("in vals: %s", vals)
        product_id = vals.get('default_product_id', False)
        if product_id is False:
            product_id = vals.get('product_id', False)
        _logger.info('Product ID: %s', product_id)

        #If a product was set
        #  Looking for category lot sequence bottom-->up
        if product_id:
            categ_id = self.env['product.product'].browse(product_id).categ_id.id
            _logger.info('Category ID: %s', categ_id)
            lot_id = self.env['product.category'].browse(categ_id).x_lot_id.id
            _logger.info('Lot ID: %s', lot_id)

            while lot_id is False:
                categ_id = self.env['product.category'].browse(categ_id).parent_id.id
                if categ_id == False:
                    break
                lot_id = self.env['product.category'].browse(categ_id).x_lot_id.id
            
            # Not set, using default serial number
            if lot_id is False:
                _logger.info('Category has no sequence set ! Setting default sequence')
                lot_code = self.env['ir.sequence'].search([('name', '=', 'Serial Numbers')])._next()

            # Found ! Using it
            else:
                _logger.info('Product category lot found !')
                lot_code = self.env['ir.sequence'].get_id(lot_id)

        # Product empty, using default
        else:
            lot_code = self.env['ir.sequence'].search([('name', '=', 'Serial Numbers')])._next()

        _logger.info('Lot: %s', lot_code)
        return lot_code

    _defaults = {
        'name': _findGoodSequence,
    }

    #_sql_constraints = [
    #    ('unique_name',
    #     'unique(name)',
    #     'Lot number already exists !')
    #]

    #@api.one
    #@api.constrains('name')
    #def _check_unique_name(self):
    #    record = self.search([('name', '=', self.name)])
    #    val = len(record)
    #    _logger.info('\n\nRecord: %s\n\n', record)
    #    _logger.info('\n\nVal: %s\n\n', val)
    #    _logger.info('\n\nName: %s\n\n', self.name)
    #    if (val > 0):
    #        raise ValidationError("Lot number already exists !")
