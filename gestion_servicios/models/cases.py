from odoo import models, fields, api

class TypeCases(models.Model): 
	_name = 'types.cases'
	_description = 'Tipos de caso'

	name = fields.char(string='Tipo de caso')
	