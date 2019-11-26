# -*- coding: utf-8 -*-

from odoo import api, fields, models

class CrmLead(models.Model):
	_inherit = 'crm.lead'

	responsive_payment = fields.Many2one('res.partner', string = 'Responsable de Pago')
	