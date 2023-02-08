// Copyright (c) 2023, Fernando Garcia and contributors
// For license information, please see license.txt
 let max = 0;
 frappe.ui.form.on("Gym Locker", {
    onload(frm) {
        frappe.call({method:'fgarcia_frappe_eval.fgarcia_frappe_eval.doctype.gym_locker.gym_locker.get_max', args:{
        },
        callback:function(r){
            max = parseInt(r.message);
            console.log("LOCKER MAX="+max)
          

        }

    });
   // if(frm.doc.id_number < 1 || frm.doc.id_number > max)frm.disable_save();
    },
    //id_number(frm){
    //    if(frm.doc.id_number > 1 && frm.doc.id_number <= max)frm.enable_save();
    //    
    //},
    
    validate(frm){
        console.log('BEFORE SAVE')
        if (frm.doc.id_number > max || frm.doc.id_number < 1){
        frappe.throw(__("Invalid ID. Please select a number from 1 to "+max))
        console.log("ERROR! MAX="+max)
        //frm.doc.id_number='';
        }

    }
 });
