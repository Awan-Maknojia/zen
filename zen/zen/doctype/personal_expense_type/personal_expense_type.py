# Copyright (c) 2026, Awan Maknojia and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class PersonalExpenseType(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		allocated_budget: DF.Currency
		allocated_percent: DF.Percent
		expense_type: DF.Data
		type: DF.Literal["", "Amount", "Percent"]
	# end: auto-generated types
	pass