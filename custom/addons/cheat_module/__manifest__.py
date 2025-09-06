{
    'name': 'Cheat Module',
    'version': '18.0.1.0.0',
    'author': 'JKa',
    'summary': 'Cheat Module',
    'description': 'Cheat Module',
    'depends': ['base','base_setup'],
    'category': 'Tools',
    'data': [
        'security/ir.model.access.csv',
        'views/cheat_view.xml',
        'views/res_config_settings_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    "license": "AGPL-3",
}