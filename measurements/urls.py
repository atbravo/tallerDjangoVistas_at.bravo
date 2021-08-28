from django.urls import path
from . import views

urlpatterns = [
    path('list/',views.get_measurements, name = 'measurementList'),
    #Recibe como parametro el id de la measurement buscada
    path('get/<int:measure_id>', views.get_single_measurement, name = 'measurement'),
    #Recibe como parametro el id de la measurement que se quiere eliminar
    path('delete/<int:measure_id>', views.delete_single_measurement, name = 'measurementDeleted'),
    #Recibe como parametro el id de la measurement a actualizar y los nuevos valores de "value" y "place"
    path('update/<int:measure_id>/<int:new_value>/<str:new_place>', views.update_single_measurement, name = 'measurementUpdated'),
]