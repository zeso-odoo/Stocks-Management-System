from odoo import models,fields,api

class StocksManagePortfolio(models.Model):
    _name="stocks.manage.portfolio"
    _description="User portfolio"

    name=fields.Char(required=True)
    total_profit_loss = fields.Float(compute="_compute_total_profit_loss", store=True)
    user_id=fields.Many2one('res.users',string='user',required=True)
    
    # @api.depends('holding_ids')
    # def _compute_total_profit_loss(self):
    #     for rec in self:
    #         print("\n xxxxxxxxxxxxxxxxxxx\n")
    #         total_holdings=sum(rec.portfolio_ids.mapped('holding_ids.total_amount'))
    #         rec.total_profit_loss=total_holdings
            # breakpoint()

    @api.depends('holding_ids.quantity', 'holding_ids.purchase_price')
    def _compute_total_profit_loss(self):
        
        for portfolio in self:
            
            total_value = sum([hld.quantity * hld.purchase_price for hld in portfolio.holding_ids])
            # current_value = sum([hld.quantity * hld.purchase_price_current for hld in portfolio.holding_ids])
            portfolio.total_profit_loss =  total_value
