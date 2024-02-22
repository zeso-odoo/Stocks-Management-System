{
    'name':'STOCKS',
    'version':'1.0',
    'summary':'Manage your stocks with us',
    'description':'We provide best management software for your stocks',
    # 'website':'https://www.odoo.com/app/stocks',
    'depends':[
        'base'
    ],
    'data':[
        'security/ir.model.access.csv',
        
        'views/stocks_manage_portfolio_views.xml',
        'views/stocks_manage_holding_views.xml',
        'views/stocks_manage_transaction_views.xml',
        'views/stocks_manage_user_views.xml',
        'views/stocks_manage_stocks_views.xml',
        'views/stocks_menus.xml',
    ],
    'installable':True,
    'application':True
}