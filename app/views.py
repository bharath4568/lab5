from django.shortcuts import render
from django.http import HttpResponse


def json_response(request):
    return HttpResponse('{"Message": "Hello World!"}')

