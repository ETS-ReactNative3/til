from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer

class CursoAPIView(APIView):
  """
  API de Crusos da Geek
  """
  def get(self, request):
    cursos = Curso.objects.all()
    serializers = CursoSerializer(cursos, many=True)
    return Response(serializers.data)


class AvaliacaoAPIView(APIView):
  """
  API de Avaliações da Geek
  """
  def get(self, request):
    avaliacoes = Avaliacao.objects.all()
    serializers = AvaliacaoSerializer(avaliacoes, many=True)
    return Response(serializers.data)