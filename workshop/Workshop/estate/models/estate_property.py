from odoo import api, models, fields
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_compare, float_is_zero

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
    
    tag_ids = fields.Many2many('estate.property.tag')
    
    _check_expected_price = models.Constraint('CHECK(expected_price > 0)', 'the expected price must be strictly positive')
    _check_selling_price = models.Constraint('CHECK(selling_price >= 0)', 'the selling price must be strictly positive')

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
    
    @api.constrains('expected_price', 'selling_price')
    def _check_valid_Selling_price(self):
        for record in self:
            if (float_compare(record.selling_price, 0.9 * record.expected_price, precision_digits=2) < 0 and 
                not float_is_zero(record.selling_price, precision_digits=2)):
                raise ValidationError('Selling price must be at least 90% of the expected price')