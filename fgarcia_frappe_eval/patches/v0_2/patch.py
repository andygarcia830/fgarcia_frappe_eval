import frappe

def execute():
   
    SQL='SET SQL_SAFE_UPDATES=0;UPDATE `tabGym Class` set published=0;SET SQL_SAFE_UPDATES=1'
    frappe.db.sql(SQL)

    