from odoo import models, fields, api

class MaestroTraslados(models.Model):
	_name = 'maestro.traslados'

	name = fields.Char(string = 'Traslado') 