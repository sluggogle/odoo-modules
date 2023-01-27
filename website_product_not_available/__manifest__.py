# Copyright Monweblocal 2020
#
# TODO:
#   - Remove specific behavior for our customer (to tag_product_not_available)
#   - In the controller, we make a request per product: should be possible to reduce
#   - Products not available for sale are blocked in the controller but without message
#
{
    'name': 'Website Product Not Available',
    'version': '15.0.1.2.0',
    'summary': 'Option to show a product in the shop while it cannot be added to cart.',
    'description': """
        This module adds a new option for products not available but still showed in the shop.
        User may define a custom message to customers. Set item price to 0 to hide the price.
    """,
    'author': 'Monweblocal',
    'website': 'https://monweblocal.fr',
    'category': 'Website/Website',
    'license': 'OPL-1',
    'depends': [
        'website_sale_stock',
    ],
    'data': [
        'views/product_template_views.xml',
        'views/website_sale_stock_templates.xml',
    ],
    'auto_install': False,
    'application': False,
}