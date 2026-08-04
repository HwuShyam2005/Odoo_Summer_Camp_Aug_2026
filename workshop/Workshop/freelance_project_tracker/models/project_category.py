from odoo import models,fields

class ProjectCategory(models.Model):
    _name = 'project.category'
    _description = 'Project Categories'
    
    name = fields.Char(required = True)
    
    _check_unique_name = models.Constraint('UNIQUE(name)', 'the project category must be UNIQUE')