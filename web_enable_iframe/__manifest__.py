{
    'name': 'Enable embedding in iframe',
    'version': '14.0.1.0.0',
    'author': 'MonWebLocal',
    'category': 'Hidden',
    'description': """
        This module remove the `X-Frame-Options = DENY` header from Odoo web / portal / auth.
    """,
    'depends': [
        'web',
        'portal',
        # 'auth_signup'
    ],
    'data': [],
    'installable': True,
}
