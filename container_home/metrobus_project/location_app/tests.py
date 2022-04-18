#from django.test import TestCase
from unittest import TestCase
from location_app.views import AvailableUnits

class LocationAppTest(TestCase):
    #Test for the AvailableUnits View
    #It should get a JSON with a list units
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
        pass
    
    def test_available_localities(self):
        pass
    
    def test_units_in_locality(self):
        pass

