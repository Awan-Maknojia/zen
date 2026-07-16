# Copyright (c) 2026, Awan Maknojia and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
    return get_columns(), get_data(filters)


def get_columns():
    return [
        {
            "label": "ID",
            "fieldname": "name",
            "fieldtype": "Link",
            "options": "Personal Expense Tracker",
            "width": 200,
        },
        {
            "label": "Month",
            "fieldname": "month",
            "fieldtype": "Data",
            "width": 100,
        },
        {
            "label": "Date",
            "fieldname": "date",
            "fieldtype": "Date",
            "width": 120,
        },
        {
            "label": "Type",
            "fieldname": "type",
            "fieldtype": "Data",
            "width": 80,
        },
        {
            "label": "Amount Spent",
            "fieldname": "amount_spent",
            "fieldtype": "Currency",
            "width": 120,
        },
        {
            "label": "Balance",
            "fieldname": "balance",
            "fieldtype": "Currency",
            "width": 120,
        },
        {
            "label": "Saving",
            "fieldname": "saving",
            "fieldtype": "Currency",
            "width": 120,
        },
    ]
    
def get_data(filters):
    filters = filters or {}

    conditions = "WHERE docstatus = 1"

    if filters.get("month"):
        conditions += f" AND month = '{filters.get('month')}'"

    if filters.get("type"):
        conditions += f" AND type = '{filters.get('type')}'"

    if filters.get("period") == "Today":
        conditions += " AND date = CURDATE()"

    elif filters.get("period") == "This Week":
        conditions += " AND YEARWEEK(date, 1) = YEARWEEK(CURDATE(), 1)"

    elif filters.get("period") == "This Month":
        conditions += " AND MONTH(date) = MONTH(CURDATE())"
        conditions += " AND YEAR(date) = YEAR(CURDATE())"

    elif filters.get("period") == "This Year":
        conditions += " AND YEAR(date) = YEAR(CURDATE())"

    elif filters.get("period") == "Custom":
        if filters.get("from"):
            conditions += f" AND date >= '{filters.get('from')}'"

        if filters.get("to"):
            conditions += f" AND date <= '{filters.get('to')}'"
            
    data = frappe.db.sql(
        f"""
        SELECT
            name,
            month,
            date,
            type,
            amount_spent,
            balance,
            saving
        FROM `tabPersonal Expense Tracker`
        {conditions}
        """,
        as_dict=True,
    )

    return data