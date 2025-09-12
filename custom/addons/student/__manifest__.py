# -*- coding: utf-8 -*-
{
    'name': "student",

    'summary': "Student Module of SW LMS",

    'description': """
This is a part from LMS
    """,

    'author': "Asem.Smartsware",
    'website': "https://www.smartsware.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'LMS',
    'version': '18.0.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

