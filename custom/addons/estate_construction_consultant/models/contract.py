from odoo import models, fields, api

class Contract(models.Model):
    _name = 'estate.contract'
    _description = 'Contract'
    name = fields.Char(string='Name', required=True)
    date = fields.Date(string='Date', required=True)
    party_id = fields.Many2one('res.partner', string='Party', required=True)
    contact_name = fields.Char(string='Contact Name', required=True)
    contact_number = fields.Char(string='Contact Number', required=True)
    contact_type = fields.Selection([
        ('client', 'Client'),
        ('agent', 'Agent'),
        ('consultant', 'Consultant'),
    ], string='Contact Type', required=True)
    email = fields.Char(string='Email', required=True)
    engineer_signature = fields.Char(string='Engineer Signature', required=True)
    client_signature = fields.Char(string='Client Signature', required=True)
    date_signed = fields.Date(string='Date Signed', required=True)
    date_confirmed = fields.Date(string='Date Confirmed', required=True)
    active = fields.Boolean(string='Active', default=True)

