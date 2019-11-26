# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Cupos(models.Model):
    _name = 'store.cupos'

    name = fields.Many2one('res.partner', string='Aseguradora', domain="[('aseguradora_id', '=', True)]")
    cupo_total = fields.Float(string='Cupo total', help='Almacene acá el cupo total del cliente por aseguradora')
    cupo_utilizado = fields.Float(string='Cupo utilizado', help='Almacene acá el cupo utilizado por el cliente')
    cupo_disponible = fields.Float(string='Cupo disponible', compute='_cupo_disponible')

    @api.depends('cupo_utilizado','cupo_total')
    def _cupo_disponible(self):
    	self.cupo_disponible = self.cupo_total - self.cupo_utilizado






