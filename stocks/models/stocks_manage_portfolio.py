from odoo import models,fields

class StocksManagePortfolio(models.Model):
    _name="stocks.manage.portfolio"
    _description="User portfolio"

    name=fields.Char(required=True)
    user_id=fields.Many2one('res.users',string='user',required=True)
