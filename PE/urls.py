
from django.urls import path
from . import  views
urlpatterns = [

    path('PE',views.PeHome,name='PEHome'),
]
