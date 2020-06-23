from django.contrib import admin
from django.urls import path
from .views import (ListSubdivision, ListSubdivisionEmploe, 
                    DetailEmploe, ListSubordinateEmploe)


urlpatterns = [
    path('list-subdivision/', ListSubdivision.as_view()),
    path('list-subdivision-emploe/<int:pk>', ListSubdivisionEmploe.as_view()),
    path('detail-emploe/<int:pk>', DetailEmploe.as_view()),
    path('detail-emploe/<int:pk>/subordinate', ListSubordinateEmploe.as_view())
]
