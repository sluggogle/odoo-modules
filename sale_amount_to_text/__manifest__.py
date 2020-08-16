# -*- coding: utf-8 -*-
{
    'name': 'Sale Amount to text',
    "summary": 'A field with the amount in text',
    'version': '12.0.1.0.0',
    'author': 'AgenceZ7',
    'category': 'Sales',
    'description': """
        Adds a computed field in sale.order and account.invoice to display the amount by words in reports.
    """,
    'depends': [
        'sale_management', 'purchase'
    ],
    'data': [

    ],
    'application': False,
    'installable': True,
}
