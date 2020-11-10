from odoo import fields, models

def test():
    return 2

class Plants(models.Model):
    _name = 'nursery.plant'
    
    name = fields.Char("Plant Name")
    price = fields.Float(label="Prix")