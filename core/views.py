from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Accident, Branch
from .serializers import AccidentSerializer, BranchSerializer

class AccidentView(APIView):
    def post(self, request):
        data = request.data.get("data", {}).get("accidents", {}).get("items", [])
        branch_data = request.data.get("data", {}).get("currentSession", {}).get("branch", {})

        # Verifica se há dados de acidentes
        if not data:
            return Response({"error": "Nenhum dado de acidente encontrado."}, status=status.HTTP_400_BAD_REQUEST)

        # Verifica se os dados da filial estão presentes
        if not branch_data:
            return Response({"error": "Dados da filial ausentes."}, status=status.HTTP_400_BAD_REQUEST)

        # Processa ou cria a filial (Branch)
        try:
            branch, _ = Branch.objects.update_or_create(
                id=branch_data["id"],
                defaults={
                    "organizationId": branch_data["organizationId"],
                    "name": branch_data["name"]
                }
            )
        except KeyError as e:
            return Response({"error": f"Erro ao processar dados da filial: falta a chave {str(e)}."}, status=status.HTTP_400_BAD_REQUEST)

        created_accidents = []
        for accident_data in data:
            # Adiciona a filial ao JSON antes de serializar
            accident_data["branch"] = branch.id

            # Verifica se o acidente já existe antes de tentar salvar
            existing_accident = Accident.objects.filter(id=accident_data["id"]).first()

            # Caso o acidente já exista, tenta atualizar
            if existing_accident:
                serializer = AccidentSerializer(existing_accident, data=accident_data, partial=True)
            else:
                serializer = AccidentSerializer(data=accident_data)

            if serializer.is_valid():
                try:
                    accident = serializer.save(branch=branch)
                    created_accidents.append(serializer.data)
                except Exception as e:
                    print(f"Erro ao salvar o acidente: {str(e)}")  # Log para depuração
                    return Response({"error": f"Erro ao salvar o acidente: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                print(f"Erros de validação para o acidente: {serializer.errors}")  # Log para depuração
                return Response({"error": f"Erro de validação: {serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)

        # Retorna os acidentes criados ou processados
        return Response({"created_accidents": created_accidents}, status=status.HTTP_201_CREATED)
    