from odoo import models, fields, api
from odoo.exceptions import ValidationError

class FinanceReportWizard(models.TransientModel):
    _name = 'finance.filter.wizard'
    _description = 'Finance Filter Wizard'

    entry_type = fields.Selection([
        ('income', 'Income'),
        ('expense', 'Expense'),
    ], string="Entry Type")

    date_from = fields.Date(string="Date From")
    date_to = fields.Date(string="Date To")

    def action_filter_report(self):
        if self.date_from and self.date_to:
            if self.date_from > self.date_to:
                print("Error Date from is greater")
                raise ValidationError("Start date cannot be later than end date.")

        """Filters records based on user input and redirects to a tree view."""
        domain = []

        if self.entry_type:
            domain.append(('entry_type', '=', self.entry_type))

        if self.date_from:
            domain.append(('date_time', '>=', self.date_from))

        if self.date_to:
            domain.append(('date_time', '<=', self.date_to))

        return {
            'type': 'ir.actions.act_window',
            'name': 'Filtered Finance Entries',
            'res_model': 'finance.entry',
            'view_mode': 'tree,form',
            'domain': domain,
            'target': 'current',
        }
