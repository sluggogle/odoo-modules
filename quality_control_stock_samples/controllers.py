# -*- coding: utf-8 -*-
from openerp import http

# class QualityControlStockSamples(http.Controller):
#     @http.route('/quality_control_stock_samples/quality_control_stock_samples/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/quality_control_stock_samples/quality_control_stock_samples/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('quality_control_stock_samples.listing', {
#             'root': '/quality_control_stock_samples/quality_control_stock_samples',
#             'objects': http.request.env['quality_control_stock_samples.quality_control_stock_samples'].search([]),
#         })

#     @http.route('/quality_control_stock_samples/quality_control_stock_samples/objects/<model("quality_control_stock_samples.quality_control_stock_samples"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('quality_control_stock_samples.object', {
#             'object': obj
#         })