from odoo import fields,models
from datetime import date
from dateutil.relativedelta import relativedelta

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Real Estate Property"
    _inherit = "estate.property"
    name = fields.Char(required = True)
    description = fields.Text(required = False)
    postcode = fields.Char(required = False)
    active = fields.Boolean(string="active" , default = True)
    state = fields.Selection(
        selection=[
            ('new','New'),
            ('offer_received','Offer Received'),
            ('offer_accepted','Offer Accepted'),
            ('sold','Sold'),
            ('cancelled','Cancelled'),
        ],
        string="Status",
        required = True,
        copy = False,
        default = 'new',
    )
    date_availability = fields.Date(string="Available From",copy = False,default=lambda self: date.today() + relativedelta(months=3))
    expected_price = fields.Float(required = True)
    selling_price =fields.Float(string = "Selling Price",copy = False,readonly = True)
    bedrooms = fields.Integer(required = False)
    living_area = fields.Integer(required = False)
    facades = fields.Integer(required = False)
    garage = fields.Integer(required = False)
    garden = fields.Integer(required = False)
    garden_area = fields.Selection(
        selection = [('north','North'),('south','South'),('east','East'),('west','West')],
        string="Orientation"
    )
    property_type_id = fields.Many2one("estate.property.type",string="Property Type")