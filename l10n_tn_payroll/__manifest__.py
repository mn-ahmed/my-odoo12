
{
'name': 'Tunisia-payroll',
'category': 'Localization/Payroll',
'author': 'Ahmed Mnasri',
'website': '',
"category" : "Localization",
'version': '1.0',
'depends': ['hr_payroll'],


'description': """Tunisian Payroll Rules.
======================
   Gestion de la Paie Tunisienne:    
    - Gestion des employés.
    - Gestion des contrats.
    - Configuration et paramètrage
            * Les rubriques de paie :primes,indemnités,avantages,déductions,...
            * Les rubriques cotisable ,imposable , soumise à la prime d'ancienneté  ...
            * Les cotisations : cotisations salariales et patronales CNSS,Mutuelle...
            * Barème de la prime d'ancienneté,cotisations CNSS ...       
    - Calcul de paie selon les normes tunisien : calcul automatique de la prime d'ancienneté,heures supplémentaire,cotisations salariales et patronales,...
    - Gestion des congés  :Calcul automatique des congés non payés à partir du module hr_holidays
    - Comptabilisation de la paie :  configuration des comptes de credit et de débit
    - Reporting : les  bulletins de paie,journale de paie ,Ordres de virement ...
    """,

'data': [
	'views/l10n_tn_payroll_view.xml',
    'data/l10n_tn_payroll_data.xml',
    #'report/report.xml',
    #'report/report_l10n_tn_fiche_paye.xml',
        ],
'auto_install': False,
'installable': True,
'application': False,
}
