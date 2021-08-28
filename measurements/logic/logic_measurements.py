from ..models import Measurement

def get_all_measurements():
    """returns a list of all measurements"""
    measurements = Measurement.objects.all()
    return measurements

def get_measurement(measure_id):
    """returns the measurement with the id given"""
    m = Measurement.objects.filter(id = measure_id)
    return m

def delete_measurement(measure_id):
    """Deletes the measurement with the given id and returns the list of measurements remaining"""
    m = Measurement.objects.filter(id = measure_id)
    m.delete()
    return Measurement.objects.all()

def update_measurement(measure_id, new_value, new_place):
    """Updates and returns the measurement with id given using the information given as parameters"""
    m = Measurement.objects.filter(id = measure_id)
    m.update(value = new_value, place = new_place)
    return m