from odoo import models,fields

class StocksManagement(models.Model):
    _name="stick.manage.transaction"
    
    transaction_type=fields.Selection([('buy','Buy'),('sell','Sell')],string='Transaction Type',required=True)
    transaction_price=fields.Float(string='Transaction price',required=True)
    transaction_date=fields.Date(string='Transaction Date',required=True)