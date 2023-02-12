import os

from cryptography.fernet import Fernet
from django.http import FileResponse
from django.shortcuts import render, redirect

from pet_project_1.settings import MEDIA_ROOT

APP_STORAGE = os.path.join(MEDIA_ROOT, 'cryptography')


def index(request):
    if request.method == 'GET':
        return render(request, 'web/html/cryptography/cryptography.html')
    else:
        with open(os.path.join(APP_STORAGE, 'crypto.key'), 'r') as f:
            key = f.read()
            t_file = os.path.join(APP_STORAGE, 'temp')
            file = request.FILES['file']
            fernet = Fernet(key)
            if request.POST.get('encrypt-button'):
                with open(t_file, 'wb') as f:
                    f.write(fernet.encrypt(file.read()))
                fOut = open(t_file, 'rb+')
                return FileResponse(fOut, as_attachment=True, filename=file.name)
            elif request.POST.get('decrypt-button'):
                with open(t_file, 'wb') as f:
                    f.write(fernet.decrypt(file.read()))
                fOut = open(t_file, 'rb+')
                return FileResponse(fOut, as_attachment=True, filename=file.name)
            else:
                return redirect('cg')


def key_gen(key_name='crypto.key'):
    key_path = os.path.join(APP_STORAGE, key_name)
    with open(key_path, 'wb') as f:
        f.write(Fernet.generate_key())


if __name__ == '__main__':
    key_gen()
