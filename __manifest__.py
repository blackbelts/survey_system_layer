# -*- coding: utf-8 -*-
{
    'name': "Survey System Layer",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'surveillance',

    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','survey_system'],

    # always loaded
    'data': [
        # 'security/security.xml',
        'security/ir.model.access.csv',
        'views/all_lab_results.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
