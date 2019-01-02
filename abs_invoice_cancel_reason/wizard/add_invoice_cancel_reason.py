# -*- coding: utf-8 -*-
#################################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2018-Today Ascetic Business Solution <www.asceticbs.com>
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

from odoo import api,fields,models,_

from odoo import api,fields,models,_
class AddInvoiceCancelReason(models.TransientModel):
    _name="add.invoice.reason"

    invoice_cancel_reason_id = fields.Many2one("invoice.cancel.reason",string= "Invoice Cancellation Reason", required =True, help="This field display reason of invoice cancellation")

    # For adding the reason of cancel invoice on invoices	
    @api.multi
    def cancel_invoice_wizard(self):
        if self.env.context.get('active_model') == 'account.invoice':
            active_model_id = self.env.context.get('active_id')
            invoice_obj = self.env['account.invoice'].search([('id','=',active_model_id)])
            invoice_obj.write({'invoice_cancel_reason_id':self.invoice_cancel_reason_id.id})
            invoice_obj.action_invoice_cancel()
	

	
