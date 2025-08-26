import random
import string


from odoo import _,models,fields,api
class BasicCheat(models.Model):
    _name = 'basic.cheat'
    char_field = fields.Char(string='Char field',required=True)
    text_field = fields.Text(string='Text field')
    boolean_field = fields.Boolean(string='Boolean field')
    integer_field = fields.Integer(string='Integer field')
    selection_field = fields.Selection(selection=[
        ('1','item1'),
        ('2','item2'),
        ('3','item3'),
    ],string='Selection field')
    computed_field = fields.Boolean(string='Computed field',compute='_my_compute_field',store=True)
    @api.depends('boolean_field')
    def _my_compute_field(self):
        for record in self:
            record.computed_field = record.boolean_field

    def __init__(self):
        pass
    def cheat(self):
        print('cheat')
    def cheat2(self):
        print('cheat2')