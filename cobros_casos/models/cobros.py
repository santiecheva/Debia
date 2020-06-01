from odoo import models, fields, api

class CobrosCasos(models.Model):
	_name = 'tarifas.casos'

	name = fields.Char(string = 'Cobro')
	case_id = fields.Many2one('types.cases', string = 'Oportunidad')
	cobro = fields.Integer(string = 'Valor a cobrar')
	pago = fields.Integer(string = 'Valor a Pagar')
	fecha_desde = fields.Date(string = 'Vigencia desde')
	fecha_hasta = fields.Date(string = 'Vigencia hasta')	

class CrmLead(models.Model):

	inherit = 'crm.lead'

	tarifa_cobro = fields.Integer(string = 'Tarifa Cobro')
	tarifa_pago = fields.Integer(string = 'Tarifa pago')


	@api.onchange('case_id')
	def _onchange_case(self):
		tarifa = self.env['tarifas.casos'].search([('case_id','=',self.case_id)])
		self.tarifa_pago = tarifa.pago
		self.tarifa_cobro = tarifa.cobro

