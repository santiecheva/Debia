from odoo import models, fields, api, exceptions, tools

class CrmLead(models.Model):
	_inherit = 'crm.lead'

	attach_ids = fields.Many2one('res.documents', string='Adjuntos')

	@api.model
	@api.multi
	def _set_res_id(self):
		for record in self:
			for attach in attach_ids:
				attach.write('res_is':self.id)			
		return True 


