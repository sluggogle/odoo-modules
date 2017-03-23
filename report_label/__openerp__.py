# -*- coding: utf-8 -*-
{
    'name': "Report Label",

    'summary': """
Just for us !
""",

    'description': """
Adding --disable-smart-shrinking to wkhtmlpdf command when the paperformat id is 3 (Label A4).\n\n

""",

    'author': "Laboratoires Bories",
    'website': "http://www.laboratoires-bories.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Reporting',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','report'],

    # always loaded
    'data': [

    ],
    # only loaded in demonstration mode
    'demo': [

    ],
}
