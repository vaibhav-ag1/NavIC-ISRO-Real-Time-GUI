from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name="index"),
    path("map/<int:x>/<int:y>",views.map,name="map"),
    path("realtime",views.realtime,name="realtime"),
    path("team",views.team,name="team")
]