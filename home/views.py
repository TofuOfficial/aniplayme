from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    return render(request, 'home.html')

# def get_anime(request):
    
#     return get_text