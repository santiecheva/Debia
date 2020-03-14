from odoo import models, fields, api, exceptions, tools

class CrmLead(models.Model):
	_inherit = 'crm.lead'

	attach_ids = fields.Many2many('res.documents', string='Adjuntos', domain = "[('res_id','=',id)]")

	@api.multi
	def _set_res_id(self):
		for attach in attach_ids:
			attach.write({'res_id':self.id})
		return True

	@api.model
	@api.multi
	def create_attach(self):
		for attach in attach_ids:
			vals = {
				'name': self.attach.name,
				'res_id':self.id,
				'res_model':'crm.lead',
				}
				self.env['ir.attachment'].create(vals)





