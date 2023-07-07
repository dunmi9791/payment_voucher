# -*- coding: utf-8 -*-
# from odoo import http


# class PaymentVoucher(http.Controller):
#     @http.route('/payment_voucher/payment_voucher', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/payment_voucher/payment_voucher/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('payment_voucher.listing', {
#             'root': '/payment_voucher/payment_voucher',
#             'objects': http.request.env['payment_voucher.payment_voucher'].search([]),
#         })

#     @http.route('/payment_voucher/payment_voucher/objects/<model("payment_voucher.payment_voucher"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('payment_voucher.object', {
#             'object': obj
#         })
