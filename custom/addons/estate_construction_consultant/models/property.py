from odoo import models, fields, api

class Property(models.Model):
    _name = 'estate.property'
    _description = 'Property'
    name = fields.Char(string='Name', required=True)
    type = fields.Selection([
        ('house', 'House'),
        ('apartment', 'Apartment'),
    ], string='Type', required=True)
    price = fields.Float(string='Price', required=True)
    area = fields.Float(string='Area', required=True)
    location = fields.Char(string='Location', required=True)
    description = fields.Text(string='Description')
    state = fields.Selection([
        ('new', 'New'),
        ('offer_received', 'Offer Received'),
        ('offer_accepted', 'Offer Accepted'),
        ('sold', 'Sold'),
        ('canceled', 'Canceled'),
    ], string='State', default='new')
    date_available = fields.Date(string='Date Available')
    
