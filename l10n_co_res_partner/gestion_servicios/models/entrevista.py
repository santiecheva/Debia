from odoo import models, fields, api, exceptions, tools

class ResEntrevista(models.Model):
	_name = 'maestro.entrevista'
	_description = 'Maestro de entrevistas'

	name = fields.Char(string='Nombre del entrevistado')
	documento = fields.Char(string = 'Tipo y Nro de Documento')
	relacion = fields.Char(string = 'Relacion')
	relato = fields.Text(string = 'Información Relevante')


class CrmLead(models.Model):
	_inherit = 'crm.lead'

	entrevistas_ids = fields.Many2many('maestro.entrevista', string = 'Entrevistas')
	