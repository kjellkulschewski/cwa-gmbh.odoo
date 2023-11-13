# -*- coding: utf-8 -*-

from odoo import models, fields


class EstateProperyTag(models.Model):
    _name = "estate.property.tag"
    _description = "This is the estate property tag."

    name = fields.Char(required=True)
