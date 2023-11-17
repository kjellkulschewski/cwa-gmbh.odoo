# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models
from dateutil.relativedelta import relativedelta

class RecurringPlan(models.Model):
    _name = "estate.property.type"
    _description = "this is the estate property type Model class"

    name = fields.Char(required=True)
    

