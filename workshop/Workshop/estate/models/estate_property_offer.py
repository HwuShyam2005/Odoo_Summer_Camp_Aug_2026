from odoo import api,models,fields
from odoo.exceptions import UserError

class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Estate Property Offers'
    
    price = fields.Float()
    partner_id = fields.Many2one('res.partner')
    
    property_id = fields.Many2one('estate.property') 
    
    state = fields.Selection(selection = [('accepted', 'Accepted'), ('refused', 'Refused')])
    
    def accept_offer(self):
        for record in self:
            if record.property_id.state == 'offer_accepted':
                raise UserError('this property already has an offer accepted')
            elif record.state == 'refused':
                raise UserError('you cannot accept a refused offer')
            else:
                 record.property_id.state = 'offer_accepted'
                 record.property_id.buyer_id = record.partner_id
                 record.property_id.selling_price = record.price
                 record.state = 'accepted'
    
    def refuse_offer(self):
        for record in self:
            if record.state == 'accepted':
                raise UserError('accepted offers cannot be refused')
            else:
                record.state = 'refused'
                

                