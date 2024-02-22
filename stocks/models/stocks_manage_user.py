from odoo import models,fields,api

class StocksManageUser(models.Model):
    _name="stocks.manage.user"
    _description="welcome to the stocks management software"

    name=fields.Char(default='unknown')
    description=fields.Char(string='Description')
    pancard=fields.Char(required=True)
    email=fields.Char(string='email',required=True)
    no_of_stocks=fields.Integer(required=True)
    # portfolio_ids=fields.One2many('stocks.manage.portfolio','user_id',string='Portfolios')
    # holding_id=fields.Many2one('stocks.manage.holding',string='holdings')
    total_profit_loss=fields.Float(string='Total Profit/Loss',compute='_compute_total_profit_loss')
    
    
    # @api.depends('portfolio_ids')
    # def _compute_total_profit_loss(self):
    #     for rec in self:
    #         print("\n xxxxxxxxxxxxxxxxxxx\n")
    #         total_holdings=sum(rec.holding_id.mapped('total_amount'))
    #         rec.total_profit_loss=total_holdings
    #         # breakpoint()