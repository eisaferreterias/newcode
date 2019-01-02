import json
from odoo import http
from odoo.addons.blue_custom_branding.helpers.less import write_less


class BlueTheme(http.Controller):

    @http.route('/blue_custom_branding/static/src/less/variables.less.css', type='http', auth='public')
    def handler(self, **kwargs):
        less_string = write_less(
            http.request.env.user.company_id, http.request.env)
        bootswatch_less = write_bootswatch_less(
            http.request.env.user.company_id, http.request.env)
        if less_string:
            return http.request.make_response(less_string)

    @http.route('/blue_custom_branding/cssClassname', type='http', auth='public')
    def userinfo_handler(self):
        company_id = http.request.env.user.company_id.id
        dbname = http.request.env.cr.dbname
        className = "blue_theme__%s__%d" % (dbname, company_id)
        return http.request.make_response(json.dumps({
            'className': className,
        }))
