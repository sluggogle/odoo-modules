# -*- coding: utf-8 -*-
{
    'name': "Report MRP Order - Uom Conversion",

    'summary': """
Define a custom parser for report_mrporder report.
The parser adds the keyword uom_conversion to change the quant qty by the equivalent UOM value.
""",

    'description': """
Define a custom parser for report_mrporder report.\n
The parser adds the keyword uom_conversion to change the quant qty by the equivalent UOM value.

""",

    'author': "Laboratoires Bories",
    'website': "http://www.laboratoires-bories.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Report',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mrp'],

    # always loaded
    'data': [

    ],
    # only loaded in demonstration mode
    'demo': [

    ],
}
