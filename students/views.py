from django.shortcuts import render
from django.http import HttpResponse


def students(requests):
    students = [
        {'id':1 , 'name': 'korede jerry', 'age': 15}
    ]
    return HttpResponse(students)