from odoo import api,models,fields
from odoo.exceptions import UserError

class FreelanceProjects(models.Model):
    _name = 'freelance.project'
    _description = 'freelance projects'
    
    name = fields.Char(required = True)
    description = fields.Text()
    price = fields.Float()
    state = fields.Selection(selection=[('open','open'),('progress','In Progress'),('completed','Completed')], default = 'open')
    client_id = fields.Many2one('res.partner', string = 'Client')
    freelancer_id = fields.Many2one('res.partner', string = 'Freelancer')
    category_id = fields.Many2one('project.category', string = 'Project Category')
    project_id = fields.Many2one('project.project', copy = False)

    def claim_project(self):
        self.ensure_one()
        for record in self:
            if not record.project_id:
                project = self.env['project.project'].create({
                    'name': record.name,
                    'partner_id': record.client_id
                })
                record.project_id = project.id
            if not record.freelancer_id:
                raise UserError('Please assign this project to a freelancer first')
                record.state = 'progress'

    def complete_project(self):
        for record in self:
            if record.state == 'open' and not record.freelancer_id:
                raise UserError('Please assign this project to a freelancer first')
            else:
                record.state = 'completed'