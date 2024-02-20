from odoo import models,fields

class StocksManageHolding(models.Model):
    _name="stocks.manage.holding"
    _description="Stocks Holding"

    portfolio_id=fields.Many2one('stocks.manage.portfolio',string='portfolio',required=True)
    quantity=fields.Float(string='Quantity',required=True)
    purchase_price=fields.Float(string='Purchase Price',required=True)
    purchase_date=fields.Date(string='Purchase Date',required=True)

    