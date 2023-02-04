from django.urls import path

import cryptography_.views

urlpatterns = [
    path('', cryptography_.views.index, name='cg'),
]