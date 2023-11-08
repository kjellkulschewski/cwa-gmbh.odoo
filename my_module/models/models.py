# -*- coding: utf-8 -*-

from odoo import models, fields, api


class my_module(models.Model):
    _name = 'my_module.my_module'
    _description = 'Test module which contains orders'

    name = fields.Char(required=True)
    price = fields.Float(required=True)
    quantity = fields.Integer(required=True)
    mwst = fields.Float(compute="_compute_mwst", store=True)
    total = fields.Float(compute="_compute_total", store=True)
    description = fields.Text()

    @api.depends('price')
    def _compute_mwst(self):
        for record in self:
            record.mwst = float(record.price) * 0.19

    @api.depends('price', 'mwst', 'quantity')
    def _compute_total(self):
        for record in self:
            record.total = (float(record.price) + float(record.mwst)) * float(record.quantity)
