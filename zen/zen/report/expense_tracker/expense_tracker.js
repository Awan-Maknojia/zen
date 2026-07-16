// Copyright (c) 2026, Awan Maknojia and contributors
// For license information, please see license.txt

frappe.query_reports["Expense Tracker"] = {
	"filters": [
		{
			fieldname: "period",
			label: __("Period"),
			fieldtype: "Select",
			default: "",
			options: ["", "Today", "This Week", "This Month", "This Year", "Custom"],
			width: 100,
			reqd: 0,
		},
		{
			"fieldname": "month",
			"label": __("Month"),
			"fieldtype": "Select",
			"default": "",
			"options": ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
			"width": 100,
			"reqd": 0,
		},
		{
			"fieldname": "type",
			"label": __("Type"),
			"fieldtype": "Select",
			"default": "",
			"options": ["", "Amount", "Percent"],
			"width": 100,
			"reqd": 0,
		},
		{
			fieldname: "from",
			label: __("From Date"),
			fieldtype: "Date",
			width: 80,
			depends_on: "eval:doc.period=='Custom'",
			mandatory_depends_on: "eval:doc.period=='Custom'",
		},
		{
			fieldname: "to",
			label: __("To Date"),

			fieldtype: "Date",
			width: 80,
			depends_on: "eval:doc.period=='Custom'",
			mandatory_depends_on: "eval:doc.period=='Custom'",
		}
	]
};
