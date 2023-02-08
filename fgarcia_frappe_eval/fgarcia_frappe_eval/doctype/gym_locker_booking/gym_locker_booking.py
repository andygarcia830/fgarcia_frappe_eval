# Copyright (c) 2023, Fernando Garcia and contributors
# For license information, please see license.txt

import frappe
from datetime import datetime
from collections import namedtuple
Range = namedtuple('Range', ['start', 'end'])
from frappe.model.document import Document

class GymLockerBooking(Document):
	pass


@frappe.whitelist()
def validate(name,gym_locker,start_date,end_date):
	start_date=datetime.strptime(start_date,'%Y-%m-%d').date()
	end_date=datetime.strptime(end_date,'%Y-%m-%d').date()
	r1 = Range(start=start_date, end=end_date)
	print(f'VALIDATE {gym_locker},{start_date},{end_date}')
	docList=frappe.db.get_list('Gym Locker Booking',filters={'gym_locker':gym_locker,},fields=['name','start_date', 'end_date'])
	for item in docList:
		if (item.name == name): continue
		r2 = Range(start=item.start_date, end=item.end_date)
		latest_start = max(r1.start, r2.start)
		earliest_end = min(r1.end, r2.end)
		delta = (earliest_end - latest_start).days + 1
		overlap = max(0, delta)
		print(f'LOCKER BOOKING {overlap}')
		if overlap > 0:
			# BUGGY! STILL SAVES AFTER THROWN EXCEPTION AND THE MESSAGE IS NOT DISPLAYED ON THE ERROR DIALOG BOX
			#msg = f'Locker {gym_locker} is already booked for that date range'
			#frappe.throw(msg)
			return overlap
	return 0
		

