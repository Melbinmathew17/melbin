from django.urls import path
from webapp2 import views

urlpatterns=[
path('homepage/',views.homepage,name="homepage"),
path('playerspage/<catg>/',views.playerspage,name="playerspage"),
path('singleplayer/<int:dataid>/',views.singleplayer,name="singleplayer"),

]