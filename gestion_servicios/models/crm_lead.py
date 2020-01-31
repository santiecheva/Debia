from datetime import datetime, timedelta, date


from odoo import models, fields, api, exceptions, tools

class CrmLead(models.Model):

	_inherit = 'crm.lead'
#Campos generales
	placa = fields.Char(string = 'Placa', 
	help = 'Ingrese la placa del vehículo siniestrado' )

	assistant_id = fields.Many2one('res.users', string='Asistente Administrativo')
	insurance_id = fields.Many2one('res.partner', string = 'IPS', domain = "[('entidad','=','ips')]")
	poliza = fields.Char(string = 'Póliza', help = 'Ingrese el número de la póliza')
	factura = fields.Char(string = 'Factura', help = 'Ingrese la factura del caso')
	case_id = fields.Many2one('types.cases', string = 'Tipo de Caso',  domain = "[('insurance_id','=','partner_id')]", help = 'Registre acá el tipo de caso')
	calidad = fields.Selection([('conductor','Conductor'),('ocupante','Ocupante'),
								('peaton','Peatón'),('ciclista','Ciclista')], string = 'Calidad del Lesionado')
	valor = fields.Integer(string = 'Valor de Factura')
	relato_furips = fields.Text(string = 'Relato furips')
	relato_lesionado = fields.Text(string = 'Relato Lesionado')
	lesion = fields.Text(string = 'Lesiones')
	vehiculo_id = fields.Many2one('tipo.vehiculo', string = 'Tipo de Vehículo')
	observaciones = fields.Html(string = 'Observaciones')
	motivo_estado = fields.Char(string = 'Motivo de objeción')

# Datos del lesionado
	lesionado_id = fields.Many2one('res.partner', string='Lesionado', domain = "[('entidad','!=','ips'),('entidad','!=','eps')]" )	
	tipo_documento = fields.Selection([('cedula','Cédula'),('ti','Tarjeta de Identidad'),
										('cc','Registro Civil'),('as','Adulto sin identificación'),
											('ms','Menor sin identificación'),('ce','Cédula de extrangería'),('nn','No identificado')], string = 'Tipo de Documento')		
	cedula_lesionado = fields.Char(string = 'Cedula del lesionado')
	phone_lesionado = fields.Char(string = 'Telefono del lesionado')	
#   Campos del fórmularios de datos según la IPS
	fecha_ips = fields.Datetime(string = 'Fecha Accidente FURIPS')
	direccion_ips = fields.Char(string = 'Dirección Accidente FURIPS')

	contactado_id = fields.Many2one('res.partner', string='Contactado',  
		help = 'Ingrese el contacto que fue contactado por defecto este será el mismo lesionado, cámbielo si no es así.',
		domain = "['&',('entidad','!=','ips'),('entidad','!=','eps')]")
	fecha_contactado = fields.Datetime(string = 'Fecha Accidente según Contactado')
	direccion_contactado = fields.Char(string = 'Dirección Accidente según Contactado')
	

	fecha_ingreso = fields.Datetime(string = 'Fecha Ingreso')
	fecha_egreso = fields.Datetime(string = 'Fecha Egreso')

	informe_medico = fields.Text(string = 'Informe Médico')
	atencion = fields.Text(string = 'Tratamiento')
	heridos = fields.Char(string = 'Heridos') 
	traslado_id = fields.Many2one('maestro.traslados', string = 'Descripción Traslado')
	estados_id = fields.Many2one('maestro.resultados', string = 'Resultado', domain = "[('partner_id','=',partner_id)]")
	tomador_id = fields.Many2one('res.partner', string = 'Tomador')
	caso = fields.Char(string = 'Caso')
	telefono_contactado = fields.Char(string = 'Telefono del contactado')

	vigencia_poliza_desde = fields.Date(string = 'Vigencia Desde')
	vigencia_poliza_hasta = fields.Date(string = 'Vigencia Hasta')
	fecha_documento = fields.Datetime(string ='Fecha Documento', default = fields.Datetime.now)
	propietario_id = fields.Many2one('res.partner', string = 'Propietario', domain = "[('entidad','!=','ips'),('entidad','!=','eps')]")
	sexo = fields.Selection([('hombre','Hombre'),('mujer','Mujer')], string = 'Género')

	@api.constrains('valor')
	def _check_valor(self):
		if self.valor < 0:
			raise exceptions.ValidationError('El valor no puede ser negativo')

	@api.onchange('lesionado_id')
	def _onchage_contactado(self):
		if not self.contactado_id:
			self.contactado_id = self.lesionado_id


	@api.constrains('heridos')
	def _check_valor(self):
		if type(self.heridos) == int:
			raise exceptions.ValidationError('Por Favor escriba la cantidad de heridos en letras ejm: dos.')		

