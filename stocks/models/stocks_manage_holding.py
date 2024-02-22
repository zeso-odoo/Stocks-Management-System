from odoo import models,fields,api

class StocksManageHolding(models.Model):
    _name="stocks.manage.holding"
    _description="Stocks Holding"

    name=fields.Char(required=True)
    portfolio_id=fields.Many2one('stocks.manage.portfolio',string='portfolio',required=True)
    quantity=fields.Float(string='Quantity',required=True)
    purchase_price=fields.Float(string='Purchase Price',required=True)
    purchase_date=fields.Date(string='Purchase Date',required=True)
    total_amount=fields.Float(compute='_compute_total_amount')
    user_id=fields.Many2one('stocks.manage.user',string='user',store=True)
    portfolio_ids=fields.Many2one('stocks.manage.portfolio',string='Portfolios',required=True,ondelete='cascade')

    @api.depends('quantity','purchase_price')
    def _compute_total_amount(self):
        for record in self :
            record.total_amount=record.quantity * record.purchase_price
    
