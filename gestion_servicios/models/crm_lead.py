from datetime import datetime, timedelta, date
import logging


from odoo import models, fields, api, exceptions, tools

_logger = logging.getLogger(__name__)


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


	cedula_lesionado = fields.Char(string = 'Cedula del Afectado', readonly = 'True' )
	phone_lesionado = fields.Char(string = 'Telefono del Afectado')	

#   Campos del fórmularios de datos según la IPS relacionados con el afectado
	cedula_lesionado_related = fields.Char(string='Cédula del Afectado',
                                readonly = 'True',
                                )

	phone_lesionado_related = fields.Char(string='Telefono del Afectado',
                               store=True,
                               related='lesionado_id.mobile')

	doctype = fields.Char(string = 'Tipo de Documento')
	#onchange con campo cedula lesionadi
	
	@api.onchange('lesionado_id')
	def cedula_lesionado(self):
		if self.lesionado_id:
			self.id_afectado = self.lesionado_id.xidentification

	id_afectado = fields.Char(string='Documento del Lesionado')

	tipo_documento_compute = fields.Char(string = 'Tipo de Documento',  readonly = 'True')

	@api.onchange('lesionado_id')
	@api.model
	def compute_tipo_documento(self):
		if self.lesionado_id:
			if self.lesionado_id.doctype == 1:
				self.doctype = 'Sin Identificación'
			elif self.lesionado_id.doctype == 11:
				self.doctype = 'Certificado de Nacimiento'
			elif self.lesionado_id.doctype == 12:
				self.doctype = 'Tarjeta de Identidad'			
			elif self.lesionado_id.doctype == 13:
				self.doctype = 'Cédula de Ciudadanía'
			elif self.lesionado_id.doctype == 21:
				self.doctype = 'Tarjeta de Extranjería'
			elif self.lesionado_id.doctype == 22:
				self.doctype = 'Cédula de Extranjería'
			elif self.lesionado_id.doctype == 31:
				self.doctype = 'NIT'
			elif self.lesionado_id.doctype == 41:
				self.doctype = 'Pasaporte'
			elif self.lesionado_id.doctype == 42:
				self.doctype = 'Documento de Identificación Extranjero'
			elif self.lesionado_id.doctype == 43:
				self.doctype = 'Sin Identificación del Exterior'	


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
	hechos = fields.Text(string = 'Hechos del Siniestro')
	nunc = fields.Char(string = 'NUNC')
	spoa = fields.Char(string = 'SPOA')
	fiscalia = fields.Char(string = 'Fiscalía')
	registro_defuncion = fields.Char(string = 'Registro Defunción')
	notaria = fields.Char(string = 'Notaría') 

	fecha_inscripcion = fields.Date(string = 'Fecha de Inscripción')
	estado_cuerpo = fields.Char(string = 'Estado del cuerpo')
	radicado_cuerpo = fields.Char(string = 'Registro de Defunción')
	activo_caso = fields.Selection([('activo','Activo'),('inactivo','Inactivo'),('archivado','Archivado')] ,string = 'Estado Fiscalía')
	
	fecha_expedicion_cc = fields.Date(string = 'Fecha de Expedición', help='Fecha de expedición de la cédula del lesionado')
	ciudad_expedicion = fields.Char(string= 'Lugar de Expedición Doc')

	funeraria = fields.Char(string = 'Funeraria')

	fecha_velacion = fields.Date(string = 'Fecha de Velación')
	
	cementerio = fields.Char(string = 'Cementerio')
	pago = fields.Selection([('no_pago','Sin pago'),('pago','Pago')], string='Estado de Pago')
	
	numero_noticia = fields.Char(string = 'Número de Noticia')
	direccion_fiscalia = fields.Char(string = 'Dirección Fiscalía')
	telefono_fiscalia = fields.Char(string = 'Telefono Fiscalía')

	department_id = fields.Many2one('res.country.state', string = 'Departamento Accidente')
	
	#cityacc_id = fields.Many2one('res.country.state.city', string = 'Ciudad Accidente')

	#cityacci_id = fields.Many2one('res.country.state.city', string= 'Ciudad Accidente')

	diligencia_no_conforme = fields.Text(string= 'Diligencias no Conformes')

	marca = fields.Char(string = 'Marca')
	linea = fields.Char(string = 'Línea')
	modelo = fields.Char(string = 'Modelo')
	color = fields.Char(string = 'Color')

	#estado_cedula = fields.Char(string = 'Estado Cédula')

	objecion_id = fields.Many2one('maestro.objecion', string = 'Causal de Objeción')

	analisis_final = fields.Html(string = 'Analisis Final')

	# Campos para determinar el tipo de diseño del informe
	is_contactado = fields.Boolean(string = 'Es Contactado', default=True)
	is_estandar = fields.Selection([
		('cubierto','Formato Cubierto'),
		('cubierto_con_novedad','Formato Cubierto con Novedad'),
		('no_cubierto','Formato No Cubierto'),
		('ocurrencia_no_confirmada','Ocurrencia No confirmada'),
		('trabajo_adelantado_cubierto','Trabajo Adelantado Cubierto'),
		('trabajo_adelantado_no_cubierto','Trabajo Adelantado No Cubierto')], 
		 string = 'Formato Analisis', default='cubierto')



	@api.onchange('phone_lesionado')
	def _onchange_tel_lesionado(self):
		if not self.telefono_contactado:			
			self.telefono_contactado = self.phone_lesionado

	@api.onchange('lesionado_id')
	def _onchage_contactado(self):
		if not self.contactado_id:
			self.contactado_id = self.lesionado_id


	@api.constrains('valor')
	def _check_valor(self):
		if self.valor < 0:
			raise exceptions.ValidationError('El valor no puede ser negativo')

	@api.constrains('stage_id')
	def _check_stage(self):
		if self.env.user == self.user_id:
			if self.stage_id == 4:
				raise exceptions.ValidationError('Por favor comuníquese con su coordinador para cerrar el caso')



