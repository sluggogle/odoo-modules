# -*- coding: utf-8 -*-
{
    'name': 'Sale Manual Sequence',
    "summary": 'Set the sequence manually',
    'version': '14.0.1.0.0',
    'author': 'Stephane AMAOUA',
    'category': 'Sales',
    'description': """
        User is able to set the sale order reference manually at creation or let the system use the next sequence.
    """,
    'depends': [
        'sale_management',
    ],
    'data': [
        'views/sale_views.xml',
    ],
    'application': False,
    'installable': True,
}
