from django.shortcuts import render
from django.http import JsonResponse  # Import JsonResponse

# Create a view to return the "Hello World" JSON response
def hello_world(request):
    return JsonResponse({"Message": "Hello World!"})


# Create your views here.
