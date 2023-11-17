# -*- coding: utf-8 -*-

from odoo import models, fields, api


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "This is the estate property type."
    _order = "sequence, name"
    _sql_constraints = [
        ("unique_type_name", "UNIQUE(name)", "The type name should be unique.")
    ]

    name = fields.Char(required=True)
    property_ids = fields.One2many("estate.property", "property_type_id", string="Properties")
    sequence = fields.Integer("Sequence", default=1)
    offer_ids = fields.One2many("estate.property.offer", inverse_name="property_type_id", string="Offers")
    offer_count = fields.Integer(compute="_compute_offer_count")

    @api.depends('offer_ids')
    def _compute_offer_count(self):
        for record in self:
            if record.offer_ids == self:
                record.offer_count += 1

