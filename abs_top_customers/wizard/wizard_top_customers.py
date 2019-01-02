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

from odoo import api, fields, models,_
from datetime import datetime
from odoo.exceptions import ValidationError

# wizard 
class TopCustomers(models.TransientModel):
    _name = "top.customers"

    date_from = fields.Date('From Date')
    date_to = fields.Date('To Date')

    @api.onchange('date_to')
    def onchange_date_to(self):
        for record in self:
            if record.date_to < record.date_from:
                raise ValidationError("Please select right date")
            else:
                pass

    @api.multi
    def top_customers(self):
        customer_list = []
        top_customer_list = []
        top_customer = self.env['top.customer']
        sale_order_ids = self.env['sale.order'].search([('confirmation_date','<=',self.date_to),('confirmation_date','>=',self.date_from),('state','in',['sale','done'])])
        if sale_order_ids:
            for order in sale_order_ids:
                total_amount = 0
                if order.partner_id not in customer_list:
                    customer_list.append(order.partner_id)
                    for customer in sale_order_ids:
                        if order.partner_id == customer.partner_id:
                            total_amount = total_amount + customer.amount_total
                    customer_dict = {'customers' : order.partner_id.id, 'amount' : total_amount}
                    top_customer_id = top_customer.create(customer_dict)
                    if top_customer_id:
                       top_customer_list.append(top_customer_id)

        return {
            'name': _('Top Customers'),
            'type': 'ir.actions.act_window',
            'domain': [('id','in',[x.id for x in top_customer_list])],
            'view_mode': 'tree',
            'res_model': 'top.customer',
            'view_id': False,
            'action' :'view_customers_tree',
            'target' : 'current'
        }
