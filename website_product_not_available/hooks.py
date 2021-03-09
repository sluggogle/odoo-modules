# Copyright Monweblocal 2020

def uninstall_hook(cr, registry):
    """Restore inventory_availability to default value for products"""
    cr.execute("""
        UPDATE product_template
        SET inventory_availability = 'never'
        WHERE inventory_availability = 'not_available'
    """)