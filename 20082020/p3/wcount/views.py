from django.shortcuts import render
import operator
from django.http import HttpResponse
# Create your views here.
def home(requests):
    return render(requets, 'wcount/home.html')
def count(requests):
    mytext=requests.GET['fulltext']
    wcount=len(mytext.split())
    ##write logic
    ########
    mylist=[('rn1','sreya'),('rn2','sunitha')]
    return render(requets, 'wcount/count.html',{'mycount':'wcount','yourlist':mylist})
