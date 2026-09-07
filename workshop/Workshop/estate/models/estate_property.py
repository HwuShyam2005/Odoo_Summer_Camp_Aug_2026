from odoo import api, models, fields
from odoo.exceptions import UserError

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
    
    state = fields.Selection(selection=[('new','New'), ('offer_accepted','Offer Accepted'), ('sold','Sold'), ('cancelled',' Cancelled')], default='new')
    
    def sell_property(self):
        for record in self:
            if record.state == 'cancelled':
                raise UserError('you cannot sell a cancelled property')
            else:
                record.state = 'sold'
                
    def cancel_property(self):
        for record in self:
            if record.state == 'sold':
                raise UserError('you cannot cancel a sold property')
            else:
                record.state = 'cancelled'
                