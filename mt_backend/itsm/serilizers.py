from rest_framework import serializers
from itsm.models import Incident


class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = "__all__"


class SearchSerializer(serializers.ModelSerializer):
    rank = serializers.FloatField()  # Assuming rank is a FloatField
    headline = serializers.CharField()

    class Meta:
        model = Incident
        fields = '__all__'
