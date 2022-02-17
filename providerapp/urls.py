from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name= 'Index'),
    path('GarageDetails/', views.AddGarageDetails, name= 'AddGarageDetails'),
    path('My_Request/', views.Request_Handle, name="Request_Handle"),
    path('Request/<int:req_id>/', views.Request_Handle, name="Request_Handle"),
    path('LogOut/', views.LogOut, name="LogOut"),
    path('UserQuery', views.UserQuery, name="UserQuery"),
]