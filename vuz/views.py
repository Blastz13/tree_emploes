from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView

from django_filters import rest_framework as filters

from .serializers import (ListSubdivisionSerializer, 
                          ListEmploeSerializer, 
                          DetailEmploeSerializer)
from .models import Subdivision, Emploe


class ListSubdivision(ListAPIView):
    queryset = Subdivision.objects.all()
    serializer_class = ListSubdivisionSerializer
    filter_backends = (filters.DjangoFilterBackend,)

    def get_queryset(self):
        if self.request.GET.get('reverse') == 'True':
            return self.queryset.order_by('-title')
        return self.queryset.order_by('title')


class ListSubdivisionEmploe(ListAPIView):
    queryset = Emploe.objects.all()
    serializer_class = ListEmploeSerializer
    filter_backends = (filters.DjangoFilterBackend,)

    def get_queryset(self):
        if self.request.GET.get('reverse') == 'True':
            return Emploe.objects.filter(subdivision__id=self.kwargs.get('pk')).order_by('-name')
        return Emploe.objects.filter(subdivision__id=self.kwargs.get('pk')).order_by('name')


class DetailEmploe(RetrieveAPIView):
    queryset = Emploe.objects.all()
    serializer_class = DetailEmploeSerializer
    filter_backends = (filters.DjangoFilterBackend,)


class ListSubordinateEmploe(ListAPIView):
    queryset = Emploe.objects.all()
    serializer_class = ListEmploeSerializer
    filter_backends = (filters.DjangoFilterBackend,)

    def get_queryset(self):
        emploe = Emploe.objects.filter(id=self.kwargs.get('pk'))
        subordinate = emploe.get_descendants(include_self=False)
        return subordinate
