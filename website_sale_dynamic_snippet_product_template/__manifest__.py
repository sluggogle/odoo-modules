# Copyright Monweblocal 2020
#
# TODO:
#
#
{
    'name': 'eCommerce Product Template in Dynamic Snippet ',
    'version': '14.0.1.1.0',
    'summary': 'Product templates usable in dynamic snippet',
    'description': """
        This module adds product template as a model to render in the Dynamic snippet.
        Thus it makes the model also available for Dynamic Snippet Carousel.
    """,
    'author': 'Monweblocal',
    'website': 'https://monweblocal.fr',
    'category': 'Website/Website',
    'depends': [
        'website_sale',
    ],
    'data': [
        'data/dynamic_snippet.xml',
        'views/assets.xml',
    ],
    'demo': [
        ''
    ],
    'auto_install': False,
    'application': False,
}