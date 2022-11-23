# -*- coding: utf-8 -*-
# from odoo import http


# class Sis-module(http.Controller):
#     @http.route('/sis-module/sis-module', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sis-module/sis-module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sis-module.listing', {
#             'root': '/sis-module/sis-module',
#             'objects': http.request.env['sis-module.sis-module'].search([]),
#         })

#     @http.route('/sis-module/sis-module/objects/<model("sis-module.sis-module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sis-module.object', {
#             'object': obj
#         })
