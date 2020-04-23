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
	case_id = fields.Many2one('types.cases', string = 'Tipo de Caso',  domain = "[('insurance_id','=',partner_id)]", help = 'Registre acá el tipo de caso')
	calidad = fields.Selection([('conductor','Conductor'),('ocupante','Ocupante'),
								('peaton','Peatón'),('ciclista','Ciclista')], string = 'Calidad del Afectado')
	valor = fields.Integer(string = 'Valor de Factura')
	relato_furips = fields.Text(string = 'Relato furips')
	relato_lesionado = fields.Text(string = 'Relato Afectado')
	lesion = fields.Text(string = 'Lesiones')
	vehiculo_id = fields.Many2one('tipo.vehiculo', string = 'Tipo de Vehículo')
	observaciones = fields.Html(string = 'Observaciones')
	motivo_estado = fields.Char(string = 'Motivo de objeción')
	conductor = fields.Char(string = 'Conductor')


# Datos del lesionado

	lesionado_id = fields.Many2one('res.partner', string='Afectado', domain = "[('entidad','=',False)]" )	
	tipo_documento = fields.Selection([('cedula','Cédula'),('ti','Tarjeta de Identidad'),
										('cc','Registro Civil'),('as','Adulto sin identificación'),
											('ms','Menor sin identificación'),('ce','Cédula de extrangería'),('nn','No identificado')], string = 'Tipo de Documento')		
	cedula_lesionado = fields.Char(string = 'Cedula del Afectado')
	phone_lesionado = fields.Char(string = 'Telefono del Afectado')	

#   Campos del fórmularios de datos según la IPS
	cedula_lesionado_related = fields.Char(string='Cédula del Afectado',
                               store=True,
                               related='lesionado_id.vat')
	phone_lesionado_related = fields.Char(string='Telefono del Afectado',
                               store=True,
                               related='lesionado_id.mobile')	

	fecha_ips = fields.Datetime(string = 'Fecha Accidente FURIPS')
	direccion_ips = fields.Char(string = 'Dirección Accidente FURIPS')

	contactado_id = fields.Many2one('res.partner', string='Contactado',  
		help = 'Ingrese el contacto que fue contactado por defecto este será el mismo lesionado, cámbielo si no es así.',
		domain = "[('entidad','=',False)]")
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
	propietario_id = fields.Many2one('res.partner', string = 'Propietario', domain = "[('entidad','=',False)]")
	doc_propietario = fields.Char(string = 'Documento propietario') 

	sexo = fields.Selection([('hombre','Masculino'),('mujer','Femenino')], string = 'Género')

	###### MORTALES #################
	beneficiario_id = fields.Many2one('res.partner', string = 'Beneficiario Principal', domain = "[('entidad','=',False)]")
	exequias = fields.Text(string = 'Exequias')
	nunc = fields.Char(string = 'NUNC')
	spoa = fields.Char(string = 'SPOA')
	fiscalia = fields.Char(string = 'Fiscalía')
	registro_defuncion = fields.Char(string = 'Registro Defunción')
	notaria = fields.Char(string = 'Notaría') 

	fecha_inscripcion = fields.Date(string = 'Fecha de Inscripción')
	estado_cuerpo = fields.Char(string = 'Estado del cuerpo')
	radicado_cuerpo = fields.Char(string = 'Registro de Defunción')
	activo_caso = fields.Selection([('activo','Activo'),('inactivo','Inactivo'),('archivado','Archivado')] ,string = 'Estado Fiscalía')
	

	funeraria = fields.Char(string = 'Funeraria')

	fecha_velacion = fields.Date(string = 'Fecha de Velación')
	
	cementerio = fields.Char(string = 'Cementerio')
	pago = fields.Selection([('no_pago','Sin pago'),('pago','Pago')], string='Estado de Pago')
	
	numero_noticia = fields.Char(string = 'Número de Noticia')
	direccion_fiscalia = fields.Char(string = 'Dirección Fiscalía')
	telefono_fiscalia = fields.Char(string = 'Telefono Fiscalía')

	#analisis_final = fields.Html(string = 'Analisis Final',
	 #	default = default_analisis_final)

	
	@api.multi
	def write_phone(self):
		partner_ids = self.env['res.partner'].search([('id','=',self.lesionado_id.id)])
		for partner in partner_ids:
			partner.write({'mobile':self.phone_lesionado})


	@api.onchange('phone_lesionado')
	def _onchange_tel_lesionado(self):
		if not self.telefono_contactado:			
			self.telefono_contactado = self.phone_lesionado

	@api.onchange('lesionado_id')
	def _onchage_contactado(self):
		if not self.contactado_id:
			self.contactado_id = self.lesionado_id


	# @api.constrains('heridos')
	# def _check_valor(self):
	# 	if self.heridos in [i for i in range(0:100)]:
	# 		raise exceptions.ValidationError('Por Favor escriba la cantidad de heridos en letras ejm: dos.')		

	@api.constrains('valor')
	def _check_valor(self):
		if self.valor < 0:
			raise exceptions.ValidationError('El valor no puede ser negativo')


			

	
"""
	def default_analisis_final(self):
		result = <div>PRUEBA</div>
		return result





	 	<div>
	 		Según el cotejamiento de la información dada por el entrevistado y los gastos que la  + self.insurance_id.name + reclama por la atención a este en la factura <b>No</b>  + self.factura +,  por el valor de $<span t-field = 'o.valor' />, encontramos que la información coincide y el centro clínico realizó al paciente los procedimientos por los cuales realiza la facturación brindada a la empresa. Así mismo, se confirmaron los hechos ocurridos el día  <span t-field = 'o.fecha_ips'  t-options='{"format": "MM/dd/yyyy"}'/>, donde resultó lesionado el señor <span t-field = 'o.lesionado_id.name' /> que involucra el <span t-field = 'o.vehiculo_id.name' /> de placas <span t-field = 'o.placa' /> amparado bajo la póliza SOAT <b>No.</b> <span t-field = 'o.poliza' /> expedida por seguros <span t-field = 'o.partner_id.name' />.
	 	</div>
	"""