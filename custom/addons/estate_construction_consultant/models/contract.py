from odoo import _ ,models, fields, api

class Contract(models.Model):
    _name = 'contract'
    _description = 'Contract'
    name = fields.Char(string='Contract Name',required=True)
    date = fields.Date(string='Date',required=True)
    party_id = fields.Many2one('res.partner', string='Party',required=True)
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

