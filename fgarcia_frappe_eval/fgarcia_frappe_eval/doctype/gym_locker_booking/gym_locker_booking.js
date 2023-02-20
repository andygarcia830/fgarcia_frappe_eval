// Copyright (c) 2023, Fernando Garcia and contributors
// For license information, please see license.txt

 frappe.ui.form.on("Gym Locker Booking", {
    validate(frm){
        if (frm.doc.start_date > frm.doc.end_date ) {
            frappe.throw(__("Invalid date range: Start date must come before end date."));
        }
        console.log('VALIDATE')
        frappe.call({method:'fgarcia_frappe_eval.fgarcia_frappe_eval.doctype.gym_locker_booking.gym_locker_booking.validate', args:{
            name:frm.doc.name,
            gym_locker:frm.doc.gym_locker,
            start_date:frm.doc.start_date,
            end_date:frm.doc.end_date
        },
        callback:function(r){
            let overlap=0
            overlap = parseInt(r.message);
            if (overlap > 0) {
                frappe.validated=false
                frappe.throw(__("Locker is already booked for that date range"));
            }
        
        },
       
        });

    },

    refresh(frm){
        frm.set_value('gym_member',frappe.session.user)
        let is_allowed = frappe.user_roles.includes('Gym Manager') || frappe.user_roles.includes('Administrator') ;
        frm.toggle_enable(['gym_member'], is_allowed);
    },

 });
