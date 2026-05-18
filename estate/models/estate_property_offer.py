from odoo import fields,models

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate Property Offer"

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
