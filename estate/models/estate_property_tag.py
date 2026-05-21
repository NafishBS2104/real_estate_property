from odoo import fields,models

class EstatePropertyTag(models.Model):
    _name="estate.property.tag"
    _description = "Estate Property Tags"

    _sql_constraints = [
        (
            "unique_name_unique",
            "UNIQUE(name)",
            "The property tag name must be unique."
        ),
    ]

    name = fields.Char(required=True)