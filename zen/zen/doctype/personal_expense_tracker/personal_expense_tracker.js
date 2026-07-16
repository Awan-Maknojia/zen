frappe.ui.form.on("Personal Expense Tracker", {
    refersh(frm) {
        toggle_column(frm)
    },
    type(frm) {
        toggle_column(frm)
    },
    setup: function (frm) {
        frm.check_expense_type = function (frm, row) {
            frm.doc.tracker.forEach(item => {
                if ((row.expense_type == '' || row.idx == item.idx)) {
                }
                else {
                    if (row.expense_type == item.expense_type) {
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

function toggle_column(frm) {
    if (frm.doc.type == "Amount") {
        manage_child_columns(frm, ["allocated_percent"], "tracker", 1),
            manage_child_columns(frm, ["allocated_budget"], "tracker", 0)
    }
    else if (frm.doc.type == "Percent") {
        manage_child_columns(frm, ["allocated_budget"], "tracker", 1)
        manage_child_columns(frm, ["allocated_percent"], "tracker", 0)
    }
    else {
        manage_child_columns(frm, ["allocated_percent", "allocated_budget"], "tracker", 0)
    }
}

function manage_child_columns(frm, fields, table, hidden_value) {
    let grid = frm.get_field(table).grid;

    for (let field of fields) {
        grid.fields_map[field].hidden = hidden_value;
    }

    grid.visible_columns = undefined;
    grid.setup_visible_columns();

    grid.header_row.wrapper.remove();
    delete grid.header_row;
    grid.make_head();

    for (let row of grid.grid_rows) {
        if (row.open_form_button) {
            row.open_form_button.parent().remove();
            delete row.open_form_button;
        }

        for (let field in row.columns) {
            if (row.columns[field] !== undefined) {
                row.columns[field].remove();
            }
        }
        delete row.columns;
        row.columns = [];
        row.render_row();
    }

}
