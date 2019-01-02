# -*- coding: utf-8 -*-
# noinspection PyStatementEffect
{
    'name': 'Odoo Color Branding',
    'category': 'Extra Tools',
    'version': '11.0.0',
    'license': 'OPL-1',
    'author': 'Blue Stingray',
    'website': 'http://bluestingray.com/services/erp',
    'application': True,
    'available_in_store': True,

    # |-------------------------------------------------------------------------
    # | Short Summary
    # |-------------------------------------------------------------------------
    # |
    # | Short 1 phrase line / summary of the modules purpose. Used as a subtitle
    # | on module listings.
    # |

    'summary': 'Easily set the color scheme for your Odoo instance',

    # |-------------------------------------------------------------------------
    # | Description
    # |-------------------------------------------------------------------------
    # |
    # | Long description describing the purpose / features of the module.
    # |

    'description': 'Easily set the color scheme for your Odoo instance',

    # |-------------------------------------------------------------------------
    # | Dependencies
    # |-------------------------------------------------------------------------
    # |
    # | References of all modules that this module depends on. If this module
    # | is ever installed or upgrade, it will automatically install any
    # | dependencies as well.
    # |

    'depends': ['base'],

    # |-------------------------------------------------------------------------
    # | Data References
    # |-------------------------------------------------------------------------
    # |
    # | References to all XML data that this module relies on. These XML files
    # | are automatically pulled into the system and processed.
    # |

    'data': [
        'security/ir.rule.csv',
        'security/ir.model.access.csv',
        # 'security/groups/group_module.xml',

        'init.xml',
        'records/asset.xml',
        'records/parameter.xml',
        'records/view/form/form_res.xml',
    ],

    # |-------------------------------------------------------------------------
    # | Images
    # |-------------------------------------------------------------------------
    # |
    # | Relative paths to images, primarily for use in module descriptions.
    'images': [
        'static/description/banner.jpg',
    ],

    # |-------------------------------------------------------------------------
    # | Demo Data
    # |-------------------------------------------------------------------------
    # |
    # | A reference to demo data
    # |

    'demo': [
        'records/demo/demo.xml'
    ],

    # |-------------------------------------------------------------------------
    # | Is Installable
    # |-------------------------------------------------------------------------
    # |
    # | Gives the user the option to look at Local Modules and install, upgrade
    # | or uninstall. This seems to be used by most developers as a switch for
    # | modules that are either active / inactive.
    # |

    'installable': True,

    # |-------------------------------------------------------------------------
    # | Auto Install
    # |-------------------------------------------------------------------------
    # |
    # | Lets Odoo know if this module should be automatically installed when
    # | the server is started.
    # |

    'auto_install': False,

    # |-------------------------------------------------------------------------
    # | Module Pricing
    # |-------------------------------------------------------------------------
    # |
    # | This is used for http://odoo.com/apps when the module is for sale. This
    # | states how much the module costs and in what currency.
    # |

    'price': 50.00,
    'currency': 'USD'
}
