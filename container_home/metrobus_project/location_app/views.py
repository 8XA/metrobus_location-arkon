from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from location_app.models import UnidadesModel
from location_app.serializers import UnidadesSerializer
from location_app.microbuses_information import get_units_information


class AvailableUnits(APIView):
    """
    This View returns a JSON with the labels of the available units.
    """
    def get(self, request):
        availables = UnidadesModel.objects.all() 
        serializer = UnidadesSerializer(availables, many=True)
        try:
            units_list = [unit['label'] for unit in serializer.data]
        except:
            units_list = []
        available_units = {
                "available_units": units_list
            }
        return Response(available_units, status=status.HTTP_201_CREATED)


class UnitLocation(APIView):
    pass


class AvailableLocalities(APIView):
    pass


class UnitsInLocality(APIView):
    pass


class FetchData(APIView):
    """
    This View adds or updates the microbuses units information in the database.
    It just need to be called by their Endpoint.
    """
    
    def get(self, request):
        #Gets a list of the units with their information
        data = get_units_information()
    
        serializer_data_sum = []
        #The units are added or updated one by one, because the action
        #can be different for each case.
        for unit in data:
            try:
                filtered_units = UnidadesModel.objects.filter(label=unit['label'])
                if len(filtered_units) == 0:
                    serializer = UnidadesSerializer(data=unit)
                else:
                    serializer = UnidadesSerializer(filtered_units[0], data=unit)

                if serializer.is_valid():
                    serializer.save()
                    serializer_data_sum.append(serializer.data)
            except:
                return Response("Los datos a registrar son incorrectos.", status=status.HTTP_400_BAD_REQUEST)
        
        #Return info
        serializer_data_sum.insert(0, 'Número de unidades insertadas/actualizadas: {}'.format(len(serializer_data_sum)))
        
        return Response(serializer_data_sum, status=status.HTTP_201_CREATED)

