# Copyright (c) 2023, Fernando Garcia and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class GymLocker(Document):
	pass

@frappe.whitelist()
def get_max():
	settings = frappe.get_doc('Gym Settings')
	return settings.locker_count