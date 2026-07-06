from odoo import models, fields


class EstatePropertyType(models.Model):
    _name='estate.property.type'
    _description='Real Estate Property Type'

    name=fields.Char(required=True, string="Name")
    _sql_constraints = [
        (
            'check_name_unique',
            'unique(name)',
            'Property Name Must Be Unique'
        )
    ]
