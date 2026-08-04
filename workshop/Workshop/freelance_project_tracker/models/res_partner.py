from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    listed_project_ids = fields.One2many('freelance.project', 'client_id', string='Listed Projects')
    working_project_ids = fields.One2many('freelance.project', 'freelancer_id', string='Working Projects')