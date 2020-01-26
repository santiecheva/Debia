from odoo import models, fields, api

class TipoVehiculo(models.Model):
	_name = 'tipo.vehiculo'

	name = fields.Char(string = 'Tipo de Vehiculo')
	lead_id = fields.One2many('crm.lead','vehiculo_id',string = 'Leads')