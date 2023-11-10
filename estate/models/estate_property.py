# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models
from dateutil.relativedelta import relativedelta

class RecurringPlan(models.Model):
    _name = "estate_property"
    _description = "this is a estate_property example"
    _order = "sequence"

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char(required=True)
    date_availability = fields.Date(copy=False, default=fields.Date.today() + relativedelta(months=3))
    expected_price = fields.float(required=True)
    selling_price = fields.float(readonly=True,copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Boolean()
    garden_orientation = fields.Selection(
        string='Orientation',
        selection=[('north','North'),('east','East'),('south','South'),('west','West')],
        help="Orientation is the direction from Point A to Point B.However it is always one of the four sides of the Horizon"
    active = fields.Boolean('Active',readonly=True)
    )
