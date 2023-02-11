# Copyright (c) 2023, Fernando Garcia and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime
from datetime import timedelta

class GymMembershipPurchases(Document):
	pass


@frappe.whitelist()
def fetch_data(name,start):
	membership = frappe.get_doc('Gym Membership',name)
	start_date=datetime.strptime(start,'%Y-%m-%d')
	end_date = (start_date + timedelta(days = int(membership.duration_in_days))).date()
	print(f'\n\n {name} START {start_date} END {end_date}')
	result={}
	result['price']=membership.price
	result['end_date'] = end_date
	return result

@frappe.whitelist()
def update_member(name,start,end,member):
	member = frappe.get_doc('Gym Member',member)
	print(f'\n\nGOT MEMBER {member}')
	member.status='ACTIVE'
	member.subscription=name
	member.subscription_start=start
	member.subscription_end=end
	member.submit()