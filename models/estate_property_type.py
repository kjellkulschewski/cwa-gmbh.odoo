# -*- coding: utf-8 -*-

from odoo import models, fields


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
