// Copyright (c) 2026, Awan Maknojia and contributors
// For license information, please see license.txt

frappe.ui.form.on("Personal Expense Tracker", {
    setup: function (frm) {
        frm.check_expense_type = function (frm,row) {
            frm.doc.tracker.forEach(item => {
                    if ((row.expense_type == '' || row.idx == item.idx)) {
                    }
                    else {
                        if (row.expense_type  == item.expense_type ) {
                            row.tracker = '',
                            frappe.throw(__(`Row${item.idx}: ${item.expense_type} is already exist`))
                            frm.refresh_field('tracker');
                        }
                    }
                
            });
        };
    },
});


frappe.ui.form.on("Expense Tracker", {
    expense_type: function (frm, cdt, cdn) {
        let row = locals[cdt][cdn];
        frm.check_expense_type(frm, row);
    }
});
