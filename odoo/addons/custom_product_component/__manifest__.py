{
    'name': 'Product Component',
    'version': '1.0',
    'summary': 'Adds custom fields to product',
    'depends': [
        'base', 'product', 'stock', 'sale',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/chemical_component_menu.xml',
        'views/product_component_menu.xml',
        'views/product_template_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
}