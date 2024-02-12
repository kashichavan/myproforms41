How To create django forms:
---------------------------

Step 1)  create forms.py file innside the application

Step 2) first imports forms module to forms.py file

	from django import forms

step 3) create  a formclass with name that class need to inherit from forms.Form class

Step 4) inside your class describe the fields(form fields)


	class StudentForm(forms.Form):
    		name=forms.CharField(max_length=26)
    		age=forms.IntegerField()

Step 5) go to views and then create an object for form class

step 6) that obbject pass as value for key in dict

step 7)  go to html page use {{keyName}} it should be presentin html form tag

step 8) create submit button
