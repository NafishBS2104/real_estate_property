import json
from odoo import http
from odoo.http import request,content_disposition

class XLSXReportController(http.Controller):

    @http.route(
        "/xlsx_reports",
        type="http",
        auth="user",
        csrf=False
    )
    def get_report_xlsx(self,model,options,output_format,report_name,**kw):
        report_obj = request.env[model].sudo()
        options = json.loads(options)
        response = request.make_response(
            None,
            headers=[
                (
                    "Content-Type",
                    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                ),
                (
                    "Content-Disposition",
                    content_disposition(
                        f"{report_name}.xlsx"
                    )
                )
            ]
        )

        report_obj.get_xlsx_report(options,response)

        return response
