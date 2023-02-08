# -*- coding: utf-8 -*-
###############################################################################

###############################################################################

{
    'name': 'Hiworth EMS Activity',
    'version': '14.0.1.0',
    'license': 'LGPL-3',
    'category': 'Education',
    "sequence": 3,
    'summary': 'Manage Activities',
    'complexity': "easy",
    'author': 'Hiworth Solutions',
    'website': 'http://www.hiworthsolutions.com',
    'depends': ['openeducat_core'],
    'data': [
        'security/op_security.xml',
        'security/ir.model.access.csv',
        'data/activity_type_data.xml',
        'wizard/student_migrate_wizard_view.xml',
        'views/activity_view.xml',
        'views/activity_type_view.xml',
        'views/student_view.xml',
        'menus/op_menu.xml'
    ],
    'demo': [
        'demo/activity_demo.xml',
    ],
    'images': [
        'static/description/openeducat_activity_banner.jpg',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
