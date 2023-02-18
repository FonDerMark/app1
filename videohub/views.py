from django.shortcuts import render, redirect
from .forms import FilmsForm
from .models import Films

from pet_project_1.settings import MEDIA_ROOT

# Create your views here.
def index(request):
    if request.method == 'GET':
        form = FilmsForm()
        context = {
            'form': form,
            'films': Films.objects.all(),
            'media_root': MEDIA_ROOT,
        }
        return render(request, 'web/html/videohub/videohub.html', context)
    elif request.method == 'POST':
        form = FilmsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('vh')


def remove_video(request, film_id):
    Films.objects.get(pk=film_id).delete()
    return redirect('vh')
