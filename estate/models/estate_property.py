from odoo import fields, models, api
from datetime import date
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError,ValidationError


class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Estate Property'

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    active = fields.Boolean(string="active", default=True)
    state = fields.Selection(
        selection=[
            ('new', 'New'),
            ('offer_received', 'Offer Received'),
            ('offer_accepted', 'Offer Accepted'),
            ('sold', 'Sold'),
            ('cancelled', 'Cancelled'),
        ],
        string="Status",
        required=True,
        copy=False,
        default='new',
    )
    date_availability = fields.Date(string="Available From", copy=False,
                                    default=lambda self: date.today() + relativedelta(months=3))
    expected_price = fields.Float(required=True)
    _sql_constraints = [
        (
            'expected_price',
            'CHECK(expected_price >= 0.0)',
            'Expected Price Must Be Positive'
        )
    ]
    selling_price = fields.Float(string="Selling Price", copy=False, readonly=True)
    _sql_constraints = [
        (
            'selling_price',
            'CHECK(selling_price >= 0.0)',
            'Selling Price Must Be Positive'
        )
    ]
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
        string="Orientation"
    )
    property_type_id = fields.Many2one("estate.property.type", string="Property Type")
    salesperson_id = fields.Many2one("res.users", string="Salesperson", default=lambda self: self.env.user)
    buyer_id = fields.Many2one("res.partner", string="Buyer", copy=False)
    tag_ids = fields.Many2many("estate.property.tag", string="Tags")
    offer_ids = fields.One2many("estate.property.offer", "property_id", string="Offers")
    total_area = fields.Integer(string="Total Area", compute="_compute_area")

    @api.depends("living_area", "garden_area")
    def _compute_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    best_price = fields.Integer(string="Best Price", compute="_compute_best_price")

    @api.depends("offer_ids.price")
    def _compute_best_price(self):
        for record in self:
            prices = record.offer_ids.mapped("price")
        if prices:
            record.best_price = max(prices)
        else:
            record.best_price = 0.0

    @api.onchange("garden")
    def _onchange_garden(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = 'north'
        else:
            self.garden_area = False
            self.garden_orientation = False

    def action_sell(self):
        for record in self:
            if record.state == 'cancelled':
                raise UserError('Cannot sell cancelled property')
            record.state = 'sold'
        return True

    def action_cancel(self):
        for record in self:
            if record.state == 'sold':
                raise UserError('Cannot cancel sold property')
            record.state = 'cancelled'
        return True

    @api.onchange("selling_price")
    @api.constrains('expected_price','selling_price')
    def _validate_selling_price(self):
        for record in self:
            if record.expected_price * 0.9 > record.selling_price:
                raise ValidationError("Selling price must be at least 90% of the expected price")
