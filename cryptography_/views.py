import os
from pathlib import Path
import environ
from django.http import HttpResponse
from django.shortcuts import render

from .forms import CGForm

env = environ.Env(
    DEBUG=(bool, False)
)

BASE_DIR = Path(__file__).resolve().parent.parent

env.read_env(os.path.join(BASE_DIR, '.env'))

def index(request):
    if request.method == 'GET':
        context = {
            'form': CGForm,
        }
        print(env('HELLO'))
        return render(request, template_name='web/html/cryptography.html', context=context)
    if request.method == 'POST':
        form = CGForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            form.encoded = False
            form.save()
        return render(request, template_name='web/html/cryptography.html')
