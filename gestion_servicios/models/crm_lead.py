from odoo import models, fields, api

class CrmLead(models.Model):

	_inherit = 'crm.lead'

	assistant_id = fields.Many2one('res.users', string='Administrative assistant')
	insurance_id = fields.Many2one('res.partner', string = 'Insurance', domain = "[('entidad','=','eps')]" )
	placa = fields.Char(string = 'Placa')
	poliza = fields.Char(string = 'Póliza')
	factura = fields.Char(string = 'Factura')
	case = fields.Many2one('types.cases', string = 'Tipo de Caso')
	fecha = fields.Datetime(string = 'Fecha-Hora Accidente')
	relato_furips = fields.Text(string = 'Relato furips')
	relato_lesionado = fields.Text(string = 'Relato Lesionado')
	calidad = fields.Char(string = 'Calidad del Lesionado')
	fecha_ingreso = fields.Datetime(string = 'Fecha Ingreso')
	fecha_egreso = fields.Datetime(string = 'Fecha Egreso')
	ips_id = fields.Many2one('res.partner', string = 'IPS', domain = "[('entidad','=','ips')]")
	valor = fields.Integer(string = 'Valor de Factura')
	lesion = fields.Text(string = 'Lesiones')
	informe_medico = fields.Text(string = 'Informe Médico')
	atencion = fields.Text(string = 'Tratamiento')
	vehiculo = fields.Char(string = 'Tipo de Vehículo')
	observaciones = fields.Html(string = 'Observaciones')
	heridos = fields.Integer(string = 'Heridos') 
	traslado = fields.Char(string = 'Descripción Traslado')
