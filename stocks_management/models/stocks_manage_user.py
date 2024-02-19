from odoo import models,fields

class StocksManagement(models.Model):
    _name="stocks.manage.user"
    _description="welcome to the stock management system"

    name = fields.Char(default='Unknown')
    description = fields.Char(string='Description')
    pancard=fields.Char(required=True)
    email=fields.Char(string='user@gmail.com',required=True)
    no_of_stocks=fields.Integer(required=True)
    total_PL=fields.Float(readonly=True,copy=False)
    