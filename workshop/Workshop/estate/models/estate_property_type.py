from odoo import api, models, fields

class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Estate Property types'
    
    name = fields.Char(required=True)