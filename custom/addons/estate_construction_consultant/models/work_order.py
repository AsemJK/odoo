from odoo import api,fields,models

class WorkOrder(models.Model):
    _name = 'work.order'
    _description = 'Work Order'
    name = fields.Char(string='Work Order Name',required=True)
    date = fields.Date(string='Date',required=True)
    partner_id = fields.Many2one('partner')
    project_id = fields.Many2one('project.project', string='Project',required=True)
    contact_name = fields.Char(string='Contact Name')
    contact_number = fields.Char(string='Contact Number')
    contact_type = fields.Selection([
        ('client', 'Client'),
        ('agent', 'Agent'),
        ('consultant', 'Consultant'),
    ], string='Contact Type')
    email = fields.Char(string='Email')
    engineer_signature = fields.Char(string='Engineer Signature')
    client_signature = fields.Char(string='Client Signature')
    date_signed = fields.Date(string='Date Signed')
    date_confirmed = fields.Date(string='Date Confirmed')
    active = fields.Boolean(string='Active', default=True)
}