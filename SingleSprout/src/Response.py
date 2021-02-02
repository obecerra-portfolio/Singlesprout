# Response Object

import json
from _overlapped import NULL

def createResponse(content):
    keys = []
    response = []
    mainJson = json.loads(content)
    
    for jsonObj in mainJson:
        if jsonObj['full_name'] in keys:
            foundObj = retrieveObject(response, jsonObj['full_name'])
            if("phone" in jsonObj):
                if jsonObj['phone'] not in foundObj['phone_numbers']:
                    foundObj['phone_numbers'].append(jsonObj['phone'])
            if("email_address" in jsonObj):
                if jsonObj['email_address'] not in foundObj['emails']:
                    foundObj['emails'].append(jsonObj['email_address'])
            if("employments" in jsonObj):
                if("employments" in foundObj):
                    foundObj['employments'] = mergeEmploymentHistory(jsonObj, foundObj)
                else:
                    foundObj['employments'] = jsonObj['employments']
        else: 
            keys.append(jsonObj['full_name'])
            response.append(createFinalObject(jsonObj))
            
    return response

def mergeEmploymentHistory(mainObj, resultObj):
    return resultObj['employments'] + [x for x in mainObj['employments'] if x not in resultObj['employments']]

def retrieveObject(response, name):
    first, last = normalizeResponseName(name)
    for jsonObj in response:
        if first == jsonObj['first_name']:
            if last == jsonObj['last_name']:
                return jsonObj
    
def normalizeResponseName(name):
    name = name.split()
    firstName = name[0]
    lastName = name[1]
    
    return firstName, lastName

def createFinalObject(jsonObj):
    firstName, LastName = normalizeResponseName(jsonObj['full_name'])
    responseObj = {'first_name': firstName, 'last_name': LastName}
            
    if("phone" in jsonObj):
        phoneList = []
        phoneList.append(jsonObj['phone'])
        responseObj['phone_numbers'] = phoneList
                
    if("email_address" in jsonObj):
        emailList = []
        emailList.append(jsonObj['email_address'])
        responseObj['emails'] = emailList
            
    if("linkedin_username" in jsonObj):
        responseObj['linkedin_username'] = jsonObj['linkedin_username']
                
    if("employments" in jsonObj):
        employmentArr = []
                
        for employee in jsonObj['employments']:
            employmentArr.append(addEmploymentField(employee))
                    
        responseObj['employments'] = employmentArr
            
    return responseObj

def addEmploymentField(employee):
    employmentObj = {'company_name': employee['company_name']}
    employmentObj['job_title'] = employee['job_title']
    employmentObj['start_date'] = employee['start_date']
    employmentObj['end_date'] = employee['end_date']
    
    return employmentObj