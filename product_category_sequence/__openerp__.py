# -*- coding: utf-8 -*-
{
    'name': "Product Category Sequence",

    'summary': """
Category sequence type used for product internal references.
""",

    'description': """
This module allows you to set a sequence to a product category so each time you create a product (template only) of this category, the internal reference will be set with the next sequence value.\n
If you set the wrong reference, you can generate a new code from the sequence by writting 'Auto' in the field.\n\n

/!\\ The field is not unique so you can leave it empty /!\\\n

The module comes with a default sequence used when no sequence is set.\n\n

Todo:\n
- Add a button to write 'Auto' in the field.\n
""",

    'author': "Laboratoires Bories",
    'website': "http://www.laboratoires-bories.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Product',
    'version': '8.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','product'],

    # always loaded
    'data': [
        'product_category.xml',
        'data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo.xml',
    ],
}
