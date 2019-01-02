# -*- coding: utf-8 -*-
from openerp import api, fields, models


class SystemParameter(models.Model):
    _inherit = 'ir.config_parameter'

    show_customer_branding_help = fields.Boolean(string='Show Custom Branding Help', compute='_compute_show_help',
                                                 help='Used to decide if we are going to show a help message to the user or not related to custom branding.')

    @api.multi
    @api.depends('key')
    def _compute_show_help(self):
        for parameter in self:
            parameter.show_customer_branding_help = parameter.key == 'blue_custom_branding.addon_path'
