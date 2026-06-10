from odoo import models,fields


class ResUsers(models.Model):
    _inherit = "res.users"


    property_id = fields.One2many(
        "estate.property",
        "user_id",
        domain=[("state","=","new")]
    )