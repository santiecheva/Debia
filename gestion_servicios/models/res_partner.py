from odoo import models, fields, api

class ResPartner(models.Model):
	_inherit = 'res.partner'

	entidad = fields.Selection([('ips','IPS'),('eps','Aseguradora'),('propietarop','Propietario')], string = 'Entidad')
	#customer = fields.Boolean(default = True)

	
	
	