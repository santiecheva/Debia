from odoo import models, fields, api

class CrmLead(models.Model):
	_inherit = 'crm.lead'

	assistant_id = fields.Many2one('res.partner', string='Administrative assistant')
	insurance_id = fields.Many2one('res.partner', string = 'Insurance', domain = "[('is_insurance','=',True)]" )
	placa = fields.Char(string = 'Placa')
	poliza = fields.Char(string = 'Póliza')
	factura = fields.Char(string = 'Factura')
	