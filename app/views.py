from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from app.models import *
from app.forms import *


def create_student(request):
    ESFO = StudentForm()
    d = {'ESFO':ESFO}
    
    if request.method=='POST':
        SDFO=StudentForm(request.POST)
        if SDFO.is_valid():
            SDFO.save()
            return HttpResponse('create_student is done')
        else:
            return HttpResponse('in valide data')
    return render(request,'create_student.html',d)





