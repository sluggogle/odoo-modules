# -*- coding: utf-8 -*-
{
    'name': 'Sale Amount to text',
    "summary": 'A field with the amount in text',
    'version': '15.0.1.0.0',
    'author': 'Stephane AMAOUA',
    'category': 'Sales',
    'description': """
        Adds a computed field in sale.order and account.invoice to display the amount by words in reports.
    """,
    'depends': [
        'sale_management',
    ],
    'data': [

    ],
    'application': False,
    'installable': True,
}
