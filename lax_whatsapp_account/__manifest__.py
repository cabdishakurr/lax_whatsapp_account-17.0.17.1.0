# -*- coding: utf-8 -*-
# Part of LaxiconSolution. See LICENSE file for full copyright and licensing details.
{
    'name': 'Laxicon Whatsapp Account',
    "author": "Laxicon Solution",
    "license": "OPL-1",
    "website": "https://www.laxicon.in",
    "support": "info@laxicon.in",
    "category": "Accounting",
    "summary": "Send Invoice & Bills on Whatspapp",
    "description": """This module is very useful to send Invoice & Bills by Whatsapp to customer easily.""",
    'version': '17.1.0',
    'sequence': 1,
    'depends': ['base', 'account','lax_whatsapp_base'],
    'data': [
        
        'views/account_move_view.xml',
        
    ],
    "images":['static/description/banner.png'],
    'installable': True,
    'application': True,
    'pre_init_hook':  'pre_init_check',
}
