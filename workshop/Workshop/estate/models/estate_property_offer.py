from odoo import api,models,fields

class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Estate Property Offers'
    
    price = fields.Float()
    partner_id = fields.Many2one('res.partner')
    
    property_id = fields.Many2one('estate.property')