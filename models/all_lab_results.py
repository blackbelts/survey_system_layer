from odoo import api, fields, models


class AllLabResults(models.Model):
    _name = 'all.lab.results'
    _rec_name = 'isolate_number'
    _description = 'Middle Layer before Lab Data Mapping'

    lab_code = fields.Char()
    hospital_name = fields.Char()
    branch_name = fields.Char(string="Lab Name")
    culture_name = fields.Char()
    location_name = fields.Char()
    patient_no = fields.Char(string="Patient Number")
    lab_no = fields.Char()
    barcode = fields.Char()
    gender = fields.Selection(selection=[('Male', 'Male'), ('Female', 'Female'), ])
    age_years = fields.Integer(string="Age Years")
    age_months = fields.Integer(string="Age Months")
    age_days = fields.Integer(string="Age Days")
    sample_type = fields.Char()
    reg_date = fields.Datetime(string="REG Date",)
    collection_date = fields.Datetime()
    reviewed_date = fields.Datetime()
    colony_count = fields.Integer()
    isolate_number = fields.Char(required=True)
    organism_name = fields.Char()
    anti_details_ids = fields.One2many(comodel_name="lab.result.details", inverse_name="result_id",)
