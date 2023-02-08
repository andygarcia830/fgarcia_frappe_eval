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
            frm.doc.start_date_and_time=r.message
        },
       
        });

    },

});
