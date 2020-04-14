from odoo import models, fields, api, exceptions, tools

class CrmLead(models.Model):
	_inherit = 'crm.lead'

	attach_ids = fields.Many2many('res.documents', string='Adjuntos')

	@api.onchange('team_id')
	def item_delivered_ids_onchange(self):
		for record in self:
			return {'domain': {'attach_ids': [('name.team_id', '=', self.team_id.id)]}}	


#domain = "[('name.team_id','=',team_id)]



