from rest_framework.viewsets import ViewSet
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
                "Available units": units_list
            }
        return Response(available_units, status=status.HTTP_200_OK)


class UnitLocation(APIView):
    """
    This View returns a JSON with the location of the unit specified by the URL parameter.
    The location is given by the longitude and the latitude, also by the locality.
    The URL parameter has to be an integer number which is the ID/label of the unit.
    """
    def get(self, request, label):
        try:
            unit = UnidadesModel.objects.get(label=label)
            serializer = UnidadesSerializer(unit)

            only_location = serializer.data.copy()
            only_location.pop('updated')
            
            return Response(only_location, status=status.HTTP_200_OK)
        except:
            return Response("ID de unidad inexistente.", status=status.HTTP_404_NOT_FOUND)


class AvailableLocalities(APIView):
    """
    This View returns the list of the available localities.
    It no need parameters.
    """
    def get(self, request):
        try:
            availables = UnidadesModel.objects.all()
            serializer = UnidadesSerializer(availables, many=True)
            localities_list = list(set([unit['alcaldia'] for unit in serializer.data]))
            ordered_localities = sorted(localities_list, key=str.casefold)
        except:
            ordered_localities = []
        return Response({"Available localities": ordered_localities}, status=status.HTTP_200_OK)


class UnitsInLocality(APIView):
    """
    This View returns the list of the available units in the locality specified
    by the URL.
    The URL parameter is case insensitive, but you must pass accents, dots and
    spaces through itself.
    """
    def get(self, request, alcaldia):
        availables = UnidadesModel.objects.filter(alcaldia__iexact=alcaldia) 
        serializer = UnidadesSerializer(availables, many=True)
       
        locality = alcaldia
        if len(serializer.data) > 0:
            locality = serializer.data[0]['alcaldia']
        else:
            return Response('En estos momentos no hay registros para {}.'.format(alcaldia), 
                    status=status.HTTP_404_NOT_FOUND)
        try:
            units_in_locality = [unit['label'] for unit in serializer.data]
        except:
            units_in_locality = []
        available_units = {
                'Units in {}'.format(locality): units_in_locality
            }
        return Response(available_units, status=status.HTTP_200_OK)


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

