# -*- coding: utf-8 -*-
{
    'name': 'Stock Picking Manual Date Done',
    "summary": 'Set the date done manually',
    'version': '14.0.1.0.0',
    'author': 'Stephane AMAOUA',
    'category': 'Stock',
    'description': """
        User is able to set the stock picking date done manually at creation or let the system set the current day.
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
