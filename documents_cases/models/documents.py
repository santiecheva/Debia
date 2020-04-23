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
	image_bin = fields.Binary(string = 'Adjunto')
	renovacion = fields.Date(string = 'renovacion')
	description = fields.Char(string = 'Descripción')
	



