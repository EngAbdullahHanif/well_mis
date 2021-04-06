from django.shortcuts import render, redirect
from tablib import Dataset
  
from django.http import HttpResponse
from .resources import MemberResource
from .models import Well

 
 
def export(request):
    member_resource = MemberResource()
    dataset = member_resource.export()
    #response = HttpResponse(dataset.csv, content_type='text/csv')
    #response['Content-Disposition'] = 'attachment; filename="member.csv"'
    #response = HttpResponse(dataset.json, content_type='application/json')
    #response['Content-Disposition'] = 'attachment; filename="persons.json"'
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="persons.xls"'
    return response

def simple_upload(request):
    if request.method == 'POST':
        person_resource = MemberResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read(),format='xlsx')
        #print(imported_data)
        for data in imported_data:
        	print(data[1])
        	value = Well(
        		data[0],
        		data[1],
        		 data[2],
        		 data[3]
        		)
        	value.save()       
        
        result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
           person_resource.import_data(dataset, dry_run=False)  # Actually import now

    return request