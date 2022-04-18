#from django.test import TestCase
from unittest import TestCase
from location_app.models import UnidadesModel
from location_app.views import AvailableUnits
from location_app.views import UnitLocation

class LocationAppTest(TestCase):
    #Test for the AvailableUnits View
    def test_available_units(self):
        view_instance = AvailableUnits()
        get_method = view_instance.get(None)
        units_list = get_method.data['available_units']
        units_validation = [isinstance(unit, int) for unit in units_list]  
        non_repeated_units = list(set(units_list))

        #All the labels/ID units are integers
        assert all(units_validation)
        #Every unit ID is unique
        assert len(units_list) == len(non_repeated_units)
        #MEthod return 200 OK status
        assert get_method.status_text == 'OK'

    def test_unit_location(self):
        view_instance = UnitLocation()
        LABEL = 112
        FIELDS_NUM = 4
        get_method = view_instance.get(None, LABEL)
        if 2 > len(UnidadesModel.objects.filter(label=LABEL)) > 0:
            #It has only the four valid fields
            assert len(get_method.data) == FIELDS_NUM
            assert len([field in ['label', 'longitude', 'latitude', 'alcaldia'] for field in get_method.data]) == FIELDS_NUM
            #Verifies if the data type is right
            assert isinstance(get_method.data['label'], int)
            assert isinstance(get_method.data['longitude'], str)
            assert isinstance(get_method.data['latitude'], str)
            assert isinstance(get_method.data['alcaldia'], str)
            #HTTP Response is OK
            assert get_method.status_text == 'OK'
        else:
            assert get_method.status_text == 'Not Found'
    
    def test_available_localities(self):
        pass
    
    def test_units_in_locality(self):
        pass

