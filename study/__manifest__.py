# -*- coding: utf-8 -*-
{
    'name': "study",

    'summary': """
        Pscloud 培训""",

    'description': """
        学生管理系统
    """,

    'author': "Pscloud",
    'website': "http://www.mypscloud.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'tools',
    'version': '12.0.1',
   # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
#         'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
#         'demo/demo.xml',
    ],
}
