{
    "name": "Attendance Dashboard",
    "version": "1.0",
    "category": "Dashboard",
    "summary": "Employee Attendance Dashboard for odoo-18",
    "description": "Attendace Dashboard for employee in Odoo-18",
    "author": "Brain Station 23",
    "license": "LGPL-3",
    "depends": ["web","hr_attendance",],
    "data":["views/attendance_dashboard_views.xml"],
    "assets":{
        "web.assets_backend":[
              "attendance_dashboard/static/src/components/employee_card/employee_card.js",
              "attendance_dashboard/static/src/components/employee_card/employee_card.xml",
              "attendance_dashboard/static/src/components/employee_card/employee_card.scss",
            
              "attendance_dashboard/static/src/attendance_dashboard/attendance_dashboard.xml",
              "attendance_dashboard/static/src/attendance_dashboard/attendance_dashboard.js",
              "attendance_dashboard/static/src/attendance_dashboard/attendance_dashboard.scss",
                              ],
    },
    "application": True,
    "installable": True,
}