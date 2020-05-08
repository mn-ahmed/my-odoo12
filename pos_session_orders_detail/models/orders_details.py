# -*- coding: utf-8 -*-
#################################################################################
# Author      : Acespritech Solutions Pvt. Ltd. (<www.acespritech.com>)
# Copyright(c): 2012-Present Acespritech Solutions Pvt. Ltd.
# All Rights Reserved.
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#################################################################################

from odoo import api, models, fields


class PosSession(models.Model):
    _inherit = 'pos.session'


    #orders_ids = fields.One2many('pos.order', 'session_id',  string='Orders')
    orders_ids = fields.One2many(comodel_name="pos.order", inverse_name="session_id", string="Pos Orders Information")



class PosConfig(models.Model):
    _inherit = 'pos.config'

    session_ids = fields.One2many('pos.session', 'config_id', string='Sessions')
    transaction_cash = fields.Float(compute='_compute_session')


    

    @api.depends('session_ids')
    def _compute_session(self):
        PosSession = self.env['pos.session']
        for pos_config in self:
            session = PosSession.search_read(
                [('config_id', '=', pos_config.id)],# ('state', '=', 'closed')],
                ['cash_register_total_entry_encoding'],
                order="stop_at desc", limit=1)
            if session:
                pos_config.transaction_cash = session[0]['cash_register_total_entry_encoding']
            else:
                pos_config.transaction_cash = 0
             