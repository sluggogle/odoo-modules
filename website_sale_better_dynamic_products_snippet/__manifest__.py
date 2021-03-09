# Copyright Monweblocal 2020
#
# TODO:
#   - Adapt `Header Image Footer Card` template to support ribbon
#
{
    'name': 'eCommerce Better Dynamic Products Snippet',
    'version': '14.0.1.1.0',
    'summary': 'Dynamic Products snippet with template and ribbons',
    'description': """
        This module adds product template as a model to render in the Dynamic snippet.
        Thus it makes the model also available for Dynamic Carousel and Dynamic Products.

        It also checks if there's a ribbon configured on the product and adapts the default templates.
    """,
    'author': 'Monweblocal',
    'website': 'https://monweblocal.fr',
    'category': 'Website/Website',
    'depends': [
        'website_sale',
    ],
    'data': [
        'data/website_data.xml',
        'data/dynamic_snippet.xml',
        'views/assets.xml',
    ],
    'demo': [
        ''
    ],
    'auto_install': False,
    'application': False,
}