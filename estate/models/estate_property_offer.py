from odoo import fields,models,api
from datetime import timedelta

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate Property Offer"

    _sql_constraints = [
        (
            "check_price",
            "CHECK(price > 0)",
            "The offer price must be strictly positive."
        ),
    ]
    validity = fields.Integer(default = 7)
    date_deadline = fields.Date(
        compute="_compute_date_deadline",
        inverse="_inverse_date_deadline"
    )

    price = fields.Float(required = True)
    status = fields.Selection(
        [
            ('accepted' , 'Accepted'),
            ('rejected' ,  'Rejected'),
        ],
        copy=False,
    )
    property_id = fields.Many2one("estate.property" , required = True)
    partner_id = fields.Many2one("res.partner" , required = True)


    @api.depends("validity", "create_date")
    def _compute_date_deadline(self):
        for record in self:
            create_date = record.create_date or fields.Date.today()
            record.date_deadline = create_date + timedelta(days=record.validity)

    def _inverse_date_deadline(self):
        for record in self:
            create_date = record.create_date or fields.Date.today()
            record.validity = (record.date_deadline - create_date.date()).days

    def action_accept(self):
        for record in self:
            record.status = "accepted"
            record.property_id.buyer_id = record.partner_id
            record.property_id.selling_price = record.price
        return True

    def action_refuse(self):
        for record in self:
            record.status = "rejected"
        return True