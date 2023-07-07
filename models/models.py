#-*- coding: utf-8 -*-
from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    state = fields.Selection(selection_add=[('fc_control', 'FC Approval'), ('cfo_approve', 'CFO Approval')],
                             ondelete={'fc_control': 'cascade', 'cfo_approve': 'cascade'})


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    def fc_approve(self):
        self.write({
            'state': 'fc_control',
        })

    def cfo_approve(self):
        self.write({
            'state': 'cfo_approve',
        })




# class payment_voucher(models.Model):
#     _name = 'payment_voucher.payment_voucher'
#     _description = 'payment_voucher.payment_voucher'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
