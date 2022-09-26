# -*- coding: utf-8 -*-
from odoo import http, tools, _
from odoo.exceptions import AccessError, UserError
from odoo.http import request,Response
from datetime import datetime,date


class LabIntegration(http.Controller):

    @http.route('/create_lab_culture',type='json',auth='user',method="POST")
    def create_lab_result(self, **post):
        if request.jsonrequest:
            try:
                vals = {
                    "lab_code":post['rf.lab_code'],
                    "hospital_name":post['hospital_name'],
                    "branch_name":post['Branch_name'],
                    "culture_name":post['Culture_name'],
                    "location_name":post['LOCATION_NAME'],
                    "patient_no":post['PATIENT_NO'],
                    "lab_no":post['LAB_NO'],
                    "barcode":post['BARCODE'],
                    "gender":post['Gender'],
                    "age_years":post['AGE_YEARS'],
                    "age_months":post['AGE_MONTHS'],
                    "age_days":post['AGE_DAYS'],
                    "sample_type":post['SAMPLE_TypeE'],
                    "reg_date":post['REG_DATE'],
                    "collection_date":post['Collection_DATE'],
                    "reviewed_date":post['Reviewed_DATE'],
                    "colony_count":post['Colony Count'],
                    "isolate_number": post['isolate_number'],
                    "organism_name": post['ORGANISM_NAME'],
                }
                lines = []
                for rec in post['anti_details']:
                    lines.append((0,0,rec))
                vals.update({'anti_details_ids': lines})
                lab_result_id = request.env['all.lab.results'].create(vals)
                # result = {'id': lab_result_id.id}
                response = {"code": 200, "message": "Everything worked as expected,creation done correctly",
                            "data": {'lab_obj_id': lab_result_id.id}}
                return response
            except Exception as e:
                response = {'code': 400, 'message': 'Unexpected Error:{}'.format(e)}
                return response
        else:
            return False
