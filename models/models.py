# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Datos(models.Model):
    _name = 'reportes.trabajo'
    _inherit = ['mail.thread']

    orden_trabajo = fields.Integer(string='Núm. Orden de trabajo')
    orden_compra = fields.Integer(string='Núm. Orden de Compra')
    num_cotizacion = fields.Integer(string='Núm. de Cotización')
    num_remision = fields.Integer(string='Núm. de Remisión')
    num_pieza = fields.Integer(string='Núm. de Piezas')
    num_parte = fields.Integer(string='Núm. de Parte')
    fecha_solicitud = fields.Date(string='Fecha de solicitud')
    fecha_entrega = fields.Date(string='Fecha de entrega programada')
    fecha_real = fields.Date(string='Fecha de entrega real')
    descripcion = fields.Text(string='Escribe una nota')

    servicios_ids = fields.One2many('reportes.actividad','trabajo_id',string='Orden de trabajo')

    #----------MATERIALES--------------------------
    nom_material = fields.Char(string='Descripción')
    cantidad_mat = fields.Integer(string='Cantidad')
    unidad_mat = fields.Char(string='Unidad(es)')

    #---------Directorio---------------------------

    directorio = fields.Many2one('muk_dms.directory', string='Directorio')

class Operador(models.Model):
    _name = 'reportes.persona'

    nom_empleado = fields.Char(string='Nombre del empleado')
    dep_empleado = fields.Char(string='Departamento')


class Servicio(models.Model):
    _name = 'reportes.actividad'

    num_piezas = fields.Integer(string='Número de piezas')
    tiempo = fields.Float(string='Tiempo planificado')
    tiempo_r = fields.Float(string='Tiempo real')
    tipo_serv = fields.Selection([('1', 'Maquinado'),
                                  ('2', 'Fresado'),
                                  ('3', 'Soldadura'),
                                  ('4', 'Corte'),
                                  ('5', 'Rectificado'),
                                  ('6', 'Medición')],'Tipo de servicio')

    persona_id = fields.Many2one('reportes.persona',string="Operador")
    trabajo_id = fields.Many2one('reportes.trabajo',string="Orden de trabajo")