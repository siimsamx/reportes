# -*- coding: utf-8 -*-
{
    'name': "Producción",

    'summary': """
        Orden de trabajo,SIIMSA """,

    'description': """
        Universidad Politécnica Metropolitana de Hidalgo | Ingeniería en Tecnologías de la Información
    """,

    'author': "Alan Cortés",
    'website': "https://www.siimsa.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Prototipo',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail','hr','web_planner','web_tour','muk_dms'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/one_view.xml',
        'views/two_view.xml',
        'views/three_view.xml',
        'views/four_view.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}