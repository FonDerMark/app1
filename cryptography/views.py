import os
from django.http import HttpResponse
from django.shortcuts import render

from .forms import CGForm


# Create your views here.
def index(request):
    if request.method == 'GET':
        form = CGForm()
        context = {
            'form': form,
        }
        return render(request, template_name='web/html/cryptocraphy.html', context=context)
    if request.method == 'POST':
        form = CGForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, template_name='web/html/cryptocraphy.html')
