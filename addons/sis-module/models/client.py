# -*- coding: utf-8 -*-

from odoo import models, fields


class Client(models.Model):
    _name = "sis-module.clients"
    _description = "Clients"

    name = fields.Char(string="name", required=True)
    outline = fields.Text(string="outline", required=True)
    industry = fields.Selection(
        selection=["small/medium", "corporate", "enterprise"], string="industry", required=True)
    logo = fields.Image(string="logo", required=True)
    phoneNumber = fields.Char(string="phoneNumber", required=True)

    handledBy = fields.Many2one(
        comodel_name="sis-module.employees", string="handledBy")
    uses = fields.One2many(comodel_name="sis-module.solutions",
                           inverse_name="usedBy", string="uses")
