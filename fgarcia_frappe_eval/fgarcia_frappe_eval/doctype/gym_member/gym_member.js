// Copyright (c) 2023, Fernando Garcia and contributors
// For license information, please see license.txt

 frappe.ui.form.on("Gym Member", {
 	refresh(frm) {
        frm.add_fetch('user','first_name','first_name');
        frm.add_fetch('user','last_name','last_name');
        frm.add_fetch('user','email','email_address');
        frm.add_fetch('user','mobile_no','mobile_no');
        frm.add_fetch('user','location','location');
        frm.add_fetch('user','birth_date','birth_date');
        frm.add_fetch('user','gender','gender');
 	},

    before_save(frm) {
        console.log('BEFORE SAVE')
        frappe.call({method:'fgarcia_frappe_eval.fgarcia_frappe_eval.doctype.gym_member.gym_member.set_role', args:{
            email_address : frm.doc.user
            },
            callback:function(r){}
            });
        }
 });
