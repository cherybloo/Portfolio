from . import views
from django.urls import path

app_name = "showcase"

urlpatterns = [
    path('',views.home,name="home")
]