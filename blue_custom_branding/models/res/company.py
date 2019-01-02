# -*- coding: utf-8 -*-
import os
from odoo import api, fields, models, addons
from odoo.addons.blue_custom_branding.helpers.less import write_less, write_bootswatch_less, combine_bootswatch_less, combine_variables_less


class Company(models.Model):
    """
    Inherit the Company model to add the ability to select theme colors for specific areas in Odoo.
    """
    _inherit = "res.company"

    override_home = fields.Boolean('Override Dashboard Background', default=True,
                                   help='If checked, this will override the dashboard background with the Info Theme Color')
    theme_color_primary = fields.Char(string='Primary Theme Color', default='337ab7')
    theme_color_success = fields.Char(string='Success Theme Color', default='5cb85c')
    theme_color_info = fields.Char(string='Info Theme Color', default='5bc0de')
    theme_color_warning = fields.Char(string='Warning Theme Color', default='f0ad4e')
    theme_color_danger = fields.Char(string='Danger Theme Color', default='d9534f')
    can_change_theme = fields.Boolean(string='Can Change Theme', compute='_compute_can_change_theme', help='Sets if the correct system parameters are setup.')

    @api.multi
    def write(self, vals):
        """
        Inherit `super` to change theme colors by updating .less files.
        :param vals:
        :return: super.write
        """
        res = super(Company, self).write(vals)
        self.with_context({'noreturn': True}).build_theme()
        return res

    @api.multi
    def build_theme(self):
        write_less(self.env)
        write_bootswatch_less(self.env)
        combine_bootswatch_less(self.env)
        combine_variables_less(self.env)

        if not self.env.context.get('noreturn', False):
            return {'type': 'ir.actions.client', 'tag': 'reload'}

    @api.model
    def _setup_parameters(self):
        """
        Setup the parameters required for this module. We do not need to worry about this
        function running multiple times automatically or on an interval. If the users change paths of the module,
        then they will need to manually set the system parameter or update this module.

        :return: ir.config_parameter The parameter that was either updated or created.
        """
        parameter_pool = self.env['ir.config_parameter']
        existing_parameter = parameter_pool.search([('key', '=', 'blue_custom_branding.addon_path')], limit=1)

        if existing_parameter:
            existing_parameter.unlink()
        return parameter_pool.create({'key': 'blue_custom_branding.addon_path',
                                      'value': self._get_addon_path()})

    @api.model
    def _default_less(self):
        """
        Generate defaults for the auto loaded files so that the module does not crash
        immediately on install / update.

        :return: None
        """
        addon_path = self._get_addon_path()

        try:
            with open("{}/static/src/less/bootswatch.less".format(addon_path), "w+") as bootswatch_file:
                bootswatch_file.write("")
            with open("{}/static/src/less/variables.less".format(addon_path), "w+") as variables_file:
                variables_file.write("")
        except Exception as e:
            pass

    @api.multi
    def _compute_can_change_theme(self):
        for company in self:
            company.can_change_theme = bool(self.env['ir.config_parameter'].get_param('blue_custom_branding.addon_path', False))

    def _get_addon_path(self):
        """
        Get the path on the server to the source code for this addon.

        :return: str
        """
        param_addon_path = self.env['ir.config_parameter'].get_param('blue_custom_branding.addon_path', False)
        if param_addon_path:
            return param_addon_path
        return os.path.dirname(os.path.abspath(addons.blue_custom_branding.__file__))
