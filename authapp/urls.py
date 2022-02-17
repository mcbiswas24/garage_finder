from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.Auth_Index, name='Auth_Index'),
    path('About/', views.Auth_About, name='Auth_About'),
    path('Services/', views.Auth_Services, name='Auth_Services'),
    path('Career/', views.Auth_Career, name='Auth_Career'),
    path('Contact/', views.Auth_Contact, name='Auth_Contact'),
    path('login/', views.LoginPage, name='LoginPage'),
    path('register/',views.RegisterPage, name='RegisterPage'),
    path('forgot password/', views.ForgotPage, name= 'ForgotPage'),
    path('Register/', views.Register, name='Register'),
    path('Login/', views.Login, name= 'Login'),
    path('Forgot/', views.Forgot, name='Forgot'),
    path('OTP_Validate/<int:otp>/<str:role>', views.OTP_Validate, name='OTP_Validate'),
    path('CustomerQuery/', views.CustomerQuery, name='CustomerQuery'),
    path('Parts/', views.Parts, name='Parts'),
    path('Engine_Parts/', views.Engine_Parts, name='Engine_Parts'),
    path('Camshaft/',views.Camshaft_Details,name= 'Camshaft_Details'),
    path('BuyParts/', views.BuyParts, name= 'BuyParts'),
    path('FindParts/', views.FindParts, name= 'FindParts'),
     path('Payment/', views.Payment, name= 'Payment'),
]
