from odoo import fields, models,api ,_

class FirstModel(models.Model):
    _name = 'first.model'
    _description = 'First Model'
    name = fields.Char(string='Name')
