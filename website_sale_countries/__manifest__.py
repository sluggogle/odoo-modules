# Copyright Monweblocal 2020
{
    'name': 'Website Ecommerce Countries',
    'version': '14.0.1.0.0',
    'summary': 'Select countries available in the billing and shipping addresse forms',
    'description': """
        This module lets the customer choose only the countries selected for there billing and shipping addresses.
        To make a country available, go to Contact > Configuration > Countries and activate the button in the column `Show in Ecommerce`.
    """,
    'author': 'Monweblocal',
    'website': 'https://monweblocal.fr',
    'category': 'Website/Website',
    'license': 'OPL-1',
    'depends': [
        'website_sale_delivery',
    ],
    'data': [
        'views/res_country_views.xml',
    ],
    'auto_install': False,
    'application': False,
}