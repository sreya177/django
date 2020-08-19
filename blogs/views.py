from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import operator
def drinks(requests):
    return HttpResponse('Drink 3 L water everyday')
def foods(requests):
    return HttpResponse('dont eat junk food-it is high in salt')
