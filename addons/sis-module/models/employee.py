# -*- coding: utf-8 -*-

from odoo import models, fields


class Employee(models.Model):
    _name = "sis-module.employees"
    _description = "Employees"

    firstName = fields.Char(string="firstName", required=True)
    lastName = fields.Char(string="lastName", required=True)
    password = fields.Char(string="password", required=True)
    profile = fields.Image(string="profile", required=True)
    isAdmin = fields.Boolean(string="isAdmin", required=True)
    phoneNumber = fields.Char(string="phoneNumber", required=True)
    email = fields.Char(string="email", required=True)

    creates = fields.One2many(comodel_name="sis-module.solutions",
                              inverse_name="createdBy", string="creates")
    handles = fields.One2many(
        comodel_name="sis-module.clients", inverse_name="handledBy", string="handles")
