from odoo import models,fields

class StocksManageTransaction(models.Model):
    _name="stocks.manage.transaction"
    _description="Transaction"

    transaction_type= fields.Selection(string='Transaction Type',
    selection=[('buy', 'Buy'), ('sell', 'Sell')], 
    required=True)
    transaction_price=fields.Float(string='Transaction price',required=True)
    transaction_date=fields.Date(string='Transaction Date',required=True)
    holding_id=fields.Many2one('stocks.manage.holding',string='holding',required=True)