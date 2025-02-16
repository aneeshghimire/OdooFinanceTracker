from odoo import models, fields, api

class FinanceEntry(models.Model):
    _name = 'finance.entry'
    _description = 'Finance Entry'

    title = fields.Char(string="Title", required=True,default="Draft Transaction")
    description = fields.Text(string="Description")
    amount = fields.Float(string="Amount", required=True,default=0.00)

    entry_type = fields.Selection([
        ('income', 'Income'),
        ('expense', 'Expense'),
    ], string="Entry Type", required=True)


    category_id = fields.Many2one(
        'finance.category',
        string="Category",
        required=True,
        domain="[('entry_type', '=', entry_type)]"
    )


    date_time = fields.Datetime(string="Date & Time", default=fields.Datetime.now, required=True)

