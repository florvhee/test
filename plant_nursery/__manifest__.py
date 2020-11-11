{
    'name': 'Plant Nursery',
    'version': '1.1',
    'category': 'Tools',
    'summary': 'Plants and customers management',
    'depends': ['web'],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/nursery_views.xml',
    ],
    'demo': [
        'data/demo.xml',
    ],
    'css': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}