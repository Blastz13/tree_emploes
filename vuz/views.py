from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from django_filters import rest_framework as filters

from .serializers import (ListSubdivisionSerializer, 
                          ListEmploeSerializer, 
                          DetailEmploeSerializer)
from .models import Subdivision, Emploe, Position


class ListSubdivision(ListAPIView):
    queryset = Subdivision.objects.all()
    serializer_class = ListSubdivisionSerializer
    filter_backends = (filters.DjangoFilterBackend,)

    def get_queryset(self):
        if self.request.GET.get('reverse') == 'True':
            return self.queryset.order_by('-title')
        return self.queryset.order_by('title')


class ListSubdivisionEmploe(APIView):
    def get(self, request, pk):
        subdivision = Subdivision.objects.get(id=pk)

        if self.request.GET.get('reverse') == 'True':
            emploes_subdivision = Emploe.objects.filter(subdivision=subdivision).order_by('-name')
        else:
            emploes_subdivision = Emploe.objects.filter(subdivision=subdivision).order_by('name')

        serializer = ListEmploeSerializer(emploes_subdivision, many=True)
        return Response(serializer.data)


class DetailEmploe(RetrieveAPIView):
    queryset = Emploe.objects.all()
    serializer_class = DetailEmploeSerializer
    filter_backends = (filters.DjangoFilterBackend,)


class ListSubordinateEmploe(APIView):
    def get(self, request, pk):
        position_subordinate = Position.objects.filter(parent=Emploe.objects.get(id=pk).position_id)
        emploes_subordinate = Emploe.objects.filter(position__in=position_subordinate)
        serializer = ListEmploeSerializer(emploes_subordinate, many=True)
        return Response(serializer.data)
