// Copyright (c) 2023, Fernando Garcia and contributors
// For license information, please see license.txt

frappe.ui.form.on("Gym Trainer Booking", {
    validate(frm){
        console.log('VALIDATE '+frm.doc.start_date_and_time)
        
        frappe.call({method:'fgarcia_frappe_eval.fgarcia_frappe_eval.doctype.gym_trainer_booking.gym_trainer_booking.validate', args:{
            name:frm.doc.name,
            gym_trainer:frm.doc.gym_trainer,
            start_date_and_time:frm.doc.start_date_and_time,
            duration_in_hours:frm.doc.duration_in_hours
        },
        callback:function(r){
            console.log("GOT DATETIME"+r.message)
            let overlap=0
            try {
                overlap = parseInt(r.message);
                if (overlap == 1) {
                    frappe.validated=false
                    frappe.throw(__("Trainer is already booked for that date range"));
                }
            }catch (Exception){}
            frm.doc.start_date_and_time=r.message
        },
       
        });

    },

    refresh(frm){

        let is_allowed = frappe.user_roles.includes('Gym Manager') || frappe.user_roles.includes('Administrator')  || frappe.user_roles.includes('Gym Trainer') ;
        if (!is_allowed) frm.set_value('gym_member',frappe.session.user)
        frm.toggle_enable(['gym_member'], is_allowed);
    },

});
