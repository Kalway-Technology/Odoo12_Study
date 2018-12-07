# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Study_Iterm(models.Model):
    _name = 'study.iterm'

    name = fields.Char(u'名称', size=64, translate=True)
    person_id = fields.Many2one('res.partner', u'负责人')
    description = fields.Text(u'描述')
    lession_id = fields.One2many('Study_Class',‘Iterm_id’,u'课程')
    
    
class Study_Class(models.Model):
    _name = 'study.class'

    name = fields.Char(u'名称', size=64, translate=True)
    teacher = fields.Many2one('res.partner', u'老师')
    start_time = fields.Datetime(u'开始时间')
    end_time = fields.Datetime(u'结束时间')
    seat_number = fields.Integer(u'座位数')
    study = fields.Many2many('res.partner','res_partner_study_rel','name',u'学生')
    Iterm_id = fields.Many2one('Study_Iterm',u'课程')