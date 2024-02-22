from odoo import fields,api,models

class StocksManageStocks(models.Model):
    _name='stocks.manage.stocks'
    _description='Stocks management system'

    stocks_name=fields.Char(required=True)
    company_name=fields.Char()
    sector=fields.Selection(copy=False,selection=[('it','IT'),('agriculture','Agriculture'),('medical','Medical'),('real estate','Real Estate')])
    ceo=fields.Char()
    no_of_employee=fields.Integer(required=True) 
    current_price=fields.Float(required=True)
    all_time_high=fields.Float(required=True)
    all_time_low=fields.Float(required=True)
    Company_revenue=fields.Float(required=True)


