from odoo import models, fields, api, exceptions, tools

class MaestroResultados(models.Model):
	
	_name = 'maestro.resultados'

	name = fields.Char(string = 'Resultado')
	partner_id = fields.Many2one('res.partner', string = 'Aseguradora', domain = "[('entidad','=','eps')]")



class MaestroObjecion(models.Model):
	_name = 'maestro.objecion'

	name = fields.Char(string = 'Objeción')
	codigo = fields.Integer(string = 'Código Aseguradora')
	insurance_id = fields.Many2one('res.partner',string = 'Aseguradora', domain="[('entidad','=','eps')]")

	