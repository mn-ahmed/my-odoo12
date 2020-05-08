# -*- encoding: utf-8 -*-

from odoo import models, fields, api

class ResPartner(models.Model):

    _inherit = 'res.partner' 
    #Do not touch _name it must be same as _inherit
    #_name = 'res.partner' 

    cin_passport = fields.Char('CIN ou Passport :', size=64)
    permis = fields.Char('Permis N° :')
    date_permis = fields.Date('Date')
    date = fields.Date('Date :')
    

