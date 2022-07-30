from odoo import api, fields, models


class BenchClient(models.Model):
    _name = "bench.client"
    _description = "Bench Client"

    client_name = fields.Char(string='Client Name')
    contract_value = fields.Integer(string="Contract Value")
    contract_type = fields.Selection([('bookkeeping', 'bookkeeping'), ('consulting', 'consulting'),('odoo', 'odoo'),('audit', 'audit')], string="Contract Type")
    ref = fields.Integer(string='Reference')
    contract_start = fields.Date(string='Contract Start Date')
    account_team_leader = fields.Selection([('ahmed', 'ahmed')], string="Account Team Leader")
    contract_end = fields.Date(string='Contract End Date')
    active = fields.Boolean(string="Active", default=True)