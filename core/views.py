from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Accident
from .serializers import AccidentSerializer

class AccidentView(APIView):
    def post(self, request, *args, **kwargs):
        accident_data = request.data.get("data", {}).get("accidents", {}).get("items", [])

        if not accident_data:
            return Response({"error": "Nenhum acidente encontrado"}, status=status.HTTP_400_BAD_REQUEST)

        accidents_created = []
        for accident in accident_data:
            serializer = AccidentSerializer(data=accident)
            if serializer.is_valid():
                serializer.save()
                accidents_created.append(serializer.data)
        
        return Response({"accidents": accidents_created}, status=status.HTTP_201_CREATED)
