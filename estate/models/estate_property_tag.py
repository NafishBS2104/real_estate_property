from odoo import models, fields


class EstatePropertyTag(models.Model):
    _name='estate.property.tag'
    _description='Real Estate Property Tag'
    _order="name"

    name=fields.Char(required=True, string="Name")
    color=fields.Integer()
    _sql_constraints = [
        (
            'check_name_unique',
            'unique(name)',
            'Property Tag Name Must Be Unique'
        )
    ]
