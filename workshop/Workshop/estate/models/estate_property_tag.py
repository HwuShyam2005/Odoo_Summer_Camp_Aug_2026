from odoo import api, models, fields

class EstatePropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = 'Estate Property tags'
    
    name = fields.Char(required=True)
    color = fields.Integer('color')
    
    _check_unique_tag = models.Constraint('UNIQUE(name)', 'Property tag must be unique')