from django.shortcuts import render, HttpResponse, redirect
from .models import *
from authapp.models import Master_Table, Service_Provider,User
from providerapp.models import GarageDetails
from .util import *

# Create your views here.

def IndexPage(request):
    return ShowVehicle(request)

def LogOut(request):
   del request.session['Email'] 
   del request.session['UserName']
   del request.session['Role']

   return redirect('/authapp/')


def UserQuery(request):
    name= request.POST['name']
    email= request.POST['email']
    subject= request.POST['subject']
    message= request.POST['message']

    user_query= User_Query.objects.create(User_Name= name, Email= email, Subject= subject, Message= message)
    
    return render(request, 'userapp/contact.html')

def AddVehicle(request):
    vname= request.POST['vname']
    vmodel= request.POST['vmodel']
    vtype= request.POST['vtype']
    vnumber= request.POST['vnumber']
    vcolor= request.POST['vcolor']
    vimage= request.FILES['vimage']
    user_id= Master_Table.objects.get(Email= request.session['Email'])

    new_master_vehicle= Master_Vehicle.objects.create(
        Vname= vname, 
        Vmodel= vmodel, 
        Vtype= vtype, 
        Vnumber= vnumber, 
        Vcolor= vcolor, 
        Vimage= vimage,
        User_ID= user_id
    )


    new_vehicle= User_Vehicle.objects.create(
        Vname= vname, 
        Vmodel= vmodel, 
        Vtype= vtype,
        Vcolor= vcolor, 
        Vimage= vimage,
        Vehicle_ID= new_master_vehicle
        )

    return ShowVehicle(request)

def ShowVehicle(request):
    username= User.objects.get(User_Id= request.session['Email'])
    vehicle_details= Master_Vehicle.objects.filter(User_ID= request.session['Email'])
    return render(request, 'userapp/index.html',{'keys': vehicle_details, 'name': username})

def General_Service(request):
    provider_details= GarageDetails.objects.filter(Ser1= "General Service")
    return render(request,'userapp/show_provider.html',{'keys': provider_details})

def Oil_Changing(request):
    provider_details= GarageDetails.objects.filter(Ser2= "Oil Changing")
    return render(request,'userapp/show_provider.html',{'keys': provider_details})

def Electrical_Issue(request):
    provider_details= GarageDetails.objects.filter(Ser3= "Electrical Issue")
    return render(request,'userapp/show_provider.html',{'keys': provider_details})

def Engine_silencer_Noise(request):
    provider_details= GarageDetails.objects.filter(Ser4= "Engine/silencer Noise")
    return render(request,'userapp/show_provider.html',{'keys': provider_details})

def Repainting_Scratch_Removal(request):
    provider_details= GarageDetails.objects.filter(Ser5= "Repainting/Scratch removal")
    return render(request,'userapp/show_provider.html',{'keys': provider_details})

def Tyre_Puncture_Replacement(request):
    provider_details= GarageDetails.objects.filter(Ser6= "Tyre Puncture/Replacement")
    return render(request,'userapp/show_provider.html',{'keys': provider_details})

def Chain_Spocket_Issue(request):
    provider_details= GarageDetails.objects.filter(Ser7= "Chain and Spocket Issue")
    return render(request,'userapp/show_provider.html',{'keys': provider_details})

def All(request):
    provider_details= GarageDetails.objects.all()
    return render(request,'userapp/show_provider.html',{'keys': provider_details})

def Request_Details_Fill(request,sp_id):
    request.session['pro_id']= sp_id
    return render(request,'userapp/request.html')     

def Store_Request(request):
    v_id= request.POST['vno']
    city= request.POST['city']
    username= User.objects.get(User_Id= request.session['Email'])
    provider_id= request.session['pro_id']
    if 'urgent' in request.POST:
        need= "urgent"
        providername= Service_Provider.objects.get(SP_Id= provider_id)
        sendmail('Urgent service needed','service_need',provider_id, {'name':  request.session['UserName'],'pro_name': providername.UserName})
        
    elif 'wait' in request.POST:
        need= "wait"

    new_request= Request_Details.objects.create(
        User_Name= username.UserName,
        City= city,
        Need= need,
        Vehicle_ID= v_id,
        Provider_ID= provider_id
    )
    message= "Request has been sent"
    return render(request,'userapp/request.html',{'message': message})