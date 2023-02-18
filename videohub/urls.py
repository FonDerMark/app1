from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='vh'),
    path('remove/<int:film_id>', remove_video, name='vh_remove'),
]