from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name = "index"),
    path("jamie",views.jamie, name = "jamie"),
    path("<str:name>", views.greet, name = "greet")

    ]