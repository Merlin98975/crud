
from django.shortcuts import render
from django.db import models
from django.shortcuts import render
from .models import Employee
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.


''' function create is used as post method ,which creates the details of the employee and posts in the database'''
@csrf_exempt
def create(request):
    if request.method == 'POST':
        i = json.loads(request.body.decode('utf-8'))
        p=Employee.objects.create(
             emp_name=i['emp_name'],
             dept=i['dept'],
             email=i['email'],
             salary=i['salary'],
             blood_group=i['blood_group']
         )
    else:
        pem = 'method not allowed'
    return JsonResponse({'Response':i})

''' function read is used as get method ,which is used to get all employee details'''
@csrf_exempt
def read(request):#get all the objects
    if request.method == 'GET':
        emp = Employee.objects.all()
        l=[]
        for i in emp:
            var={
             'id':i.id,
             'emp_name':i.emp_name,
             'dept':i.dept,
             'email':i.email,
             'salary':i.salary,
             'blood_group':i.blood_group
             }
            l.append(var)
    else:
        pem = 'method not allowed'
    return JsonResponse({'Response':l})

''' function read_one is also used as get method which specifically retrives single employee details by using primary key'''
@csrf_exempt
def read_one(request,pk):#get single object
    if request.method == 'GET':
        emp = Employee.objects.filter(pk=pk)
        #l=[]
        for i in emp:
            var={
             'id':i.id,
             'emp_name':i.emp_name,
             'dept':i.dept,
             'email':i.email,
             'salary':i.salary,
             'blood_group':i.blood_group
             }
        # l.append(var)
    else:
        pem = 'method not allowed'
    return JsonResponse({'Response':var})

''' function update is used to update the existing employee details to change their data by using primary key'''
@csrf_exempt
def update(request,pk):
    if request.method == 'PUT':
       emp = Employee.objects.get(pk=pk)
       pem = json.loads(request.body)
       emp.emp_name = pem['emp_name']
       emp.dept = pem['dept']
       emp.email = pem['email']
       emp.salary = pem['salary']
       emp.blood_group = pem['blood_group']
       emp.save()
    else:
        pem = 'method not allowed'
    return JsonResponse({'Response':pem})

''' function delete is used the particular employee detail by using primary key'''
@csrf_exempt
def delete(request,pk):
    if request.method == 'PUT':
        emp = Employee.objects.get(pk=pk)
        emp.delete()
    else:
        pem = 'message not allowed'
        msg = {'Response': f'{pk} message successfully deleted'}
    return JsonResponse(msg)






