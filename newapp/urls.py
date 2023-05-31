from django.urls import path
from newapp import views

urlpatterns=[
    path('indexpage/',views.indexpage,name="indexpage"),
    path('positionpage/',views.positionpage,name="positionpage"),
    path('saveposition/',views.saveposition,name="saveposition"),
    path('displaypage/',views.displaypage,name="displaypage"),
    path('editposition/<int:dataid>/',views.editposition,name="editposition"),
    path('updateposition/<int:dataid>/',views.updateposition,name="updateposition"),
    path('deleteposition/<int:dataid>/',views.deleteposition,name="deleteposition"),
    path('playerpage/',views.playerpage,name="playerpage"),
    path('saveplayer/',views.saveplayer,name="saveplayer"),
    path('displayplayer/',views.displayplayer,name="displayplayer"),
    path('editplayer/<int:dataid>/',views.editplayer,name="editplayer"),
    path('updateplayer/<int:dataid>/',views.updateplayer,name="updateplayer"),
    path('deleteplayer/<int:dataid>/',views.deleteplayer,name="deleteplayer"),
    path('adminpage/',views.adminpage,name="adminpage"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('adminlogout/',views.adminlogout,name="adminlogout"),

]