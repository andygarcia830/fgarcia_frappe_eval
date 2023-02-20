// Copyright (c) 2023, Fernando Garcia and contributors
// For license information, please see license.txt

frappe.ui.form.on("Gym Class Booking", {
    validate(frm){
        
        frappe.call({method:'fgarcia_frappe_eval.fgarcia_frappe_eval.doctype.gym_class_booking.gym_class_booking.validate', args:{
            name:frm.doc.name,
            gym_class:frm.doc.gym_class,
            gym_member:frm.doc.gym_member
        },
        callback:function(r){
            let overlap=0
            overlap = parseInt(r.message);
            if (overlap == 2) {
                frappe.validated=false
                frappe.throw(__("Class is fully booked"));
            }
            if (overlap == 1) {
                frappe.validated=false
                frappe.throw(__("Memeber is already booked for that class"));
            }
            
        },
       
        });
        

    },

    refresh(frm){
        let is_allowed = frappe.user_roles.includes('Gym Manager') || frappe.user_roles.includes('Administrator') || frappe.user_roles.includes('Gym Trainer') ;
        if (!is_allowed) frm.set_value('gym_member',frappe.session.user)
        frm.toggle_enable(['gym_member'], is_allowed);
    },


 });
