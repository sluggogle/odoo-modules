# -*- coding: utf-8 -*-
{
    'name': 'Stock Picking Manual Sequence',
    "summary": 'Set the sequence manually',
    'version': '14.0.1.0.0',
    'author': 'Stephane AMAOUA',
    'category': 'Stock',
    'description': """
        User is able to set the stock picking sequence manually at creation or let the system use the next sequence.
    """,
    'depends': [
        'stock',
    ],
    'data': [
        'views/stock_views.xml',
    ],
    'application': False,
    'installable': True,
}
