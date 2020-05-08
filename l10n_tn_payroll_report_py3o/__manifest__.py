
{
'name': 'Tunisia-payroll-report-py3o',
'category': 'Localization/Payroll',
'author': 'Ahmed Mnasri',
'website': '',
"category" : "Report",
'version': '1.0',
'depends': ['l10n_tn_payroll',
			'report_py3o',
			'report_py3o_fusion_server', 
			'base_usability', ],


'description': """Tunisian Payroll Report .
======================
   Fiche de Paie Tunisienne:    
    
    """,

'data': [
	'report/report.xml',
	'report/salary_advance_structue.xml',
    #'report/report_l10n_tn_fiche_paye.xml',
        ],
'auto_install': False,
'installable': True,
'application': False,
}
