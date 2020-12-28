# Copyright Monweblocal 2020
{
    'name': 'Website Blog Post Form Content',
    'version': '14.0.1.0.0',
    'summary': 'Adds the blog post\'s content in the form view',
    'description': """
        This module adds the blog post's content in the form view. It enables the user to edit directly in the backend.
    """,
    'author': 'Monweblocal',
    'website': 'https://monweblocal.fr',
    'category': 'Website/Website',
    'depends': [
        'website_blog',
    ],
    'data': [
        'views/website_blog_views.xml',
    ],
    'demo': [
        ''
    ],
    'auto_install': False,
    'application': False,
}