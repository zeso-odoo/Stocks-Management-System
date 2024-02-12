{
    'name': 'Stocks_Management',
    'version': '1.0',
    'summary': 'Manage your stocks',
    'description': 'We provide all kind of facility to manage your stocks ',
    'website': 'https://www.odoo.com/app/stocks_managemnet',
    'depends': [
        'base'
    ],
    'data': [
    
        'security/ir.model.access.csv',
        'views/stocks_manage_views.xml',
        'views/stocks_management_menus.xml'
        
    ],
    'installable': True,
    'application': True
}