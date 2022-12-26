import os
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method == 'GET':
        context = {
        }
        return render(request, template_name='web/html/cryptocraphy.html', context=context)
    if request.method == 'POST':
        return render(request, template_name='web/html/cryptocraphy.html')
