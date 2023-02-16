from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='upload'),
    path('remove/<str:filename>/', remove, name='remove'),
]