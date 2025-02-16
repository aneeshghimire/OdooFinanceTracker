from odoo import models, fields, api


class FinanceReport(models.Model):
    _name = 'finance.report'
    _description = 'Finance Report'

    total_income = fields.Float(string="Total Income", compute="_compute_report",store=True)
    total_expense = fields.Float(string="Total Expense", compute="_compute_report",store=True)
    balance_comparison = fields.Char(string="Balance Comparison", compute="_compute_report",store=True)

    @api.depends('total_income', 'total_expense')
    def _compute_report(self):
        for report in self:
            # Calculate total income
            total_income = self.env['finance.entry'].search([('entry_type', '=', 'income')]).mapped('amount')
            report.total_income = sum(total_income)

            # Calculate total expense
            total_expense = self.env['finance.entry'].search([('entry_type', '=', 'expense')]).mapped('amount')
            report.total_expense = sum(total_expense)

            # Determine comparison between income and expense
            if report.total_income > report.total_expense:
                difference = report.total_income - report.total_expense
                report.balance_comparison = f'Income is greater than Expense by {difference} amount.'
            elif report.total_income < report.total_expense:
                difference = report.total_income - report.total_expense
                report.balance_comparison = f'Expense is greater than Income by {difference} amount.'
            else:
                report.balance_comparison = 'Income is equal to Expense'
