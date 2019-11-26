# -*- coding: utf-8 -*-

from odoo import api, fields, models

class ResPartner(models.Model):
	_inherit = 'res.partner'

	cupos_ids = fields.Many2many('store.cupos', string='Cupos')
