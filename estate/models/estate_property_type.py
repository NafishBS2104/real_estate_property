from odoo import models, fields


class EstatePropertyType(models.Model):
    _name='estate.property.type'
    _description='Real Estate Property Type'
    _order="name"

    name=fields.Char(required=True, string="Name")
    sequence = fields.Integer('Sequence', default=1, help="Used to order stages. Lower is better.")
    property_ids = fields.One2many("estate.property", "property_type_id")
    _sql_constraints = [
        (
            'check_name_unique',
            'unique(name)',
            'Property Name Must Be Unique'
        )
    ]
