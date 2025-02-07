from django.urls import path
from .views import AccidentView

urlpatterns = [
    path('accidents/', AccidentView.as_view(), name='accidents'),
]
