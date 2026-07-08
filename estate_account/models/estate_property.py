from odoo import fields, models
from odoo import Command


class EstateProperty(models.Model):
    _inherit = "estate.property"

    def action_sell(self):
        act = super().action_sell()
        self.env["account.move"].create({'partner_id': self.buyer_id.id,
                                         'move_type': 'out_invoice',
                                         "invoice_line_ids": [
                                             Command.create({
                                                 "name": f"{self.name}",
                                                 "quantity": 1,
                                                 "price_unit": self.selling_price * 0.06
                                             }),
                                             Command.create({
                                                 "name": "Administrative Fees",
                                                 "quantity": 1,
                                                 "price_unit": 100
                                             })
                                         ]

                                         })
        print("--------------Sell Confirmed!!!----------------")
        return act