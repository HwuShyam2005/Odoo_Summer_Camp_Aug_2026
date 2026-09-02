from odoo import api, models, fields

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Real Estate Properties'
    
    name = fields.Char(required=True)
    location = fields.Text()
    bedrooms = fields.Integer()
    expected_price = fields.Float()
    selling_price = fields.Float()
    living_area = fields.Integer()
    has_garden = fields.Boolean()
    garden_area = fields.Integer()