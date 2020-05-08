# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': "TN Invoice Report",

    'summary': """Tunisia based Invoice with Stamp""",

    'description': """
        This module adds a functionality for Tunisia based Invoice like stamp ...
    """,

    'license': 'AGPL-3',

    'author': "	AHMED MNASRI",

    'website': "",

    'category': 'Accounting',
    
    'version': '12.0.0.1.0',

    'depends': ['account',
                'timbre_fiscal',
                ],

    'data': [
        'report/reports.xml',
        'report/invoice_report_template.xml',
        
    ],
    'images': [
    ],

    'installable': True,

    'auto_install': False,

    'application': True,


}
