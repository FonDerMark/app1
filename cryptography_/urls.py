from django.urls import path

import cryptography_.views

urlpatterns = [
    path('', cryptography_.views.index, name='cg'),
    path('encrypt/', cryptography_.views.test_logic, name='encrypt'),
    path('decrypt/', cryptography_.views.decrypt, name='decrypt'),
    path('download/<str:file_name>/', cryptography_.views.download, name='cg_download'),
]