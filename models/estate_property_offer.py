# -*- coding: utf-8 -*-

from odoo import models, fields, api
from dateutil.relativedelta import relativedelta


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "This is the estate property offer."

    price = fields.Float()
    status = fields.Selection(
        string="Status",
        selection=[
            ("accepted", "Accepted"),
            ("refused", "Refused")
        ],
        help="Indicates whether an property offer was accepted or refused.",
        copy=False
    )
    partner_id = fields.Many2one("res.partner", required=True)
    property_id = fields.Many2one("estate.property", required=True)
    validity = fields.Integer(default=7)
    date_deadline = fields.Date(compute="_compute_date_deadline", inverse="_inverse_date_deadline")

    @api.depends("create_date", "validity")
    def _compute_date_deadline(self):
        for record in self:
            date = record.create_date.date() if record.create_date else fields.Date.today()
            record.date_deadline = date + relativedelta(days=record.validity)

    def _inverse_date_deadline(self):
        for record in self:
            date = record.create_date.date() if record.create_date else fields.Date.today()
            record.validity = (record.date_deadline - date).days
