import json

from django.shortcuts import render
from yndx_parse import YndxParse


def index(request):
    context = json.loads(get_weather())
    return render(request, 'web/html/parse/parse.html', context)


def get_weather(city='Лесной Свердловская') -> json:
    yp = YndxParse(city, save_json=False)
    return yp.get_weather()
