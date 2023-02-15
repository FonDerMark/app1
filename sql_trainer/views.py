from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method == 'GET':
        return render(request, 'web/html/sql_trainer/sql_trainer.html')