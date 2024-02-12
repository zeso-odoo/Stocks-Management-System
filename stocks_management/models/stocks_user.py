from odoo import models,fields

class StocksManagement(models.Model):
    _name='stocks.user'
    _description='welcome to the stock management system'

    name = fields.Char(default="Unknown")
    description = fields.Char(string='Description')
    pancard=fields.Char(required=True)
    Email=fileds.Char(string='user@gmail.com',required=True)
    no_of_stocks=fields.Integer(required=True)
    total_PL=fileds.Float(readonly=True,copy=False)
    