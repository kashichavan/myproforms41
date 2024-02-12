from django.shortcuts import render
from .forms import StudentForm
# Create your views here.

def home(request):
    f1=StudentForm()
    d={'form':f1}
    return render(request,'home.html',context=d)
