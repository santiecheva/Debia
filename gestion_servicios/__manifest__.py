# Copyright 2015 LasLabs Inc.
# Copyright 2018 Modoolar <info@modoolar.com>.
# Copyright 2019 initOS GmbH
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
{

    'name': 'Tracking service',
    "summary": "Módule for many service tracking",
    'version': '12.0.0.1',
    'author':
        "Santiago Echeverri, "
        "Epistem Enterprise SAtS",
    'category': 'sales',
    'depends': [
        'crm',
    ],
    "website": "https://epistementerprise.com/",
    "data": [
        'views/crm_lead_views.xml',
        'views/cases_views.xml',
        'views/res_partner_views.xml',
        'views/presentacion.xml',
        'security/ir.model.access.csv',
        #'security/res_users_pass_history.xml',
    ],
    #"demo": [
    #    'demo/res_users.xml',
    #],
    'aplication': True,
}
