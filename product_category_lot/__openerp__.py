# -*- coding: utf-8 -*-
{
    'name': "Product Category Lot Sequence",

    'summary': """
Category lot sequence type used for product lot.
""",

    'description': """
This module allows you to set a sequence to a product category so each time you add a new lot of this category, the lot number will be set with the next sequence value.\n\n

When no sequence is set, default serial numbers will set by default.\n\n

""",

    'author': "Laboratoires Bories",
    'website': "http://www.laboratoires-bories.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Product',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','product', 'stock'],

    # always loaded
    'data': [
        'product_category.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo.xml',
    ],
}
