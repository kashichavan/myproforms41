from django.shortcuts import render
from .forms import StudentForm
from .models import Student
# Create your views here.

def home(request):
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            # name=request.POST['name'] 
            # age=request.POST['age']
            name=form.cleaned_data['name']
            age=form.cleaned_data['age']
            data=Student.create(name=name,age=age)
        




    else:
        form=StudentForm()

    return render(request,'home.html',{'form':form})
