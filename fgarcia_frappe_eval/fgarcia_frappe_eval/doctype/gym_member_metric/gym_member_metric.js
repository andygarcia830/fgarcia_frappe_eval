// Copyright (c) 2023, Fernando Garcia and contributors
// For license information, please see license.txt





frappe.ui.form.on("Gym Member Metric", {
    onload(frm) {
        
        let is_allowed = frappe.user_roles.includes('Gym Manager') || frappe.user_roles.includes('Administrator')  || frappe.user_roles.includes('Gym Trainer') ;
        console.log("GYM MEMBER="+ frm.doc.gym_member)
        if (!is_allowed &&  frm.doc.gym_member==undefined) frm.set_value('gym_member',frappe.session.user)
        frm.toggle_enable(['gym_member'], is_allowed);

        if(!is_allowed && frappe.session.user != frm.doc.gym_member) {
            frm.disable_save();
            frappe.throw('Invalid Access');
        }
     
 	},

   
});
