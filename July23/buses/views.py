from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def func1(request):
    d={'buses':[{'name':'bus1','area':'Dharmavaram'},
        {'name':'bus2','area':'Ananthapur'},
        {'name':'bus3','area':'Pamidi'},
        {'name':'bus4','area':'Tadipatri'}]}
    return render(request,'buses.html',d)