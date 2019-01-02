Custom Branding
===============

Setup
-----

#### 1. Install the module

The module is installed through Odoo's App interface. It will
automatically install Odoo dependencies not already installed.

#### 2. Choose Theme Save Location

By default, there is a **System Parameter**, `blue\_custom\_branding.addon\_path`.
The *value* defined there tells Odoo where to store and create the less
files. It uses an example path, but you will probably need to update it
based on your Odoo server setup. We suggest using the full path of
where the `blue\_custom\_branding` module is installed.

For example, `/home/odoo\_user/odoo/odoo9/vendor\_addons/blue\_custom\_branding`.
The process Odoo runs under must have permission to read and write to this
directory.


Usage
-----

This module allows you to have a different color theme depending on
which company the user is logged into. The purpose is to give a visual
indication telling the user which company they are logged into. You can
also use this module to easily change the colors within Odoo, even if
you do not use the multi-company functionality.

#### 1. Choose Colors for the Company

To select colors for a company, go to **Settings > Users > Companies**. In the
company's form view, there is a "Theme" tab where you can enter
various colors for each class of UI elements.

When entering a color, use the hex value of the color,
leaving off the `\#` at the front of the color value.

The **Info Color** is the color that defines the top bar, perhaps the most
important variable you want to change.

##### (Optional)

You can use themes from Bootswatch (https://bootswatch.com). To use a
prebuilt theme, look at the `variables.less` file and copy the
`@brand-{variable}` value into the Theme area for the company in Odoo.

#### 2. Refresh your browser

After changing the color(s) associated with a company, you must refresh the
browser to see any changes. This also applies when changing the company
that the user is logged into.
