// Copyright (c) 2023, Fernando Garcia and contributors
// For license information, please see license.txt

frappe.ui.form.on("Gym Trainer Rating", {
	refresh(frm) {
        let is_allowed = frappe.user_roles.includes('Gym Manager') || frappe.user_roles.includes('Administrator') || frappe.user_roles.includes('Gym Trainer') ;
        if (!is_allowed) frm.set_value('gym_member',frappe.session.user)
        frm.toggle_enable(['gym_member'], is_allowed);

	},
});
