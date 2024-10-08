from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def func1(request):
    d={'movies':[{'name':'pokiri','year':2005,'director':'Puri Jagannath','rating':8,'genre':'Drama'},
                 {'name':'Avengers Endgame','year':2019,'director':'Joe Russo','rating':9,'genre':'Action'},
                 {'name':'RRR','year':2022,'director':'Rajamouli','rating':9,'genre':'Thriller'},
                {'name':'Hum Saath Saath hai','year':2001,'director':'Rajamouli','rating':9,'genre':'Family Drama'}]}
    return render(request,'file1.html',d)