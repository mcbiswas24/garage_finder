from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexPage, name= 'IndexPage'),
    path('LogOut/',views.LogOut, name= 'LogOut'),
    path('user_query/', views.UserQuery, name= 'UserQuery'),  
    path('AddVehicle/', views.AddVehicle, name= 'AddVehicle'), 
    path('ShowVehicle/',views.ShowVehicle, name= 'ShowVehicle'),
    path('Request_Details_Fill/<str:sp_id>/', views.Request_Details_Fill, name= 'Request_Details_Fill'),
    path('Store_Request/', views.Store_Request, name= 'Store_Request'),   
    path('General_Service/', views.General_Service, name= 'General_Service'),   
    path('Oil_Changing/', views.Oil_Changing, name= 'Oil_Changing'),   
    path('Electrical_Issue/', views.Electrical_Issue, name= 'Electrical_Issue'),   
    path('Engine_silencer_Noise/', views.Engine_silencer_Noise, name= 'Engine_silencer_Noise'),   
    path('Repainting_Scratch_Removal/', views.Repainting_Scratch_Removal, name= 'Repainting_Scratch_Removal'),   
    path('Tyre_Puncture_Replacement/', views.Tyre_Puncture_Replacement, name= 'Tyre_Puncture_Replacement'),   
    path('Chain_Spocket_Issue/', views.Chain_Spocket_Issue, name= 'Chain_Spocket_Issue'),   
    path('All/', views.All, name= 'All'),   
 
]