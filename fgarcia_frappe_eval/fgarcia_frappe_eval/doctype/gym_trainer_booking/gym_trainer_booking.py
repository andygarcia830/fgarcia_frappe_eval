# Copyright (c) 2023, Fernando Garcia and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime
from datetime import timedelta
from collections import namedtuple
Range = namedtuple('Range', ['start', 'end'])


class GymTrainerBooking(Document):
	pass



@frappe.whitelist()
def validate(name,gym_trainer,start_date_and_time,duration_in_hours):
	print (f'START DATE AND TIME: {start_date_and_time}')
	start_date=datetime.strptime(start_date_and_time,'%Y-%m-%d %H:%M:%S')
	end_date=start_date + timedelta(hours = int(duration_in_hours))
	r1 = Range(start=start_date, end=end_date)
	print(f'VALIDATE {gym_trainer},{start_date},{end_date}')
	docList=frappe.db.get_list('Gym Trainer Booking',filters={'gym_trainer':gym_trainer,},fields=['name','start_date_and_time', 'duration_in_hours'])
	for item in docList:
		itemEndDate=item.start_date_and_time+timedelta(hours = int(item.duration_in_hours))
		print(f'COMPARING {item.name},{item.start_date_and_time},{itemEndDate},{item.duration_in_hours}')
		if (item.name == name): 
			print('CONTINUE')
			continue
		r2 = Range(start=item.start_date_and_time, end=itemEndDate)
		latest_start = max(r1.start, r2.start)
		earliest_end = min(r1.end, r2.end)
		overlap=0
		if latest_start < earliest_end:
			overlap = 1
		print(f'TRAINER BOOKING {overlap}')
		if overlap > 0:
			# BUGGY! STILL SAVES AFTER THROWN EXCEPTION AND THE MESSAGE IS NOT DISPLAYED ON THE ERROR DIALOG BOX
			msg = f'Trainer is already booked for that date range'
			frappe.throw(msg)
	dateStr=str(start_date.year)+'-'
	if start_date.month < 10: dateStr += '0'
	dateStr+=str(start_date.month)+'-'
	if start_date.day < 10: dateStr += '0'
	dateStr+=str(start_date.day)+' '
	if start_date.hour < 10: dateStr += '0'
	dateStr+=str(start_date.hour)+':00:00'
	return dateStr
