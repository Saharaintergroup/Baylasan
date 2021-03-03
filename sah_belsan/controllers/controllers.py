# -*- coding: utf-8 -*-
from odoo import http

# class SahBelsan(http.Controller):
#     @http.route('/sah_belsan/sah_belsan/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sah_belsan/sah_belsan/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sah_belsan.listing', {
#             'root': '/sah_belsan/sah_belsan',
#             'objects': http.request.env['sah_belsan.sah_belsan'].search([]),
#         })

#     @http.route('/sah_belsan/sah_belsan/objects/<model("sah_belsan.sah_belsan"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sah_belsan.object', {
#             'object': obj
#         })