# -*- coding: utf-8 -*-
{
    'name': "Canal Telefónica CRM",
    'version': "1.0",
    'author': "Epistementerprise sas",
    'category': "sales",
    'support': "santiecheva@gmail.com",
    'summary': "Personalización de CRM para canal de venta telefónica",
    'description': """
        
    """,
    'data': [
        'security/cupos_security.xml',  
        'views/res_partner_views.xml',
        'views/crm_lead_views.xml',
    ],
    #'demo': [
     #   'demo/helpdesk_demo.xml',
   # ], 
    'images': [],
    'depends': ['crm'],
    'application': True,
}
