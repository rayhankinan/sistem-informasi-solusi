# -*- coding: utf-8 -*-

from odoo import models, fields


class Technology(models.Model):
    _name = "sis-module.technologies"
    _description = "Technologies"

    name = fields.Char(string="name", required=True)
    utility = fields.Text(string="utility", required=True)
    logo = fields.Image(string="logo", required=True)
    resource = fields.Binary(string="resource", required=True)

    build = fields.Many2many(
        comodel_name="sis-module.solutions", string="build")
    hasRisk = fields.Many2many(
        comodel_name="sis-module.vulnerabilities", string="hasRisk")
