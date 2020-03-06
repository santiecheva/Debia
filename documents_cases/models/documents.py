from odoo import models, fields, api, exceptions, tools


class FilesTeam(models.Model):
	_name = 'files.team'
	_description = 'Archivos por modelo de investigación'

	name = fields.Char(string = 'Nombre de archivo')
	team_id = fields.Many2one('crm.team', string = 'Modelo de investigación')




class Documents(models.Model):
	_name = 'res.documents'
	_description = 'Administracion de adjuntos'

	name = fields.Many2one('files.team', string = 'Documento', required = True)
	attachment_id = fields.Many2one('ir.attachment', string = 'Adjuntos')
	renovacion = fields.Date(string = 'renovacion')
	res_id = fields.Integer(string = 'res_id')
	res_model = fields.Char(string = 'res_model', default='crm.lead')
	



