# -*- coding: utf-8 -*-
{
    'name': "Stock Picking Multiple Locations",

    'summary': """
Allows to set multiple source/destination location per picking order.
""",

    'description': """
This module allows to set lines from multiple source or destination location.\n\n

""",

    'author': "Laboratoires Bories",
    'website': "http://www.laboratoires-bories.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Product',
    'version': '8.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','stock'],

    # always loaded
    'data': [
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
