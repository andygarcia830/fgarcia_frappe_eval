# Copyright (c) 2023, Fernando Garcia and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class GymClassBooking(Document):
	pass

@frappe.whitelist()
def validate(name,gym_class,gym_member):
	docList=frappe.db.get_list('Gym Class Booking',filters={'gym_class':gym_class,'gym_member':gym_member},fields=['name'])
	for item in docList:
		# BUGGY! STILL SAVES AFTER THROWN EXCEPTION AND THE MESSAGE IS NOT DISPLAYED ON THE ERROR DIALOG BOX
		msg = f'Gym Member is already booked for that class!'
		frappe.throw(msg)
	docList=frappe.db.get_list('Gym Class Booking',filters={'gym_class':gym_class},fields=['name'])
	count=len(docList)
	print(f'CLASS BOOKINGS={count}')
	docList=frappe.db.get_list('Gym Class',filters={'name':gym_class},fields=['name','available_slots'])
	print(f'AVAILABE SLOTS:{docList[0].available_slots}')
	if(count >= docList[0].available_slots):
		# BUGGY! STILL SAVES AFTER THROWN EXCEPTION AND THE MESSAGE IS NOT DISPLAYED ON THE ERROR DIALOG BOX
		msg = f'Class is fully booked!'
		frappe.throw(msg)
	