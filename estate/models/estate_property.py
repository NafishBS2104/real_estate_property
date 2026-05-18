from odoo import fields,models

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Real Estate Property"

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