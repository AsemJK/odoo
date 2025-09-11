# -*- coding: utf-8 -*-
# from odoo import http


# class Econtract(http.Controller):
#     @http.route('/econtract/econtract', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/econtract/econtract/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('econtract.listing', {
#             'root': '/econtract/econtract',
#             'objects': http.request.env['econtract.econtract'].search([]),
#         })

#     @http.route('/econtract/econtract/objects/<model("econtract.econtract"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('econtract.object', {
#             'object': obj
#         })

