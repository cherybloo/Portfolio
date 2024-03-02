from . import views
from django.urls import path

app_name = "showcase"

urlpatterns = [
    path('',views.home,name="home"),
    path('project2',views.project2,name="project2"),
    path('project3',views.project3,name="project3")
]
