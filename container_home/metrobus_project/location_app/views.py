from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from location_app.models import UnidadesModel
from location_app.serializers import UnidadesSerializer


class AvailableUnits(APIView):
    pass


class UnitLocation(APIView):
    pass


class AvailableLocalities(APIView):
    pass


class UnitsInLocality(APIView):
    pass


class FetchData(APIView):
    pass

