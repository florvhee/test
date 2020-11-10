from odoo import fields, models


class Plants(models.Model):
    _name = 'nursery.plant'
    
    name = fields.Char("Plant Name")
    price = fields.Float(label="Prix")