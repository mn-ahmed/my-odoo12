# -*- encoding: utf-8 -*-

{
    "name" : "Tunisia - Accounting",
    "version" : "1.0",
    "author" : "Ahmed Mnasri",
'category': 'Localization',
    "website": "http://www.lafirmedecommerce",
    "category" : "Localization/Account Charts",
    "description": """
This is the base module to manage the accounting chart for Tunisia.
=================================================================
""",

    "depends" : ['base','account'],
    "init_xml" : [],
    "data" : [
        'plan_comptable_general.xml',
        'l10n_tn_tax.xml',
        'account_chart_template_data.xml',
		     ],
    "auto_install": False,
    "installable": True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
