{
    'name': 'Expense Report',
    'version': '1.0.0',
    'depends': ['base','estate','report_xlsx'],
    'author': 'BRAIN STATION 23',
    'description': """
        A module to generate pdf reports for real estate application.
    """,
    'data':[
        'report/expense_reports_excel.xml',
        'report/expense_reports.xml',
        'report/expense_report_templates.xml',
    ],
    'installable': True,
}