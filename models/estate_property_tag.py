# -*- coding: utf-8 -*-

from odoo import models, fields


class EstateProperyTag(models.Model):
    _name = "estate.property.tag"
    _description = "This is the estate property tag."
    _sql_constraints = [
        ("unique_tag_name", "UNIQUE(name)", "The tag name should be unique.")
    ]

    name = fields.Char(required=True)


