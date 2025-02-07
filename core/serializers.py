from rest_framework import serializers
from .models import Accident, Branch

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'

class AccidentSerializer(serializers.ModelSerializer):
    social_security_affiliation = serializers.CharField(required=False, allow_null=True)
    branch = serializers.PrimaryKeyRelatedField(queryset=Branch.objects.all())
    class Meta:
        model = Accident
        fields = '__all__'

    def create(self, validated_data):
        branch = validated_data.pop("branch", None)
        # Verifica se já existe um acidente com o mesmo summary e data
        accident, created = Accident.objects.get_or_create(
            summary=validated_data.get("summary"),
            date=validated_data.get("date"),
            defaults={**validated_data, "branch": branch}
        )
        return accident
