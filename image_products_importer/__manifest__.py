{
    'name': 'Image Products Importer',
    'version': '1.0',
    'summary': 'Bulk import images products  by matching filenames to product internal references, names, or barcodes.',
    'category': 'Inventory',
    'author': 'Dow Group',
    'depends': ['product', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/image_import_wizard_views.xml',
    ],
    'installable': True,
    'application': True,
}
