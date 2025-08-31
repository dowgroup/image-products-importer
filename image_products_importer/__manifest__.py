{
    'name': 'Bulk Image Importer',
    'version': '1.0',
    'summary': 'Bulk import product images by matching filenames to product references, names, or barcodes.',
    'category': 'Inventory',
    'author': 'Dow Group',
    'depends': ['product', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/image_import_wizard_views.xml',
        'static/description/index.html',  # Add this if you have the description HTML file
        'static/description/Odoo app thumbnail.png',  # Your thumbnail image for the module
    ],
    'license': 'OPL-1',
    'installable': True,
    'application': True,
    'support': '',  # Add your support email here
    'website': '',  # Add your company website here
    'description': """Bulk Image Importer module for Odoo allows you to easily import product images
                      by matching filenames to product references, names, or barcodes. The app supports
                      case insensitivity, ignores dashes and underscores, and processes images in batches 
                      for smoother operation.""",
    'icon': 'static/description/module icon.png',  # Placeholder for your module icon (create and add this file)
}
