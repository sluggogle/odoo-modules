# -*- coding: utf-8 -*-
# Copyright Monweblocal 2021

from odoo.addons.portal.controllers.portal import CustomerPortal, get_error

from odoo import http, _
from odoo.http import request

class CustomCustomerPortal(CustomerPortal):

    @http.route(['/my/account'], type='http', auth='user', website=True)
    def account(self, redirect=None, **post):
        res = super(CustomCustomerPortal, self).web_client(redirect, **post)
        res.headers.pop('X-Frame-Options', None)
        return res

    @http.route('/my/security', type='http', auth='user', website=True, methods=['GET', 'POST'])
    def security(self, **post):
        values = self._prepare_portal_layout_values()
        values['get_error'] = get_error

        if request.httprequest.method == 'POST':
            values.update(self._update_password(
                post['old'].strip(),
                post['new1'].strip(),
                post['new2'].strip()
            ))

        return request.render('portal.portal_my_security', values, headers={})