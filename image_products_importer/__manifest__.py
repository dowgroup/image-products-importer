{
    'name': 'Bulk Image Importer',
    'version': '1.0',
    'summary': 'Easily bulk import product images by matching filenames to product references, names, or barcodes.',
    'category': 'Inventory',
    'author': 'Dow Group',
    'website': 'https://www.dowgroup.com',
    'support': 'info@dowgroup.com',
    'depends': ['product', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/image_import_wizard_views.xml',
    ],
    'license': 'OPL-1',
    'installable': True,
    'application': True,
    'description': """
Bulk Image Importer module for Odoo allows you to easily import product images
by matching filenames to product references, names, or barcodes. The app supports
case insensitivity, ignores dashes and underscores, and processes images in batches 
for smoother operation.
    """,
    'images': [
        'static/description/odoo_app_thumbnail.png',
        'static/description/odoo image preview.svg',
        'static/description/odoo image preview(2).svg',
        'static/description/odoo image preview(3).svg',
        'static/description/odoo image preview(4).svg',
        'static/description/odoo image preview(5).svg',
        'static/description/odoo image preview(6).svg',
    ],
    'icon': 'static/description/module_icon.png',
    'price': 100.0,
    'currency': 'USD',
}
