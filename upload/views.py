import os
from django.shortcuts import render, redirect

from pet_project_1.settings import MEDIA_ROOT

APP_ROOT = os.path.join(MEDIA_ROOT, 'files')


# Create your views here.
def index(request):
    if request.method == 'GET':
        try:
            context = {
                'files': os.scandir(APP_ROOT),
            }
        except:
            pass
        return render(request, 'web/html/upload/upload.html', context)
    if request.method == 'POST':
        if not os.path.exists(APP_ROOT):
            os.mkdir(APP_ROOT)
        file = request.FILES['file']
        with open(os.path.join(APP_ROOT, file.name), 'wb') as f:
            f.write(file.read())
        return redirect('upload')


def remove(request, filename):
    os.remove(os.path.join(APP_ROOT, filename))
    return redirect('upload')
