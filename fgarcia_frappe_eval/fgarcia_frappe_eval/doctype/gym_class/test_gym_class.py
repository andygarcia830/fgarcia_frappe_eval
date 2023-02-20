# Copyright (c) 2023, Fernando Garcia and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestGymClass(FrappeTestCase):
	def test_insert_class(self):
		frappe.get_doc({
			'doctype':'Gym Class',
			'type':'SPINNING',
			'instructor':'greg@xurpas.com',
			'schedule':'2023-02-20',
			'duration_hrs':1,
			'available_slots':10,

		}).insert()


	def test_insert_class_fail_missing_mandatory(self):
		frappe.get_doc({
			'doctype':'Gym Class',
			'type':'SPINNING',
			'instructor':'greg@xurpas.com'
		}).insert()
