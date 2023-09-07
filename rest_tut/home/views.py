from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, redirect
from .models import *
from .serializer import *

#  Its Sample API for checking
@api_view()
def hello_world(request):
    return Response({"message": "Hello, world!"})

# To get a records in Json formate by using thounder Client or postman or etc
@api_view(['GET'])
def get_students(request):
    response={'status':200}
    student_objs = Student.objects.all()
    serializer = StudentSerializer(student_objs, many=True)
    response['data'] = serializer.data
    return Response(response)


# To get the record on front end part with the help of html/js page
# #With this setup, when you access the /get_students/ endpoint, it will render the students.html template, 
# #fetch data from the get_students API, and display the list of students in the HTML table

# # @api_view(['GET'])
# # def get_students(request):
# #     student_objs = Student.objects.all()
# #     serializer = StudentSerializer(student_objs, many=True)
# #     students = serializer.data
# #     return render(request, 'students.html', {'students': students})



# Registration page to fill the data
def registration_form(request):
    return render(request,'registration.html') 


# After registration these API is called and 
@api_view(['POST'])
def post_students(request):
    response={'status':200}
    data = request.data
    serializer = StudentSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return redirect('registration_form')
        return Response(response)
    return Response(serializer.errors)
    







