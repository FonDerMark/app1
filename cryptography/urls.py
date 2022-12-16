from django.urls import path

import cryptography.views

urlpatterns = [
    path('', cryptography.views.index),
]