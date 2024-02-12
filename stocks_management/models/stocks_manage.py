from odoo import models,fields

class StocksManagement(models.Model):
    _name = "stocks.manage"
    _description = "Stocks management system"

    name = fields.Char(default="Unknown")
    description = fields.Char(string='Description')
    current_price=fields.Float(required=True)
    sector=fields.Selection(
        string='sector',
        selection=[('estate','Estate'),('it','IT'),('agriculture','Agriculture')]
    )
    high_price=fields.Float(required=True)
    low_price=fields.Float(required=True)
    all_time_high=fields.Float(required=True)
    all_time_low=field.Float(required=True)


