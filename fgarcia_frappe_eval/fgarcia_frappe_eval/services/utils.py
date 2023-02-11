import frappe

@frappe.whitelist()
def fetch_details(email):
	user = frappe.get_doc('User',email)
	details={}
	details['first_name']=user.first_name
	details['last_name']=user.last_name
	details['mobile_no']=user.mobile_no
	details['email']=user.email
	details['location']=user.location
	details['gender']=user.gender
	details['birth_date']=user.birth_date
	print(f'\n\nDETAILS={details}')
	return details
	