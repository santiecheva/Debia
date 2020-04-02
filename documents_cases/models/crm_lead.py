from odoo import models, fields, api, exceptions, tools

class CrmLead(models.Model):
	_inherit = 'crm.lead'

	attach_ids = fields.Many2many('res.documents', string='Adjuntos',
					 domain = "[('name.team_id','=',team_id)]")


		






