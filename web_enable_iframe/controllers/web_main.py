# -*- coding: utf-8 -*-
# Copyright Monweblocal 2021

import logging
from odoo.addons.web.controllers.main import Home

from odoo import http, _
from odoo.http import request

import logging
_logger = logging.getLogger(__name__)

class CustomHome(Home):

    @http.route('/web', type='http', auth="none", csrf=False)
    def web_client(self, s_action=None, **kw):
        res = super(CustomHome, self).web_client(s_action, **kw)
        res.headers.pop('X-Frame-Options', None)
        _logger.info(res.headers['Set-Cookie'])
        return res

    @http.route('/web/login', type='http', auth="none", csrf=False)
    def web_login(self, redirect=None, **kw):
        res = super(CustomHome, self).web_login(redirect, **kw)
        res.headers.pop('X-Frame-Options', None)
        return res