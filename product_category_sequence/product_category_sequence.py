# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.tools.translate import _

import logging
_logger = logging.getLogger(__name__)

########################################################
## First Add the sequence_id field to product.category #
########################################################
class ProductCategory(models.Model):
    _inherit = 'product.category'
    x_sequence_id = fields.Many2one(comodel_name='ir.sequence',
                                    string='Product Sequence',
                                    help=_("This sequence will be use for products' internal references"))

##################################################
# Now each time we create a product
#   - Get its category sequence (upward)
#   - Set sequence found or default one
##################################################
# class ProductTemplate(models.Model):
#     _inherit = 'product.template'

#     default_code = fields.Char(
#         string='Reference',
#         size=64,
#         select=True,
#         required=False,
#         default='Auto')

#     _sql_constraints = [
#         ('uniq_default_code',
#          'unique(default_code)',
#          _('The reference must be unique')),
#     ]

#     def _getInternalReference(self, vals):
#         # If editing categ_id is not in vals
#         if 'categ_id' not in vals:
#             categ_id = self.categ_id.id
#         else:
#             categ_id = vals['categ_id']

#         # Looking for category sequence bottom-->up
#         sequence_id = self.env['product.category'].browse(categ_id).x_sequence_id.id
#         while sequence_id == False:
#             categ_id = self.env['product.category'].browse(categ_id).parent_id.id
#             if categ_id == False:
#                 break
#             sequence_id = self.env['product.category'].browse(categ_id).x_sequence_id.id

#         if sequence_id is False:
#             _logger.info('Category has no sequence set ! Setting default sequence')
#             ref_code = self.env['ir.sequence'].search([('name', '=', 'Default Product Sequence')])._next()
#         else:
#             _logger.info('Product category sequence found !')
#             ref_code = self.env['ir.sequence'].get_id(sequence_id)
            
#         _logger.info('ref_code: %s', ref_code)
#         return ref_code
    
#     @api.model
#     def create(self, vals):
#         if 'default_code' in vals and vals['default_code'] == 'Auto':
#             vals['default_code'] = self._getInternalReference(vals)
#         return super (ProductTemplate, self).create(vals)

#     @api.multi
#     def write(self, vals):
#         for product in self:
#             if 'default_code' in vals and vals['default_code'] == 'Auto':
#                 vals['default_code'] = self._getInternalReference(vals)
#             elif product.default_code == 'Auto':
#                 vals['default_code'] = self._getInternalReference(vals)
#             super(ProductTemplate, product).write(vals)
#         return True

##################################################
# Same for product.product
##################################################
class ProductProduct(models.Model):
    _inherit = 'product.product'

    default_code = fields.Char(
        string='Reference',
        size=64,
        select=True,
        required=True,
        default='Auto')

    _sql_constraints = [
        ('uniq_default_code',
         'unique(default_code)',
         _('The reference must be unique')),
    ]

    def _getInternalReference(self, vals):
        # If editing categ_id is not in vals
        _logger.info('Looking for category...')
        if 'categ_id' not in vals:
            _logger.info('... category not in vals')
            if 'product_tmpl_id' in vals:
                _logger.info('... using template category in vals')
                categ_id = self.env['product.template'].browse(vals['product_tmpl_id']).categ_id.id
            else:
                _logger.info('... using product category')
                categ_id = self.categ_id.id
        else:
            categ_id = vals['categ_id']
        
        # Looking for category sequence bottom-->up
        sequence_id = self.env['product.category'].browse(categ_id).x_sequence_id.id
        while sequence_id == False:
            categ_id = self.env['product.category'].browse(categ_id).parent_id.id
            if categ_id == False:
                break
            sequence_id = self.env['product.category'].browse(categ_id).x_sequence_id.id

        if sequence_id is False:
            _logger.info('Category has no sequence set ! Setting default sequence')
            ref_code = self.env['ir.sequence'].search([('name', '=', 'Default Product Sequence')])._next()
        else:
            _logger.info('Product category sequence found !')
            ref_code = self.env['ir.sequence'].get_id(sequence_id)
            
        _logger.info('ref_code: %s', ref_code)
        return ref_code
    
    @api.model
    def create(self, vals):
        product = super(ProductProduct, self).create(vals)
        _logger.info('Product Create id: %s', product.id)
        _logger.info('Product Create vals: %s', vals)

        # Default code is set
        if product.default_code == 'Auto':
            product.default_code = self._getInternalReference(vals)

        return product

    @api.one
    def write(self, vals):
        _logger.info('Product Write: self: %s', self)
        _logger.info('Product Write: id: %s / %s', self.id, vals)
        for product in self:
            if 'default_code' in vals and vals['default_code'] == 'Auto':
                vals['default_code'] = self._getInternalReference(vals)
            super(ProductProduct, product).write(vals)
        return True
