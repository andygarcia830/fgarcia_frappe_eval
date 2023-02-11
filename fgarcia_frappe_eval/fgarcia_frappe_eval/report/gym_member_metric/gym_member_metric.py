# Copyright (c) 2023, Fernando Garcia and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns = get_columns()
	data = get_data(filters)
	return columns, data



def get_columns():
	columns=[
		"Gym Member:Link/Gym Member:200",
		"Metric Type:Data:200",
		"Metric Value:Float:200",
		"Date Taken:Date:200"
	]

	return columns

def get_data(filters):
	
	conditions=' WHERE 1=1'
	if filters.get("gym_member") : 
		conditions +=f' AND gym_member=\'{filters.get("gym_member")}\'' 
	if filters.get("type") : 
		conditions +=f' AND type=\'{filters.get("type")}\'' 

	SQL="SELECT gym_member, type, value, date_taken FROM `tabGym Member Metric`"+conditions
	result = frappe.db.sql(SQL)
	print(result)
	#data=[['andy@xurpas.com','WEIGHT IN KG',71.0,'2023-02-07']]
	data=[]
	for item in result:
		it =[item[0],item[1],item[2],item[3]]
		data.append(it)

	return data