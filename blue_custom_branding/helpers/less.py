# -*- coding: utf-8 -*-
import os
import re
import logging

_logger = logging.getLogger(__name__)


def write_less(env):
    """
    Write the company theme details as less variables in a database-specific less file.

    :raise Exception: if there is an error opening or writing to files
    :return: None
    """
    dbname = env.cr.dbname
    addon_path = env['ir.config_parameter'].get_param(
        'blue_custom_branding.addon_path')
    fname = "{}/static/src/less/variables_{}.less".format(addon_path, dbname)

    companies = env['res.company'].search([])
    try:
        f = open(fname, "w")
        for company in companies:
            less_string = """
                     @brand-primary-{database}-{company_id}: #{primary};
                     @brand-success-{database}-{company_id}: #{success};
                     @brand-info-{database}-{company_id}: #{info};
                     @brand-warning-{database}-{company_id}: #{warning};
                     @brand-danger-{database}-{company_id}: #{danger};
                     @navbar-default-bg-{database}-{company_id}: @brand-primary-{database}-{company_id};  // @brand-primary
                     @navbar-inverse-bg-{database}-{company_id}: @brand-info-{database}-{company_id};     // @brand-info
                     @label-primary-bg-{database}-{company_id}: @brand-primary-{database}-{company_id};  // @brand-primary
                     """.format(
                primary=company.theme_color_primary,
                success=company.theme_color_success,
                info=company.theme_color_info,
                warning=company.theme_color_warning,
                danger=company.theme_color_danger,
                database=dbname,
                company_id=company.id, )
            f.write(less_string)
        f.close()
    except Exception as e:
        _logger.debug('Theme error writing to file : %s' % e)


def write_bootswatch_less(env):
    """
    Write the company theme details as bootswatch-compatible less
    variables in a database-specific bootswatch less file.

    :raise Exception: if there is an error opening or writing to files
    :return: None
    """
    dbname = env.cr.dbname
    addon_path = env['ir.config_parameter'].get_param(
        'blue_custom_branding.addon_path')
    fname = "{}/static/src/less/bootswatch_{}.less".format(addon_path, dbname)

    companies = env['res.company'].search([])
    try:
        f = open(fname, "w")
        for company in companies:
            # &#123; = { &#125; = }  // They get converted back when the files are merged.
            css_string = """
              body.blue_theme__{database}__{company_id} a.oe_menu_toggler:hover,
              body.blue_theme__{database}__{company_id} a.oe_menu_toggler:focus &#123;
                background-color: darken(@brand-primary-{database}-{company_id}, 10%) !important;
              &#125;

              /* main navigation bar */
              body.blue_theme__{database}__{company_id} a.oe_menu_toggler,
              body.blue_theme__{database}__{company_id} #oe_main_menu_navbar,
              body.blue_theme__{database}__{company_id} .o_main_navbar &#123;
                background-color: @brand-primary-{database}-{company_id} !important ;
                border-color: @brand-primary-{database}-{company_id};
              &#125;

              body.blue_theme__{database}__{company_id} a.o_menu_toggle:hover,
              body.blue_theme__{database}__{company_id} a.o_menu_toggle:focus,
              body.blue_theme__{database}__{company_id} button.o_mobile_menu_toggle:hover,
              body.blue_theme__{database}__{company_id} button.o_mobile_menu_toggle:focus,
              body.blue_theme__{database}__{company_id} .o_main_navbar ul.o_menu_systray li > a:hover,
              body.blue_theme__{database}__{company_id} .o_main_navbar ul.o_menu_systray li > a:focus &#123;
                background-color: darken(@brand-primary-{database}-{company_id}, 10%) !important;
              &#125;

              @media (min-width: @grid-float-breakpoint-max) &#123;
                  body.blue_theme__{database}__{company_id} body .o_main_navbar > ul > li > a[data-toggle="collapse"]:hover,
                  body.blue_theme__{database}__{company_id} body .o_main_navbar > ul > li > a[data-toggle="collapse"]:focus &#123;
                    background-color: @brand-info-{database}-{company_id} !important;
                  &#125;
              &#125;

              body.blue_theme__{database}__{company_id} .o_list_view tfoot &#123;
                background-color: @brand-primary-{database}-{company_id};
              &#125;
              body.blue_theme__{database}__{company_id} .o_searchview .o_searchview_facet .o_searchview_facet_label &#123;
                background-color: @brand-primary-{database}-{company_id};
              &#125;
              body.blue_theme__{database}__{company_id} .o_form_view.o_form_editable .o_form_field .o_list_view td.o_readonly &#123;
                background-color: transparent;
              &#125;
              body.blue_theme__{database}__{company_id} .navbar &#123;
                &-default &#123;
                  .badge &#123;
                    background-color: #fff;
                    color: @navbar-default-bg-{database}-{company_id};
                  &#125;
                &#125;
                &-inverse &#123;
                  .badge &#123;
                    background-color: #fff;
                    color: @navbar-inverse-bg-{database}-{company_id};
                  &#125;
                &#125;
              &#125;

              body.blue_theme__{database}__{company_id} .o_form_view .o_notebook > ul.nav-tabs > li.active > a,
              body.blue_theme__{database}__{company_id} .o_form_view .o_notebook > ul.nav-tabs > li.active > a:hover,
              body.blue_theme__{database}__{company_id} .o_form_view .o_notebook > ul.nav-tabs > li.active > a:focus,
              body.blue_theme__{database}__{company_id} .o_form_view .o_notebook > ul.nav-tabs > li.active > a:active &#123;
                color: @brand-primary-{database}-{company_id};
              &#125;

              /* For the community version */
              /* This gets the developer mode button. */
              body.blue_theme__{database}__{company_id} .label-primary:hover,
              body.blue_theme__{database}__{company_id} .label-primary:focus,
              body.blue_theme__{database}__{company_id} .label-primary &#123;
                background-color: darken(@brand-primary-{database}-{company_id}, 10%) ;
              &#125;

              body.blue_theme__{database}__{company_id} .o_main_navbar &#123;
                background-color: @brand-primary-{database}-{company_id};
                border-color: @brand-primary-{database}-{company_id};
              &#125;
              body.blue_theme__{database}__{company_id} .o_main_navbar button:hover,
              body.blue_theme__{database}__{company_id} .o_main_navbar button:focus &#123;
                background-color: darken(@brand-primary-{database}-{company_id}, 10%) !important;
              &#125;


              /* This picks up the menu items that are open but lost focus. */
              body.blue_theme__{database}__{company_id} .o_main_navbar > li.open > a:focus,
              body.blue_theme__{database}__{company_id} .o_main_navbar > li.open > a[aria-expanded="true"] &#123;
                  background-color: darken(@brand-primary-{database}-{company_id}, 10%);
              &#125;

              /* This is the "X" button that closes debug mode */
              body.blue_theme__{database}__{company_id} a[data-action="leave_debug_mode"]:hover &#123;
                  background-color: darken(@brand-primary-{database}-{company_id}, 10%);
              &#125;

              @media (min-width: @grid-float-breakpoint-max) &#123;
                body.blue_theme__{database}__{company_id} .o_main_navbar > li > a.oe_menu_toggler &#123;
                  background-color: @brand-primary-{database}-{company_id} !important;
                &#125;
              &#125;

              @media (max-width: @grid-float-breakpoint-max) &#123;
                body.blue_theme__{database}__{company_id} .o_main_navbar a:hover,
                body.blue_theme__{database}__{company_id} .o_main_navbar a:focus &#123;
                  background-color: darken(@brand-primary-{database}-{company_id}, 10%) !important;
                &#125;
              &#125;

              @media (min-width: @grid-float-breakpoint-max) &#123;
                body.blue_theme__{database}__{company_id} .o_main_navbar > li > a.oe_menu_toggler:focus,
                body.blue_theme__{database}__{company_id} .o_main_navbar > li > a.oe_menu_toggler:active,
                body.blue_theme__{database}__{company_id} .o_main_navbar > li > a.oe_menu_toggler:hover,
                body.blue_theme__{database}__{company_id} .o_main_navbar > li > a[data-toggle="dropdown"]:hover,
                body.blue_theme__{database}__{company_id} .o_main_navbar > li > a[data-toggle="dropdown"]:focus,
                body.blue_theme__{database}__{company_id} .o_main_navbar > li > a[data-toggle="collapse"]:hover,
                body.blue_theme__{database}__{company_id} .o_main_navbar > li > a[data-toggle="collapse"]:focus,
                body.blue_theme__{database}__{company_id} .o_main_navbar > .open > a &#123;
                  background-color: darken(@brand-primary-{database}-{company_id}, 10%) !important;
                &#125;
              &#125;

              body.blue_theme__{database}__{company_id} .o_main_navbar &#123;
                border-color: darken(@brand-primary-{database}-{company_id}, 10%) !important;
              &#125;
              body.blue_theme__{database}__{company_id} .o_main_navbar .o_menu_brand &#123;
                border-bottom: 1px solid darken(@brand-primary-{database}-{company_id}, 10%);
              &#125;
              body.blue_theme__{database}__{company_id}.o_web_client .navbar .o_menu_toggle:hover &#123;
                background-color: darken(@brand-primary-{database}-{company_id}, 10%) !important;
              &#125;
              body.blue_theme__{database}__{company_id}.o_web_client .o_main_navbar > ul > li > a:hover,
              body.blue_theme__{database}__{company_id}.o_web_client .o_main_navbar > ul > li > a:hover,
              body.blue_theme__{database}__{company_id}.o_web_client .o_main_navbar .dropdown-toggle:hover,
              body.blue_theme__{database}__{company_id}.o_web_client .o_main_navbar .dropdown-toggle:focus &#123;
                background-color: darken(@brand-primary-{database}-{company_id}, 10%) !important;
              &#125;
              body.blue_theme__{database}__{company_id} .o_list_view tfoot &#123;
                background-color: @brand-primary-{database}-{company_id};
              &#125;
              body.blue_theme__{database}__{company_id} .o_searchview .o_searchview_facet .o_searchview_facet_label &#123;
                background-color: @brand-primary-{database}-{company_id};
              &#125;
              body.blue_theme__{database}__{company_id} .o_form_view.o_form_editable .o_form_field .o_list_view td.o_readonly &#123;
                background-color: transparent;
              &#125;
              body.blue_theme__{database}__{company_id} .navbar &#123;
                &-default &#123;
                  .badge &#123;
                    background-color: #fff;
                    color: @navbar-default-bg-{database}-{company_id};
                  &#125;
                &#125;
                &-inverse &#123;
                  .badge &#123;
                    background-color: #fff;
                    color: @navbar-inverse-bg-{database}-{company_id};
                  &#125;
                &#125;
              &#125;
              """.format(
                database=dbname,
                company_id=company.id)

            if company.override_home:
                css_string += '''
                    body.blue_theme__{database}__{company_id} .o_application_switcher &#123;
                        background: -webkit-gradient(linear, left top, right bottom,
                        from(@brand-info-{database}-{company_id}),
                        to(darken(@brand-info-{database}-{company_id}, 10%))
                        );
                    &#125;
                '''.format(
                    database=dbname,
                    company_id=company.id)

            f.write(css_string)
        f.close()
    except Exception as e:
        _logger.debug('Theme error writing to file : %s' % e)


def combine_bootswatch_less(env):
    """
    Write the company theme details as bootswatch-compatible less
    variables in a bootswatch less file.

    :raise Exception: if there is an error opening or writing to files
    :return: None
    """
    addon_path = env['ir.config_parameter'].get_param(
        'blue_custom_branding.addon_path')
    if addon_path:
        outname = "{}/static/src/less/bootswatch.less".format(addon_path)

        filepath = "{}/static/src/less/".format(addon_path)
        infiles = [fn for fn in os.listdir(
            filepath) if re.match("bootswatch_.*.less", fn)]

        try:
            f = open(outname, "w")
            for file in infiles:
                with open(filepath + file, 'r') as datafile:
                    inless = datafile.read()
                    inless = inless.replace('&#123;', '{')
                    inless = inless.replace('&#125;', '}')
                    f.write(inless)
                    datafile.close()

            f.close()
        except Exception as e:
            _logger.debug('Theme error writing to file : %s' % e)


def combine_variables_less(env):
    """
    Write the company theme details as less variables in a less file.

    :raise Exception: if there is an error opening or writing to files
    :return: None
    """
    addon_path = env['ir.config_parameter'].get_param(
        'blue_custom_branding.addon_path')
    if addon_path:
        outname = "{}/static/src/less/variables.less".format(addon_path)

        filepath = "{}/static/src/less/".format(addon_path)
        infiles = [fn for fn in os.listdir(
            filepath) if re.match("variables_.*.less", fn)]

        try:
            f = open(outname, "w")
            for file in infiles:
                with open(filepath + file, 'r') as datafile:
                    inless = datafile.read()
                    f.write(inless)
                    datafile.close()

            f.close()
        except Exception as e:
            _logger.debug('Theme error writing to file : %s' % e)
