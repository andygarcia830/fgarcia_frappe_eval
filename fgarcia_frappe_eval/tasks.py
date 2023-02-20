import frappe
from datetime import datetime
from datetime import timedelta


def weekly():
    email_class_report()

def daily():
    update_membership_status()


def email_class_report():
    # generate dates for the start and end of the past week
    print('START OF email_class_report()')
    end_date = datetime.now()
    start_date = end_date - timedelta(days = 7)
    dateFormat='%Y-%m-%d'

    baseSQL1='SELECT UNIQUE `tabUser`.email,`tabUser`.first_name from `tabGym Class Booking` INNER JOIN `tabGym Member` ON `tabGym Class Booking`.gym_member=`tabGym Member`.name INNER JOIN `tabGym Class` ON `tabGym Class`.name=`tabGym Class Booking`.gym_class INNER JOIN `tabUser` ON `tabGym Member`.name=`tabUser`.email'
    whereSQL1=f' WHERE `tabGym Class`.schedule > \'{start_date.strftime(dateFormat)}\' AND `tabGym Class`.schedule < \'{end_date.strftime(dateFormat)}\''
    
     
    SQL=baseSQL1+whereSQL1
    
    print('SQL='+SQL)

    result = frappe.db.sql(SQL)

    for item in result:
        print(f'ITEM {item}')
        email = item[0]
        print(email)
        baseSQL2='SELECT  `tabUser`.email, `tabGym Class Booking`.gym_class, `tabGym Class`.schedule from `tabGym Class Booking` INNER JOIN `tabGym Member` ON `tabGym Class Booking`.gym_member=`tabGym Member`.name INNER JOIN `tabGym Class` ON `tabGym Class`.name=`tabGym Class Booking`.gym_class INNER JOIN `tabUser` ON `tabGym Member`.name=`tabUser`.email'
        whereSQL2=f' WHERE `tabGym Class`.schedule > \'{start_date.strftime(dateFormat)}\' AND `tabGym Class`.schedule < \'{end_date.strftime(dateFormat)}\' AND `tabUser`.email=\'{email}\''
        SQL = baseSQL2+whereSQL2
        result2 = frappe.db.sql(SQL)
        subject=f'Gym Class Report for week {start_date.strftime(dateFormat)} to {end_date.strftime(dateFormat)}'
        body=f'Greetings {item[1]},\n\nHere are the Gym Classes that you have attended for the past week:\n\n'    
        for item2 in result2:
            print(f'ITEM2 {item2}')
            body+=item2[1]+'\n'
        print(subject)
        print(body)
        email_args = {
            "recipients": [item2[0]],
            "message": body,
            "subject": subject
            }
        frappe.sendmail(email_args)


def update_membership_status():
    result = frappe.get_list('Gym Member')
    now_date = datetime.now().date()
    for item in result:
        if item.subscription_end == None or item.subscription_start == None: continue
        if item.subscription_end < now_date:
            print(f'Subscription Ended! {item.name} {item.subscription}')
            item.subsciption=None
            item.subscription_start=None
            item.subscription_end=None
            item.status='INACTIVE'
            item.submit()
