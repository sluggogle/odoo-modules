# Copyright Monweblocal 2020
{
    'name': 'Website Product Not Available',
    'version': '14.0.1.1.0',
    'summary': 'Option to show a product in the shop while it cannot be added to cart.',
    'description': """
        This module adds a new option in the product availability for products not available but still showed in the shop.
        User may define a custom message to customers. Set item price to 0 to hide the price.
    """,
    'author': 'Monweblocal',
    'website': 'https://monweblocal.fr',
    'category': 'Website/Website',
    'depends': [
        'website_sale_stock',
    ],
    'data': [
        'views/product_template_views.xml',
        'views/website_sale_stock_templates.xml',
    ],
    'demo': [
        ''
    ],
    'auto_install': False,
    'application': False,
}