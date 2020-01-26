from odoo import models, fields, api, exceptions, tools

class MaestroResultados(models.Model):
	
	_name = 'maestro.resultados'

	name = fields.Char(string = 'Resultado')
	partner_id = fields.Many2one('res.partner', string = 'Aseguradora', domain = "[('entidad','=','eps')]")
	