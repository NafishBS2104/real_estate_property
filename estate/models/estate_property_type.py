from odoo import fields,models

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Estate Property Types"

    _sql_constraints = [
        (
            "unique_name",
            "UNIQUE(name)",
            "The property type name must be unique"
        ),
    ]

    name = fields.Char(required=True)