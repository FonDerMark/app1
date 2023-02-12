import io
import os

import pyAesCrypt
from django.core.files import File
from django.core.files.storage import FileSystemStorage
from django.http import FileResponse
from django.shortcuts import render

from pet_project_1.settings import MEDIA_ROOT
from .forms import CGForm

APP_STORAGE = os.path.join(MEDIA_ROOT, 'cryptography')
fss = FileSystemStorage(location=APP_STORAGE)


def index(request):
    if request.method == 'GET':
        context = {
            'form': CGForm,
        }
        return render(request, template_name='web/html/cryptography/cryptography.html', context=context)
    if request.method == 'POST':
        form = CGForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            form.encoded = False
            form.save()
        return render(request, template_name='web/html/cryptography/cryptography.html')


def encrypt(request):
    if request.method == 'GET':
        return render(request, 'web/html/cryptography/crypt.html')
    if request.method == 'POST' and request.FILES['file']:
        file = File(request.FILES['file'])
        password = request.POST['password']
        fss.save(file.name, file)
        path_to_file = os.path.join(APP_STORAGE, file.name)
        pyAesCrypt.encryptFile(path_to_file, path_to_file + '.aes', password)
        return render(request, 'web/html/cryptography/crypt.html', context={'file': file.name + '.aes'})


def decrypt(request):
    if request.method == 'GET':
        return render(request, 'web/html/cryptography/crypt.html')
    if request.method == 'POST' and request.FILES['file']:
        file = File(request.FILES['file'])
        file.name = file.name + '_fordecrypt'
        password = request.POST['password']
        fss.save(file.name, file)
        path_to_file = os.path.join(APP_STORAGE, file.name)
        pyAesCrypt.decryptFile(path_to_file, path_to_file, password)
        return render(request, 'web/html/cryptography/crypt.html', context={'file': file.name + '.aes'})


def download(request, file_name):
    path_to_file = os.path.join(APP_STORAGE, file_name)
    return FileResponse(open(path_to_file, 'rb'))


def test_logic(request):
    if request.method == 'GET':
        return render(request, 'web/html/cryptography/test_logic.html')
    elif request.method == 'POST':
        bufferSize = 64 * 1024
        file = File(request.FILES['file'])
        fOut = io.BytesIO()
        fss.save(file.name, file)
        password = request.POST['password']
        print(password)
        if request.POST.get('encrypt-button'):
            pyAesCrypt.encryptFile(file.read(), fOut, password, bufferSize)
            return FileResponse(fOut, as_attachment=True, filename=file.name)
        elif request.POST.get('decrypt-button'):
            pass
            # ctlen = len(fIn.getvalue())
            # pyAesCrypt.decryptStream(fIn, fDec, password, bufferSize, ctlen)
            # return FileResponse(fOut, as_attachment=True, filename=file.name)

