from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from location_app.models import UnidadesModel
from location_app.serializers import UnidadesSerializer
from location_app.microbuses_information import get_units_information


class AvailableUnits(APIView):
    pass


class UnitLocation(APIView):
    pass


class AvailableLocalities(APIView):
    pass


class UnitsInLocality(APIView):
    pass


class FetchData(APIView):
    
    def get(self, request):

        data = get_units_information()
        serializer = UnidadesSerializer(data=data, many=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def __update(self, request):
        pass

