# Copyright Monweblocal 2020
#
# TODO:
#   - Remove specific behavior for our customer (to tag_product_not_available)
#   - In the controller, we make a request per product: should be possible to reduce
#   - Products not available for sale are only disabled in the frontend but the backend would still accept them
#       - Either in /addons/website_sale/models/sale_order.py -> _cart_update()
#       - Or in /addons/website_sale/controllers/main.py -> @http.route(['/shop/cart/update'] and @http.route(['/shop/cart/update_json']
#
{
    'name': 'Website Product Not Available',
    'version': '14.0.1.1.0',
    'summary': 'Option to show a product in the shop while it cannot be added to cart.',
    'description': """
        This module adds a new option in the product availability for products not available but still showed in the shop.
        User may define a custom message to customers. Set item price to 0 to hide the price.

        The module also modifies the "Recently Viewed Product" snippet by:
            - disabling the addToCart button
            - printing another message instead of the product price
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
    'uninstall_hook': 'uninstall_hook',
}