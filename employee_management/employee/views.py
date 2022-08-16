import csv
from email import header
import json
from unittest import result
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from csv import writer,reader
import os
import pandas as pd


@api_view(['POST'])
def add_employee(request): 
    '''add a new employee row into csv file'''
    
    header = ['Employee_id', 'Firstname','Lastname', 'Designation']
    filename = './employee_file.csv'
    if os.path.exists(filename):
        with open(filename, 'a') as file:
            csv_writer = writer(file, lineterminator='\n')         
            csv_writer.writerow(request.data.values())
    else:
        with open(filename, 'w') as file:
            csv_writer = writer(file, lineterminator='\n')
            csv_writer.writerow(header) 
            csv_writer.writerow(request.data.values())
            
    return Response("success")


@api_view(['GET'])
def get_employees(request):
    '''get all employee rows from csv file'''
    
    filename = './employee_file.csv'
    result = pd.read_csv(filename)
    return Response(result.to_dict())


@api_view(['GET'])
def get_employee_by_id(request, employee_id):
    '''get particular employee row'''
    
    filename = './employee_file.csv'
    data = pd.read_csv(filename, index_col ="Employee_id")
    employee_details = data.loc[employee_id]
    print(type(employee_details))
    return Response(employee_details.to_dict())


@api_view(['PUT'])
def update_employee(request, employee_id, column_name):
    '''update a particular employee field'''
    
    data = pd.read_csv('./employee_file.csv')
    index = data.index[data['Employee_id']==employee_id].to_list()
    # print(data.loc[2, column_name])
    data.loc[index[0], column_name] = request.data.get(column_name)
    data.to_csv('./employee_file.csv',index=False)
    return Response("Successfully updated")


    


# @api_view(['POST'])
# def add_employee(request):   
#     print(request.data)
#     print(type(request.data))
#     header = ['Employee_id', 'Firstname','Lastname', 'Designation']
#     filename = './employee_file.csv'
#     if os.path.exists(filename):
#         with open(filename, 'a') as file:
#             csv_writer = writer(file, lineterminator='\n')         
#             csv_writer.writerows(request.data)
#     else:
#         with open(filename, 'w') as file:
#             csv_writer = writer(file, lineterminator='\n')
#             csv_writer.writerow(header) 
#             csv_writer.writerows(request.data)
            
#     return Response("success")


# @api_view(['GET'])
# def get_employees(request):
#     filename = './employee_file.csv'
#     result = pd.read_csv(filename)
#     return Response(result.to_string())

# @api_view(['GET'])
# def get_employee_by_id(request, employee_id):
#     filename = './employee_file.csv'
#     data = pd.read_csv(filename, index_col ="Employee_id")
#     employee_details = data.loc[employee_id]
#     return Response(employee_details.to_string())

# @api_view(['PUT'])
# def update_employee(request, employee_id, column_name):
#     data = pd.read_csv('./employee_file.csv', index_col="Employee_id")
#     data.loc[employee_id, column_name] = request.data[0]
#     data.to_csv('./employee_file.csv')
#     return Response("Successfully updated")


