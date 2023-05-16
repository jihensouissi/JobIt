
from django.urls import path
from . import  views
urlpatterns = [

    path('',views.home,name='home'),
    path('about-us.html',views.aboutus,name='About-us'),
]
