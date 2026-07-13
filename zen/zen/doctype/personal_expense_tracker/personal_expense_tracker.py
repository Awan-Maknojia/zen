# Copyright (c) 2026, Awan Maknojia and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import now_datetime


class PersonalExpenseTracker(Document):
    # begin: auto-generated types
    # This code is auto-generated. Do not modify anything in this block.

    from typing import TYPE_CHECKING

    if TYPE_CHECKING:
        from frappe.types import DF
        from zen.zen.doctype.expense_tracker.expense_tracker import ExpenseTracker

        amended_from: DF.Link | None
        amount_spent: DF.Currency
        approved: DF.Check
        balance: DF.Currency
        date: DF.Date | None
        income: DF.Currency
        month: DF.Literal["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        saving: DF.Currency
        tracker: DF.Table[ExpenseTracker]
        type: DF.Literal["", "Amount", "Percent"]
    # end: auto-generated types
    
    def before_save(self):
        self.set_balance()
        self.set_saving_amount_spent()
        self.set_month_approval()
        
    def set_balance(self):
        for i in self.tracker:
            if self.type == "Amount":
                i.balance = (i.allocated_budget or 0) - (i.utilized_budget or 0)
                if i.balance < 0:
                    frappe.throw(f"Row{i.idx}: The allocated amount for {i.expense_type} = {i.allocated_budget}")
            elif self.type == "Percent":
                i.utilized_budget = (self.income or 0) * (i.allocated_percent or 0) / 100
                i.balance = self.income - (i.utilized_budget or 0)

    def set_saving_amount_spent(self):
        amount_spent = 0
        balance = 0

        for i in self.tracker:
            amount_spent += i.utilized_budget or 0
            balance += i.balance or 0

        self.amount_spent = amount_spent
        self.balance = balance
        self.saving = self.income - self.amount_spent
        
    def set_month_approval(self):
        current_month = now_datetime().strftime("%B")
        if (self.month == current_month):
            self.approved = 0
        else:
            self.approved = 1

def set_month_button():
    current_month = now_datetime().strftime("%B")
    for name in frappe.get_all(
        "Personal Expense Tracker",
        filters={"month": current_month},
        pluck="name",
    ):
        frappe.db.set_value("Personal Expense Tracker", name, "approved", 0)
    for name in frappe.get_all(
        "Personal Expense Tracker",
        filters={"month": ["!=", current_month]},
        pluck="name",
    ):
        frappe.db.set_value("Personal Expense Tracker", name, "approved", 1)

    frappe.db.commit()