{
    'name': 'Finance Tracker',
    'version': '1.0',
    'summary': 'A custom module tracking your income and expenses',
    'author': 'Anish Ghimire',
    'depends':  ['base'],
    'sequence': -1000,
    'data': [
        "security/ir.model.access.csv",
        "views/finance_entry.xml",
        "views/finance_category.xml",
        "wizards/reports.xml"
    ],
    'installable': True,
    'application': True,
}
