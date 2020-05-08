# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import odoo.addons.decimal_precision as dp


class HrContract(models.Model):
    _name ='hr.contract'
    _inherit = 'hr.contract'

    nationalite = fields.Char(string="Nationalitie", required=False, )
    qualif = fields.Char(string="Qualification", required=False, )
    niveau = fields.Char(string="niveau", required=False, )
    coef = fields.Char(string="Coefficient", required=False, )


class ResCompany(models.Model):
    _name = 'res.company'
    _inherit = 'res.company'

    plafond_secu = fields.Float(string="Plafond de la Securite Sociale", digits_compute=dp.get_precision('Payroll'))
    nombre_employes = fields.Integer(string="Nombre d\'employes'", required=False, )
    cotisation_prevoyance = fields.Float(string="Cotisation Patronale Prevoyance",  digits_compute=dp.get_precision('Payroll'))
    org_ss = fields.Char(string="Organisme de securite sociale",)
    conv_coll = fields.Char(string="Convention collective", required=False, )

class HrPayslip(models.Model):
    _name = 'hr.payslip'
    _inherit = 'hr.payslip'

    payment_mode = fields.Char('Mode de paiement')


class HrEmployee(models.Model):
    _name = 'hr.employee'
    _inherit = 'hr.employee'

    matricule_cnss = fields.Integer(string="Matricule CNSS", required=False, )
    num_chezemployeur = fields.Integer(string="Numero chez l\'employeur", required=False, )

