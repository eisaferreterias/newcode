# -*- coding: utf-8 -*-
#################################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2018-today Ascetic Business Solution <www.asceticbs.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#################################################################################
from odoo import api, fields, models, _
from datetime import date

class SaleOrder(models.Model):
    _inherit = "sale.order"

    date = fields.Date()
    recipients_of_email = fields.Many2many(comodel_name='res.partner',relation='customer',column1='partner_id',column2='partner_name',string = "Recipients of the Email")
    subject = fields.Text('Subject')
    email_content = fields.Text('Email Content')

    @api.model
    def send_email_from_customer(self):
        today_date = date.today()
        obj = self.env['sale.order'].search([('state','in',('sale','done')),('date','=',today_date)])
        if obj:
            current_login_user = self.env.user
            for order in obj:
                email_to = []
                for record in order.recipients_of_email:
                    if record.email:
                        email_to.append(record)

                if email_to:
                    mail={
                          'subject'       : order.subject,
                          'email_from'    : order.partner_id.email,
                          'recipient_ids' : [(6,0,[v.id for v in email_to])],
                          'body_html'     : order.email_content,                  
                         }

                mail_create = current_login_user.env['mail.mail'].create(mail)
                if mail_create:
                    mail_create.send()
                    self.mail_id = mail_create
