# -*- coding: utf-8 -*-

from odoo import models, fields


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "This is the estate property type."
    _sql_constraints = [
        ("unique_type_name", "UNIQUE(name)", "The type name should be unique.")
    ]

    name = fields.Char(required=True)
