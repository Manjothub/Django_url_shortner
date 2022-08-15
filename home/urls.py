from django.urls import path,include
from home.views import *

urlpatterns = [
    path('',INDEX,name="index"),
    path('geturl',URLSHORTNER,name="urlshortner")
] 