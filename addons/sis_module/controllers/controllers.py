# -*- coding: utf-8 -*-
# from odoo import http


# class sis_module(http.Controller):
#     @http.route('/sis_module/sis_module', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sis_module/sis_module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sis_module.listing', {
#             'root': '/sis_module/sis_module',
#             'objects': http.request.env['sis_module.sis_module'].search([]),
#         })

#     @http.route('/sis_module/sis_module/objects/<model("sis_module.sis_module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sis_module.object', {
#             'object': obj
#         })
