from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    response = """
    <h1> Hello! This is my first Djano application.</h1>

    <ul>
        <li>This is a list item!</li>
        <li> This is the second list item!</li>
    </ul>

    """

    return HttpResponse(response)

def detail(request):
    return HttpResponse("<h1>This is the detail view!</h1>")

def add(request):
    return HttpResponse("<h1>This is the add view!")

