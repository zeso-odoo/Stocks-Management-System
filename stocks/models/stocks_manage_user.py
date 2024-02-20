from odoo import models,fields

class StocksManageUser(models.Model):
    _name="stocks.manage.user"
    _description="welcome to the stocks management software"

    name=fields.Char(default='unknown')
    description=fields.Char(string='Description')
    pancard=fields.Char(required=True)
    email=fields.Char(string='email',required=True)
    no_of_stocks=fields.Integer(required=True)
    total_pl=fields.Float(readonly=True,copy=False)