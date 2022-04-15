from rest_framework import serializers

from location_app.models import UnidadesModel


class UnidadesSerializer(serializers.ModelSerializer):
    """
    Basic serializer handling all the UnidadesModel reading and writing
    """

    class Meta:
        model = UnidadesModel
        fields = "__all__"

