# -*- coding: utf-8 -*-
{
    'name': "Belsan Theme",
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    'description': """
        Long description of module's purpose
    """,
    'author': "Sahraa ",
    'website': " ",
    'category': 'Theme/Ecommerce',
    'version': '0.1',
    'depends': ['base', 'website', 'website_theme_install', 'sah_belsan'],
    'data': [
        'views/customize_template.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    'images': [
        'static/description/icon.png',
    ],
    'live_test_url': '',
    'application': False,
}
