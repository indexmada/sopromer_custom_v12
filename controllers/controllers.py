# -*- coding: utf-8 -*-
from odoo import http

# class SopromerCustomV12(http.Controller):
#     @http.route('/sopromer_custom_v12/sopromer_custom_v12/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sopromer_custom_v12/sopromer_custom_v12/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sopromer_custom_v12.listing', {
#             'root': '/sopromer_custom_v12/sopromer_custom_v12',
#             'objects': http.request.env['sopromer_custom_v12.sopromer_custom_v12'].search([]),
#         })

#     @http.route('/sopromer_custom_v12/sopromer_custom_v12/objects/<model("sopromer_custom_v12.sopromer_custom_v12"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sopromer_custom_v12.object', {
#             'object': obj
#         })