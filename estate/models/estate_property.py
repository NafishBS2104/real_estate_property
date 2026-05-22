from odoo import fields, models, api
from odoo.exceptions import UserError,ValidationError
from odoo.tools.float_utils import float_compare,float_is_zero

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Real Estate Property"
    _order = "id desc"


    _sql_constraints = [
        (
            "check_expected_price",
            "CHECK(expected_price > 0)",
            "The expected price must be greater than 0."
        ),
        (
            "check_selling_price",
            "CHECK(selling_price >= 0)",
            "The selling price must be positive."
        ),
    ]

    total_area = fields.Integer(compute="_compute_total_area")
    best_price = fields.Float(compute="_compute_best_price")

    name = fields.Char(required=True)
    description = fields.Text(required=False)
    postcode = fields.Char(required=False)
    date_availability = fields.Date(required=False)
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(required=False)
    bedrooms = fields.Integer(required=False)
    living_area = fields.Integer(required=False)
    facades = fields.Integer(required=False)
    garage = fields.Boolean(required=False)
    garden = fields.Boolean(required=False)
    garden_area = fields.Integer(required=False)
    garden_orientation = fields.Selection([
        ('north','North'),
        ('south','South'),
        ('east','East'),
        ('west','West')
    ])
    state = fields.Selection([
        ('new', 'New'),
        ('offer_received', 'Offer Received'),
        ('offer_accepted', 'Offer Accepted'),
        ('sold', 'Sold'),
        ('cancelled', 'Cancelled'),
    ], default='new')

    property_type_id = fields.Many2one("estate.property.type", string = "Property Type")
    buyer_id = fields.Many2one("res.partner" , string = "Buyer" , copy = False)
    user_id = fields.Many2one(
        "res.users",
        string = "Salesperson",
        default = lambda self: self.env.user
    )

    tag_ids = fields.Many2many("estate.property.tag", string = "Tags")
    offer_ids = fields.One2many(
        "estate.property.offer",
        "property_id",
        string = "Offers",
    )

    @api.depends("living_area","garden_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area



    @api.depends("offer_ids.price")
    def _compute_best_price(self):
        for record in self:
            record.best_price = max(record.offer_ids.mapped("price"),default=0.0)



    @api.onchange("garden")
    def _onchange_garden(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = "north"
        else:
            self.garden_area = 0
            self.garden_orientation = False


    @api.constrains("selling_price","expected_price")
    def _check_selling_price(self):
        for record in self:
            if float_is_zero(record.selling_price,precision_digits=2):
                continue

            min_price = record.expected_price * 0.9

            if float_compare(
                record.selling_price,
                min_price,
                precision_digits = 2
            ) < 0 :
                raise ValidationError(
                    "The Selling Price cannot be lower than 90% of the expected price."
                )


    def action_sold(self):
        for record in self:
            if record.state == "cancelled":
                raise UserError("A cancel property cannot be sold.")
            record.state = "sold"
        return True

    def action_cancel(self):
        for record in self:
            if record.state == "sold":
                raise UserError("A sold property cannot be cancelled.")
            record.state = "cancelled"
        return True