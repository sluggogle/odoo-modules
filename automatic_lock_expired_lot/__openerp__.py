# -*- coding: utf-8 -*-
{
    'name': "Automatic lock expired lots",

    'summary': """
Automatic task that lock lots with past expiry date
""",

    'description': """
A simple cron task running over every lot and lock those with past expiry date.
By default, runs every day to be sure not to consume expired products in MRP.

TODO:
    - Notify people from the warehouse

Requires 'stock_lock_lot' and 'mrp_lock_lot'.
""",

    'author': "Laboratoires Bories",
    'website': "http://www.laboratoires-bories.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'warehouse',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mrp_lock_lot'],

    # always loaded
    'data': [
        'data/automatic_lock.xml'
    ],
    # only loaded in demonstration mode
    'demo': [

    ],
}
