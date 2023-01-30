import odoo

def migrate(cr, version):
    env = odoo.api.Environment(cr, odoo.SUPERUSER_ID, {})
    view = env['ir.ui.view'].search([('id', '=', 1327)])
    view.reset_arch(mode='hard')
    view.inherit_children_ids.reset_arch(mode='hard')
