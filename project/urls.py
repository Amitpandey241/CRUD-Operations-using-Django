from django.urls import path 
from . import views 

urlpatterns = [
    path('',views.homeView,name="home"),
    path('project/<str:pk>/', views.projectView,name="project"),
    path('create-project/',views.createView,name="create-project"),
    path('update-project/<str:pk>/',views.updateView, name="update-project"),
    path('delete-project/<str:pk>/',views.deleteView,name="delete-project"),
]
