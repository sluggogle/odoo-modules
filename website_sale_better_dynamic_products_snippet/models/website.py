# -*- coding: utf-8 -*-
# Copyright Monweblocal 2020

from odoo import models, _

class Website(models.Model):
    _inherit = 'website'

    def _bootstrap_snippet_filters(self):
        super(Website, self)._bootstrap_snippet_filters()
        action = self.env.ref('website_sale_better_dynamic_products_snippet.dynamic_snippet_product_templates_action', raise_if_not_found=False)
        if action:
            self.env['website.snippet.filter'].create({
                'action_server_id': action.id,
                'field_names': 'display_name,description_sale,image_512,list_price',
                'limit': 16,
                'name': _('Product Templates'),
                'website_id': self.id,
            })

