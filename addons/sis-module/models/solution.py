# -*- coding: utf-8 -*-

from odoo import models, fields


class Solution(models.Model):
    _name = "sis-module.solutions"
    _description = "Solutions"

    name = fields.Char(string="name", required=True)
    description = fields.Text(string="description", required=True)
    proposal = fields.Binary(string="proposal", required=True)

    createdBy = fields.Many2one(
        comodel_name="sis-module.employees", string="createdBy")
    usedBy = fields.Many2one(
        comodel_name="sis-module.clients", string="usedBy")
    builtWith = fields.Many2many(
        comodel_name="sis-module.technologies", string="builtWith")
