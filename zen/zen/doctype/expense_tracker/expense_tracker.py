# Copyright (c) 2026, Awan Maknojia and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ExpenseTracker(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		allocated_budget: DF.Currency
		allocated_percent: DF.Percent
		balance: DF.Currency
		expense_type: DF.Link | None
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		utilized_budget: DF.Currency
	# end: auto-generated types
	pass
