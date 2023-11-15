# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError
from dateutil.relativedelta import relativedelta


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "This is the estate property offer."
    _sql_constraints = [
        ("check_offer_price", "CHECK(price > 0.0)", "The offer price should be strictly positive.")
    ]

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

    # computed
    @api.depends("create_date", "validity")
    def _compute_date_deadline(self):
        for record in self:
            date = record.create_date.date() if record.create_date else fields.Date.today()
            record.date_deadline = date + relativedelta(days=record.validity)

    def _inverse_date_deadline(self):
        for record in self:
            date = record.create_date.date() if record.create_date else fields.Date.today()
            record.validity = (record.date_deadline - date).days

    # action buttons
    def action_accept(self):
        for record in self:
            if "accepted" in self.mapped("property_id.offer_ids.status"):
                raise UserError("Offer for property was already accepted.")
            else:
                record.status = "accepted"
                record.property_id.selling_price = record.price
                record.property_id.buyer_id = record.partner_id
        return True

    def action_refuse(self):
        for record in self:
            record.status = "refused"
        return True


