from django.shortcuts import render
from .models import*
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


from django.views.generic import CreateView
from rest_framework import views

@csrf_exempt
def add_image(requests):
    data = json.loads(requests.body)
    try:
        user_name = User.objects.get(user_name=data['user_name'],password=data['password'])  # enater technician code
    except:
        return JsonResponse({'response': {"response_code": '500', "message": "Invalid User!!!"}})
    new_image,c = MainPage.objects.get_or_create(name=data['name'],description=data['description'],
                                                rating=data['rating'],product_image=data['product_image'])
    new_image.save()  #save contract price
    return JsonResponse({'response': {"response_code": '200', 'message':"Image Added Succesfully"}})

# Create your views here.
def get_all(request):
    pipes = MainPage.objects.all()
    data_array=[]
    for data in pipes:
        data_details = {}
        data_details['Id'] = data.page_id
        data_details['Name'] = data.name
        data_details['Description'] = data.description
        data_details['Image'] = data.product_image
        data_details['Rating'] = data.rating
        data_array.append(data_details)
    return JsonResponse({'response': {"response_code": '200', 'data': data_array}})

# api to get technician details and edit the technician
@csrf_exempt
def get_by_id(request):
    data = json.loads(request.body)
    try:
        pipes = MainPage.objects.get(pk=data['id'])
    except:
        return JsonResponse({'response': {"response_code": '500', 'error': "Invalid ID"}})
    data_details = {}
    data_details['Name'] = pipes.name
    data_details['Description'] = pipes.description
    data_details['Image'] = pipes.product_image
    data_details['Rating'] = pipes.rating
    return JsonResponse({'response': {"response_code": '200', 'data': data_details}})

