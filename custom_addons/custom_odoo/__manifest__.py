{
    'name': 'custom_odoo',
    'version': '1.0',
    'summary': 'New Custom Addons',
    'author': 'sp',
    'website': 'www.google.com',
    'category': 'Uncategorized',
    'description': 'Custom Addons',
    'depends': ['sale', 'account'],
    'data': [
        'views/sale_order_view.xml',
        'views/sale_order_report.xml',
        # Add other data files here
    ],
    'installable': True,
}
