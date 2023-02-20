// Copyright (c) 2023, Fernando Garcia and contributors
// For license information, please see license.txt

 frappe.ui.form.on("Gym Member", {
 
    
    onload(frm) {
        
        let is_allowed = frappe.user_roles.includes('Gym Manager') || frappe.user_roles.includes('Administrator') ;
        frm.toggle_enable(['user'], is_allowed);
        frm.toggle_enable(['subscription'], is_allowed);
        frm.toggle_enable(['join_date'], is_allowed);
        frm.toggle_enable(['status'], is_allowed);
      
        if(!is_allowed && frappe.session.user != frm.doc.user) {
            frm.disable_save();
            frm.set_value('subscription','');
            frm.set_value('join_date','');
            frm.set_value('status','');
            frm.toggle_enable(['metric'], is_allowed);
            frappe.throw('Invalid Access');
        }
     
        frappe.call({method:'fgarcia_frappe_eval.fgarcia_frappe_eval.services.utils.fetch_details', args:{
            email : frm.doc.user
            },
            callback:function(r){
                const obj = r.message
                frm.set_value('first_name',obj.first_name);
                frm.set_value('last_name',obj.last_name);
                frm.set_value('email_address',obj.email);
                frm.set_value('mobile_no',obj.mobile_no);
                frm.set_value('location',obj.location);
                frm.set_value('gender',obj.gender);
                frm.set_value('birth_date',obj.birth_date);
            }
            });


 	},

    user(frm){
        frappe.call({method:'fgarcia_frappe_eval.fgarcia_frappe_eval.services.utils.fetch_details', args:{
            email : frm.doc.user
            },
            callback:function(r){
                const obj = r.message
               frm.set_value('first_name',obj.first_name);
                frm.set_value('last_name',obj.last_name);
                frm.set_value('email_address',obj.email);
                frm.set_value('mobile_no',obj.mobile_no);
                frm.set_value('location',obj.location);
                frm.set_value('gender',obj.gender);
                frm.set_value('birth_date',obj.birth_date);
            }
            });
        }
        
 });
