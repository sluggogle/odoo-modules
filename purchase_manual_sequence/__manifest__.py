# -*- coding: utf-8 -*-
{
    'name': 'Purchase Manual Sequence',
    "summary": 'Set the sequence manually',
    'version': '14.0.1.0.0',
    'author': 'Stephane AMAOUA',
    'category': 'Purchases',
    'description': """
        User is able to set the purchase order reference manually at creation or let the system use the next sequence.
    """,
    'depends': [
        'purchase',
    ],
    'data': [
        'views/purchase_views.xml',
    ],
    'application': False,
    'installable': True,
}
