// Copyright (c) 2022, excle and contributors
// For license information, please see license.txt

frappe.ui.form.on('Account Migration', {
	 refresh: function(frm) {
		frm.add_custom_button('Open Reference form', () => {
			
			frappe.set_route('Form', frm.doc.reference_type, frm.doc.reference_name);
		})
	 }
});
