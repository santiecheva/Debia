from odoo import models, fields, api

class ResPartner(models.Model):
	_inherit = 'res.partner'

	is_insurance = fields.Boolean(string = 'is insurance?')
	