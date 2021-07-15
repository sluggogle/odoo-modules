# -*- coding: utf-8 -*-
# Copyright Monweblocal 2021

from odoo.addons.web.controllers.main import Home

from odoo import http, _
from odoo.http import request

class CustomHome(Home):

    @http.route('/web', type='http', auth="none", csrf=False)
    def web_client(self, s_action=None, **kw):
        res = super(CustomHome, self).web_client(s_action, **kw)
        res.headers.pop('X-Frame-Options', None)
        return res

    @http.route('/web/login', type='http', auth="none", csrf=False)
    def web_login(self, redirect=None, **kw):
        res = super(CustomHome, self).web_login(redirect, **kw)
        res.headers.pop('X-Frame-Options', None)
        return res