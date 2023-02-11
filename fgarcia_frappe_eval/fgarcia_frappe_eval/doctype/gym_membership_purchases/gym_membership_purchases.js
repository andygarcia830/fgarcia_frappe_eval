// Copyright (c) 2023, Fernando Garcia and contributors
// For license information, please see license.txt

frappe.ui.form.on("Gym Membership Purchases", {
    gym_membership(frm){
        frappe.call({method:'fgarcia_frappe_eval.fgarcia_frappe_eval.doctype.gym_membership_purchases.gym_membership_purchases.fetch_data', args:{
            name : frm.doc.gym_membership,
            start: frm.doc.start_date
            },
            callback:function(r){
                const obj = r.message
                
                frm.set_value('price',obj.price);
                frm.set_value('end_date',obj.end_date);
                
            }
            });
        },
    after_save(frm){
        frappe.call({method:'fgarcia_frappe_eval.fgarcia_frappe_eval.doctype.gym_membership_purchases.gym_membership_purchases.update_member', args:{
            name : frm.doc.gym_membership,
            start: frm.doc.start_date,
            end: frm.doc.end_date,
            member: frm.doc.gym_member
            },
            callback:function(r){
                               
            }
            });
        }
});
