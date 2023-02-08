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
            console.log("GOT DATETIME"+r.message)
            frm.doc.start_date_and_time=r.message
        },
       
        });
        

    },

 });
