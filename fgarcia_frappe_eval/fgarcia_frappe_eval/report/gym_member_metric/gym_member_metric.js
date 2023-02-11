// Copyright (c) 2023, Fernando Garcia and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Gym Member Metric"] = {
	"filters": [ {
		"fieldname" : "gym_member",
		"label" : "Gym Member",
		"fieldtype" : "Link",
		"options" : "Gym Member",
		"width" : "100",
		"reqd" : 0
	},
	{
		"fieldname" : "type",
		"label" : "metric Type",
		"fieldtype" : "Select",
		"options" : "WEIGHT IN KG\nBMI\nBODY FAT PERCENTAGE",
		"width" : "100",
		"reqd" : 0
	}]
};
