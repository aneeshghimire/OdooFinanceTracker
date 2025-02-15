from odoo import models, fields, api

class FinanceCategory(models.Model):
    _name = 'finance.category'
    _description = 'Finance Category'

    name = fields.Char(string="Category Name", required=True)
    entry_type = fields.Selection([
        ('income', 'Income'),
        ('expense', 'Expense'),
    ], string="Category Type", required=True)

