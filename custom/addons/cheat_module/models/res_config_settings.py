from odoo import _,models,fields,api

class ResCompany(models.Model):
    _inherit = 'res.company'
    cheat_setting = fields.Boolean(string='Cheat setting')

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    cheat_setting = fields.Boolean(readonly=False,related='company_id.cheat_setting')