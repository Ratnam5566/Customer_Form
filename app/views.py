from django.shortcuts import render
from app.Forms import *
from django.http import HttpResponse

# Create your views here.
def cform(request):
    co=customerForm()
    d={'co':co}
    if request.method =='POST':
        cod=customerForm(request.POST)
        if cod.is_valid():
            n=cod.cleaned_data['First_Name']
            return HttpResponse(n)
    return render (request,'cform.html',d)