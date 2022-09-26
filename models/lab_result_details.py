from odoo import api, fields, models


class LabResultDetails(models.Model):
    _name = 'lab.result.details'
    _rec_name = 'antibiotic_name'

    antibiotic_name = fields.Char()
    result = fields.Char()
    method = fields.Char()
    result_id = fields.Many2one(comodel_name="all.lab.results")
