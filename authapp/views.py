from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from .models import *
from .util import *
from random import randint
from userapp.models import Master_Vehicle,User_Query
from userapp.views import ShowVehicle

# Create your views here.

# Redirecting to login, register forgot and index page
 
def Auth_Index(request):
    return render(request, 'authapp/auth_index.html')
 
def Auth_About(request):
    return render(request, 'authapp/auth_about.html')
 
def Auth_Services(request):
    return render(request, 'authapp/auth_services.html')

def Auth_Career(request):
    return render(request, 'authapp/auth_career.html')
  
def Auth_Contact(request):
    return render(request, 'authapp/auth_contact.html')
  
def LoginPage(request):
    return render(request, 'authapp/login.html')

def RegisterPage(request):
    return render(request, 'authapp/register.html')

def ForgotPage(request):
    return render(request, 'authapp/forgot.html')

def Parts(request):
    return render(request, 'authapp/parts.html')

def Engine_Parts(request):
    return render(request, 'authapp/parts_engine.html')

# User Registration
def Register(request):
    try:
        if request.POST['role'] == 'User':
            role = request.POST['role']
            username = request.POST['un']
            email = request.POST['em']
            password = request.POST['ps']
            c_password = request.POST['cps']

            user = Master_Table.objects.filter(Email=email)

            if user:
                message = 'This email already exists'
                return render(request, 'authapp/register.html', {'message':message})
            else:
                if password == c_password:
                    otp = randint(100000, 9999999)
                    new_master_user = Master_Table.objects.create(Email = email, Password = password, Role = role, Otp = otp)
                    new_user = User.objects.create(User_Id = new_master_user, UserName = username )
                    email_subject = 'Email confirmation'        
                    sendmail(email_subject, 'mail_template', email, {'name': username,'otp': otp}) 
                    message = 'Registration successful'
                    return render(request, 'authapp/login.html', {'message': message})
                else:
                    message = 'Password and confirm password does not match'
                    return render(request, 'authapp/register.html', {'message': message})
        elif request.POST['role'] == 'Service Provider':
            role = request.POST['role']
            username = request.POST['un']
            email = request.POST['em']
            password = request.POST['ps']
            c_password = request.POST['cps']
            
            user = Master_Table.objects.filter(Email=email)

            if user:
                message = 'This email already exists'
                return render(request, 'authapp/register.html', {'message':message})
            else:
                if password == c_password:
                    otp = randint(100000, 9999999)
                    new_master_sp= Master_Table.objects.create(Email = email, Password = password, Role = role, Otp = otp)
                    new_sp= Service_Provider.objects.create(SP_Id= new_master_sp,UserName=username)
                    email_subject = 'Email confirmation'        
                    sendmail(email_subject, 'mail_template', email, {'name': username,'otp': otp}) 
                    message = 'Registration successful'
                    return render(request, 'authapp/login.html', {'message':message})
                else:
                    message = 'Password and confirm password doesn\'t match'
                    return render(request, 'authapp/register.html', {'message': message})
    #except Exception as e:
        #message = 'Please select a role'
        #return render(request, 'authapp/register.html', {'message': message})     
    except Master_Table.DoesNotExist:
        message = 'This email already exists'
        return render(request, 'authapp/register.html', {'message': message})      
# User Login
def Login(request):
    try :
        if request.POST['role'] == 'User':
            email = request.POST['em']
            passsword = request.POST['ps']

            user = Master_Table.objects.get(Email=email)

            if user.Password == passsword and user.Role == 'User':
                get_user = User.objects.get(User_Id = user)
                request.session['Email'] = user.Email
                request.session['UserName'] = get_user.UserName
                request.session['Role'] = user.Role 
                otp = randint(100000, 9999999)
                sendmail('Login OTP', 'login_template', email, {'name':  request.session['UserName'], 'otp': otp}) 
                return render(request,'authapp/otp_validate.html',{'otp':otp, 'role': request.POST['role']})       
            else:
                message = "Incorrect password or user doesn't exist"
                return render(request, 'authapp/login.html', {'message':message})
        elif request.POST['role'] == 'Service Provider':
            email = request.POST['em']
            passsword = request.POST['ps']

            user = Master_Table.objects.get(Email= email)

            if user.Password == passsword and user.Role == 'Service Provider':
                get_sp = Service_Provider.objects.get(SP_Id = user)
                request.session['Email'] = user.Email
                request.session['UserName'] = get_sp.UserName
                request.session['Role'] = user.Role
                otp = randint(100000, 9999999)
                sendmail('Login OTP', 'login_template', email, {'name':  request.session['UserName'], 'otp': otp}) 
                return render(request,'authapp/otp_validate.html',{'otp':otp, 'role': request.POST['role']})          
            else:
                message = "Incorrect password or user doesn't exist"
                return render(request, 'authapp/login.html', {'message':message})
        else:
            message = "User does not exist"
            return render(request, 'authapp/login.html', {'message':message})
    #except Exception as e:
        #message = 'Please select a role'
        #return render(request, 'authapp/login.html', {'message': message})
    except Master_Table.DoesNotExist:
        message = 'This email already exists'
        return render(request, 'authapp/register.html', {'message': message}) 

# forgot Password
def Forgot(request):  
    email = request.POST['em']
    password = request.POST['ps']
    c_password = request.POST['cps']
    try:
        edituser = Master_Table.objects.get(Email=email)
        if edituser:
            if edituser.Email == email:
                if password == c_password:
                    edituser.Password = request.POST['ps']
                    edituser.save()
                    return render(request, 'authapp/login.html')
                else:
                    message = 'Password and confirm password doesn\'t match'
                    return render(request, 'authapp/forgot.html', {'message': message})
            else:
                message = 'This email does not match'
                return render(request, "authapp/forgot.html", {'message': message})
        else:
            message = 'This email is not available'
            return render(request, "authapp/forgot.html", {'message': message})
    except Exception as e:
        message = 'Complete details'
        return render(request, "authapp/forgot.html", {'message': message})

def OTP_Validate(request, otp, role):
    otp= request.POST['otp']
    if otp == otp:
        if role == 'Service Provider':
            return redirect('/providerapp/')
        elif role == 'User':
            return redirect('/userapp/')

def CustomerQuery(request):
    name= request.POST['name']
    email= request.POST['email']
    subject= request.POST['subject']
    message= request.POST['message']

    user_query= User_Query.objects.create(User_Name= name, Email= email, Subject= subject, Message= message)
    
    return render(request, 'authapp/auth_contact.html')

def Camshaft_Details(request):
    part_det= Parts_Details.objects.filter(Sub_Part= "Camshafts")
    return render(request,'authapp/show_parts.html', {'parts': part_det} )
  
def BuyParts(request):
     return render(request,'authapp/buy_parts.html')

def FindParts(request):

    parts = Part_Camshaft.objects.get(Bike_Model= request.GET['model'])
    message = "Scroll down to see your selection"
    return render(request, 'authapp/buy_parts.html', {'parts_details': parts, 'message':  message})

def Payment(request):
    return render(request, 'authapp/payment.html') 
