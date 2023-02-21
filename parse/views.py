from yndx_parse import YndxParse
from django.http import JsonResponse


def index(request):
    yp = YndxParse('Лесной Свердловская', save_json=False)
    print(yp.get_weather())
    return JsonResponse(yp.get_weather(), safe=False, charset='utf-8')


def json_weather(request, city='Лесной Свердловская'):
    yp = YndxParse(city, save_json=False)
    print(yp.get_weather())
    return JsonResponse(yp.get_weather(), safe=False, charset='utf-8')
