from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html',{
        'name':'Sanjeev!'
    })
def add(request):
    num1=request.GET['num1']
    num2=request.GET['num2']
    val=int(num1)+int(num2)
    return render(request,'result.html',{
        'result':val
    })
