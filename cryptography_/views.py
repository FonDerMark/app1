import os

import pyAesCrypt
from cryptography.fernet import Fernet
from django.core.files import File
from django.http import FileResponse
from django.shortcuts import render

from pet_project_1.settings import MEDIA_ROOT

from .forms import CGForm

APP_STORAGE = os.path.join(MEDIA_ROOT, 'cryptography')


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
        path_to_file = os.path.join(APP_STORAGE, file.name)
        pyAesCrypt.decryptFile(path_to_file, path_to_file, password)
        return render(request, 'web/html/cryptography/crypt.html', context={'file': file.name + '.aes'})


def download(request, file_name):
    path_to_file = os.path.join(APP_STORAGE, file_name)
    return FileResponse(open(path_to_file, 'rb'))


def test_logic(request):
    if request.method == 'GET':
        return render(request, 'web/html/cryptography/test_logic.html')
    else:
        t_file = os.path.join(APP_STORAGE, 'temp')
        file = request.FILES['file']
        fernet = Fernet(key.read())
        if request.POST['encrypt-button']:
            with open(t_file, 'rb+') as f:
                encrypted_file = fernet.encrypt(file.read())
                f.write(encrypted_file)
                return FileResponse(f, as_attachment=True, filename=file.name)
        elif request.POST['decrypt-button']:
            print('de')


def key_gen(key_name='crypto.key'):
    key_path = os.path.join(APP_STORAGE, key_name)
    with open(key_path, 'wb') as f:
        f.write(Fernet.generate_key())


if __name__ == '__main__':
    key_gen()
