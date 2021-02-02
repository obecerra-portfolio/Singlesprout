# Validation for cases
import datetime
import json
import re

import phonenumbers


def validationSuite(content):
    
    flag = True
    message = ''
    mainJson = json.loads(content)
    
    try:
        for jsonObj in mainJson:
            if("full_name" in jsonObj):
                if validateName(jsonObj['full_name']) != True:
                    flag = False
                    message = 'Please have name in format \'John Doe\''
            else:
                flag = False
                message = 'Please include name field'
            
            if("phone" in jsonObj):
                if validatePhone(jsonObj['phone']) != True:
                    flag = False
                    message = 'Phone format (xxx) xxx-xxxx'
            
            if("email_address" in jsonObj):
                if validateEmail(jsonObj['email_address']) != True:
                    flag = False
                    message = 'email format x@x.com'
            
            if("employments" in jsonObj):
                try:
                    for employee in jsonObj['employments']:
                        if("company_name" in employee):
                            if validateDate(employee['start_date']) != True:
                                flag = False
                                message = 'date format yyyy-mm-dd'
                            if validateDate(employee['end_date']) != True:
                                flag = False
                                message = 'date format yyyy-mm-dd'
                        else:
                            flag = False
                            message = 'company_name missing'
                except TypeError:
                    flag = False
                    message = 'EMPLOYMENT JSON IS INCORRECT FORMAT :: [{A:A},{B:B},...]'
                        
        
        return flag,message
    except TypeError:
        flag = False
        message = 'JSON IS INCORRECT FORMAT :: [{A:A},{B:B},...]'
        
    
def validateName(fullName):
    if not fullName:
        return False

    fullName = fullName.strip()
    if ' ' in fullName:
        if fullName.replace(" ", "").isalpha():
            return True
        else:
            return False
    else:
        return False

def validatePhone(phone):
    phone = ''.join(e for e in phone if e.isalnum())
    phone = '+1' + phone
    phone = phonenumbers.parse(phone, None)
    if phonenumbers.is_possible_number(phone):
        return True
    return False

def validateEmail(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if(re.search(regex,email)):  
        return True
    else:  
        return False  

def validateDate(date):
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
        return True
    except ValueError:
        return False
    