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
    property_type_id = fields.Many2one('estate.property.type', string = 'Property Type')
    buyer_id = fields.Many2one('res.partner', string = 'Buyer')
    salesperson_id = fields.Many2one('res.users', string = 'Salesperson', default=lambda self: self.env.user)
    offer_ids = fields.One2many('estate.property.offer', 'property_id')