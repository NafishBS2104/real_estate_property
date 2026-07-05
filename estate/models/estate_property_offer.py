import datetime as dt

from odoo import fields, models,api
from odoo.exceptions import UserError


class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Estate Property Offers Model'

    price = fields.Float()
    _order = "price desc"
    _sql_constraints = [
        (
            'price',
            'CHECK(price >= 0)',
            'Offer Price Must Be Positive'
        )
    ]
    status = fields.Selection(selection=[
        ('accepted', 'Accepted'),
        ('refused', 'Refused')]
        ,copy=False)
    validity = fields.Integer(default=7)
    partner_id = fields.Many2one('res.partner', required=True, string="Partner ID")
    property_id = fields.Many2one('estate.property', required=True, string="Property ID")
    date_deadline = fields.Date(string="Deadline", compute="_compute_deadline",inverse="_compute_deadline_inverse")
    @api.depends("validity", "create_date")
    def _compute_deadline(self):
        for record in self:
            base_date = record.create_date.date() if record.create_date else fields.Date.today()
            record.date_deadline = base_date + dt.timedelta(days=record.validity)

    @api.depends("validity","create_date")
    def _compute_deadline_inverse(self):
        for record in self:
            base_date = record.create_date.date() if record.create_date else fields.Date.today()
            record.validity = (record.date_deadline - base_date).days

    def action_accept(self):
        for record in self:
            if record.status == 'refused':
                raise UserError('Cannot Accept Refused Offer')
            record.status = 'accepted'
            record.property_id.buyer_id = record.partner_id
            record.property_id.selling_price = record.price
            record.property_id.state = 'offer_accepted'
        return True

    def action_refuse(self):
        for record in self:
            if record.status == 'accepted':
                raise UserError('Cannot refuse accepted offer')
            record.status = 'refused'
        return True

    @api.model_create_multi
    def create(self, data_list):
        print(f"Data List {data_list}")
        for data in data_list:
            property_id = data.get('property_id')
            property_rec = self.env['estate.property'].browse(property_id)
            property_rec.state = 'offer_received'
        return super(EstatePropertyOffer,self).create(data_list)