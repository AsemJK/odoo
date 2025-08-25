from odoo import models
class BasicCheat(models.Model):
    _name = 'basic.cheat'
    def __init__(self):
        pass
    def cheat(self):
        print('cheat')
    def cheat2(self):
        print('cheat2')