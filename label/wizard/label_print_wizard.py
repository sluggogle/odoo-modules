# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2011-Today Serpent Consulting Services Pvt. Ltd.
#    (<http://www.serpentcs.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
##############################################################################

from openerp import fields,models,api,_
from openerp.tools import misc
import math

class label_print_wizard(models.TransientModel):

    _name = 'label.print.wizard'

    @api.model
    def default_get(self,fields):
        if self._context is None:
            self._context = {}
        result = super(label_print_wizard, self).default_get(fields)
        if self._context.get('label_print'):
            label_print_obj = self.env['label.print']
            label_print_data = label_print_obj.browse(self._context.get('label_print'))
            for field in label_print_data.field_ids:
                if field.type == 'image':
                    result['is_image'] = True
                if field.type == 'barcode':
                    result['is_barcode'] = True
        return result

    name = fields.Many2one('label.config','Label Size', required=True)
    company_logo = fields.Boolean('Company Logo', help='Add the company logo ?')
    number_of_copy = fields.Integer('Number Of Copy', required=True,default=1)
    image_width = fields.Float('Width',default=50)
    image_height = fields.Float('Height',default=50)
    barcode_width = fields.Float('Width',default=50)
    barcode_height = fields.Float('Height',default=50)
    is_barcode = fields.Boolean('Is Barcode?')
    is_image = fields.Boolean('Is Image?')
    brand_id = fields.Many2one('label.brand', 'Brand Name', required=True)

    @api.multi
    def print_report(self):
        if self._context is None:
            self._context = {}
        if not self._context.get('label_print') or not self._context.get('active_ids'):
            return False
        total_record = len(self._context.get('active_ids', []))
        datas = {}
        for data in self.browse(self.ids):
            column = float(210) / float(data.name.width or 1)
            total_row = math.ceil(float(total_record)/ (column or 1))
            no_row_per_page = int(297 / data.name.height)
            height = 297 / (no_row_per_page or 1)
            logo_size = float(data.name.height / 3.0)
            datas = {
                'rows': int(total_row),
                'columns': int(column) == 0 and 1 or int(column),
                'model' : self._context.get('active_model'),
                'height' : str(data.name.height) + "mm",
                'no_row_per_page': no_row_per_page,
                'logo_size': str(logo_size) + "mm",
                'width' : str(data.name.width) + "mm",
                'image_width': str(data.image_width)+"mm",
                'image_height':str(data.image_height)+"mm",
                'barcode_width':data.barcode_width,
                'barcode_height':data.barcode_height,
                'font_size' : 10,
                'number_of_copy': data.number_of_copy,
                'top_margin' : str(data.name.top_margin) + "mm",
                'bottom_margin' :str(data.name.bottom_margin) + "mm",
                'left_margin' : str(data.name.left_margin) + "mm",
                'right_margin' : str(data.name.right_margin) + "mm",
                'cell_spacing' : str(data.name.cell_spacing)+ "px",
                'ids': self._context.get('active_ids', [])
            }
        cr,uid,context=self.env.args
        context = dict(context)
        context.update({'label_print_id':self._context.get('label_print'),
                        'datas': datas})
        self.env.args = cr,uid,misc.frozendict(context)

        data = {
            'ids': self.ids,
            'company_logo': self.company_logo,
            'model':'label.config',
            'form':datas
        }
        return self.env['report'].get_action(self,'label.report_label',
                                             data=data)
