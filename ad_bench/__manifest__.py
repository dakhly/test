

{
    'name': 'Bench Financial Report',
    'version': '15.0.1.0.0',
    'category': 'Accounting',
    'author': 'Ahmed Dakhly',
    'sequence': '-100',
    'summary': 'Financial Management',
    'description': """
This module contains all the common features of Financial Reports.
    """,
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/client_view.xml',
    ],
    'demo': [],
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
