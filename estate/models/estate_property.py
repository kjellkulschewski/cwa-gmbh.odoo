# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models
from dateutil.relativedelta import relativedelta

class RecurringPlan(models.Model):
    _name = "estate.property"
    _description = "this is a estate_property example"


    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char(required=True)
    date_availability = fields.Date(copy=False, default=fields.Date.today() + relativedelta(months=3))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True,copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string='Orientation',
        selection=[('north','North'),('east','East'),('south','South'),('west','West')],
        help="Orientation is the direction from Point A to Point B.However it is always one of the four sides of the Horizon"
    )
    garden_state = fields.Selection(
        string='Status',
        selection=[("new","New"),("offer received","offer received"),('offer accepted','Offer Accepted'),('sold','Sold'),("canceled","Canceled")],
        help="Status is the current situation of the Offer",
        required=True,
        copy=False,
        default='new'
    )
    active = fields.Boolean()
    property_type_id = fields.Integer()
    salesperson_id = fields.Many2one('res.users', string='Salesperson', default=lambda self: self.env.user)
    buyer_id = fields.Many2one('res.partner', string='Buyer',copy=False)
    estate_property_id = fields.Many2one('res.user',string="Property Type")