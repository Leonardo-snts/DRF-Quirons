from rest_framework import serializers
from .models import Accident

class AccidentSerializer(serializers.ModelSerializer):
    social_security_affiliation = serializers.CharField(required=False, allow_null=True)
    class Meta:
        model = Accident
        fields = '__all__'

    def create(self, validated_data):
        # Verifica se já existe um acidente com o mesmo summary e data
        accident, created = Accident.objects.get_or_create(
            summary=validated_data.get("summary"),
            date=validated_data.get("date"),
            defaults=validated_data
        )
        return accident
