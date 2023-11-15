# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
from odoo.tools.float_utils import float_compare, float_is_zero
from dateutil.relativedelta import relativedelta


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "This is the estate property."
    _sql_constraints = [
        ("check_expected_price", "CHECK(expected_price > 0.0)", "The expected price should be stricly positive."),
        ("check_selling_price", "CHECK(selling_price >= 0.0)", "The selling price should be positive.")
    ]

    name = fields.Char(required=True)
    property_type_id = fields.Many2one("estate.property.type", string="Property Type")
    buyer_id = fields.Many2one("res.partner", copy=False)
    salesperson_id = fields.Many2one("res.users", default=lambda self: self.env.user)
    tag_ids = fields.Many2many("estate.property.tag", string="Property Tag")
    offer_ids = fields.One2many("estate.property.offer", "property_id", string="Property Offers")
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(copy=False, default=fields.Date.today() + relativedelta(months=3))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    total_area = fields.Integer(compute="_compute_total_area")
    best_price = fields.Float(compute="_compute_best_price", string="Best Offer")
    garden_orientation = fields.Selection(
        string="Orientation",
        selection=[
            ("north", "North"),
            ("south", "South"),
            ("east", "East"),
            ("west", "West")
        ],
        help="Orientation equals the direction of the garden."
    )
    state = fields.Selection(
        string="Status",
        selection=[
            ("new", "New"),
            ("offer_received", "Offer Received"),
            ("offer_accepted", "Offer Accepted"),
            ("sold", "Sold"),
            ("canceled", "Canceled")
        ],
        help="State of the estate property",
        required=True,
        copy=False,
        default='new'
    )
    active = fields.Boolean(default=True)

    # computed
    @api.depends("living_area", "garden_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends("offer_ids.price")
    def _compute_best_price(self):
        for record in self:
            record.best_price = max(record.offer_ids.mapped("price")) if record.offer_ids else 0.0

    @api.onchange("garden")
    def _onchange_garden(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = "north"
        else:
            self.garden_area = 0
            self.garden_orientation = False

    # constraints
    @api.constrains("expected price", "selling_price")
    def _check_selling_price(self):
        for record in self:
            if float_compare(record.selling_price, record.expected_price * 0.9, precision_rounding=0.01) < 0:
                raise ValidationError("The selling price must be at least 90% of the expected price!")



    # action buttons
    def action_cancel(self):
        for record in self:
            if record.state == "sold":
                raise UserError("Sold properties cannot be cannot be canceled.")
            else:
                record.state = "canceled"
        return True

    def action_sold(self):
        for record in self:
            if record.state == "canceled":
                raise UserError("Cancelled properties cannot be sold.")
            else:
                record.state = "sold"
        return True



