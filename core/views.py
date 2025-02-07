from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Accident, Branch
from .serializers import AccidentSerializer, BranchSerializer

class AccidentView(APIView):
    def post(self, request):
        data = request.data.get("data", {}).get("accidents", {}).get("items", [])
        branch_data = request.data.get("data", {}).get("currentSession", {}).get("branch", {})

        # if not data:
        #     return Response({"error": "Nenhum dado de acidente encontrado."}, status=status.HTTP_400_BAD_REQUEST)

        # Processa ou cria a filial (Branch)
        branch, _ = Branch.objects.get_or_create(
            id=branch_data["id"],
            defaults={
                "organizationId": branch_data["organizationId"],
                "name": branch_data["name"]
            }
        )
 
        created_accidents = []
        for accident_data in data:
            # Adiciona a filial ao JSON antes de serializar
            accident_data["branch"] = branch.id

            serializer = AccidentSerializer(data=accident_data)
            if serializer.is_valid():
                accident = serializer.save(branch=branch)
                created_accidents.append(serializer.data)
            else:
                print(serializer.errors)  # Para debug

        return Response({"created_accidents": created_accidents}, status=status.HTTP_201_CREATED)
