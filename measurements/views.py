from .logic.logic_measurements import get_all_measurements, get_measurement, delete_measurement,update_measurement
from django.http import HttpResponse
from django.core import serializers
import json

def get_measurements(request):
    """retorna la lista de los measurements en formato json"""
    measurements = get_all_measurements()
    measurements_list = serializers.serialize('json',measurements)
    return  HttpResponse(measurements_list, content_type='application/json')

def get_single_measurement(request, measure_id):
    """retorna en formato json la measurement con el id buscado """
    measurements = get_measurement(measure_id)
    measurements_list = serializers.serialize('json',measurements)
    return  HttpResponse(measurements_list, content_type='application/json')

def delete_single_measurement(request, measure_id):
    """retorna en formato json la lista de measurements despues de eliminar la medida con id dado"""
    deleted = delete_measurement(measure_id)
    measurements_list = serializers.serialize('json', deleted)
    measurements_list = json.dumps({"MEASUREMENTS RESTANTES:" : measurements_list })
    return HttpResponse(measurements_list, content_type='application/json')

def update_single_measurement(request, measure_id, new_value, new_place):
    """actualiza y retorna en formato json la informacion de la measurement con id dado"""
    updated = update_measurement(measure_id, new_value, new_place)
    updated_json = serializers.serialize('json',updated)
    return HttpResponse(updated_json, content_type='application/json')