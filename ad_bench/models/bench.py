from odoo import api, fields, models


class BenchClient(models.Model):
    _name = "bench.client"
    _description = "Bench Client"

    name = fields.Char(string='Name')
    age = fields.Integer(string="Age")
    gender = fields.Selection([('male', 'male'), ('female', 'female')], string="Gender")
