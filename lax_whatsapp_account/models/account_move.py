# -*- coding: utf-8 -*-
# Part of LaxiconSolution. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models, _
from odoo.exceptions import UserError
import html2text

class AccountMove(models.Model):
    _inherit = 'account.move'

    def send_by_whatsapp(self):
        model_id = self.env['ir.model'].search([('model', '=', 'account.move')], limit=1)
        default_mail_template_id = self.env['mail.template'].search([('model_id', '=', model_id.id)], limit=1)
        invoice_url = self.env['ir.config_parameter'].get_param('web.base.url')
        invoice_url += self.get_portal_url()
        invoice_url += "&report_type=pdf&download=true"
        if not self.partner_id.country_id:
            raise UserError(_("Please select country for customer %s") % self.partner_id.name)
        return {
            'type': 'ir.actions.act_window',
            'name': 'Send to WhatsApp',
            'res_model': 'send.whatsapp.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_model_id': model_id.id, 'default_res': self.id, 
            'default_mail_template_id': default_mail_template_id.id,'default_mobile_number': self.partner_id.mobile, 'media_url': invoice_url},
            
        }
        
        

