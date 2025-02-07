from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AccidentSerializer

class AccidentView(APIView):
    def post(self, request, *args, **kwargs):
        print("JSON recebido:", request.data)  # Debug

        accident_data = request.data.get("data", {}).get("accidents", {}).get("items")

        if accident_data is None:
            return Response({"error": "Formato de JSON inválido"}, status=status.HTTP_400_BAD_REQUEST)

        # if not accident_data:
        #     return Response({"message": "Nenhum acidente encontrado", "accidents": []}, status=status.HTTP_200_OK)

        accidents_created = []
        for accident in accident_data:
            print("Processando acidente:", accident)  # Debug
            serializer = AccidentSerializer(data=accident)
            if serializer.is_valid():
                serializer.save()
                accidents_created.append(serializer.data)
            else:
                print("Erro no serializer:", serializer.errors)  # Mostra erros no terminal
        if not accident_data:
            return Response({"accidents": accidents_created}, status=status.HTTP_201_CREATED)

        return Response({"accidents": accidents_created}, status=status.HTTP_201_CREATED)
