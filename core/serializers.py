from rest_framework import serializers
from .models import Accident, Branch

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'

class AccidentSerializer(serializers.ModelSerializer):
    branch = serializers.PrimaryKeyRelatedField(queryset=Branch.objects.all())
    icd_code = serializers.CharField(allow_null=True, required=False)
    person_age = serializers.IntegerField(allow_null=True, required=False)
    person_gender = serializers.CharField(allow_null=True, required=False)
    class Meta:
        model = Accident
        fields = '__all__'

    def create(self, validated_data):
        branch = validated_data.pop("branch", None)
        
        # Captura os dados pessoais do JSON
        person_data = self.initial_data.get('person', {})
        validated_data['person_age'] = person_data.get('age', None)
        validated_data['person_gender'] = person_data.get('gender', None)
        
        # Captura o código ICD do JSON
        icd_data = self.initial_data.get('icd', {})
        validated_data['icd_code'] = icd_data.get('code', None)
       
        # Verifica se já existe um acidente com o mesmo id e data
        accident, created = Accident.objects.update_or_create(
            summary=validated_data.get("id"),
            # date=validated_data.get("date"),
            defaults={**validated_data, "branch": branch}
        )
        
        return accident
