# Copyright (c) 2023, Fernando Garcia and contributors
# For license information, please see license.txt
# 

import frappe
from frappe.model.document import Document

class GymMember(Document):
	pass


@frappe.whitelist()
def set_role(email_address):
	user = frappe.get_doc("User",email_address)
	print(f'\n\n{user.first_name}')
	user.append('roles',{
				"doctype": "Has Role",
				"role":"Gym Member"
				})
	#user.role_profile_name = self.user_rol
	#user.save(ignore_permissions=True)