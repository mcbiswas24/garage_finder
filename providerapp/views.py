from django.shortcuts import render, redirect
from .models import *
from authapp.models import Master_Table, Service_Provider, User
from userapp.models import Request_Details, User_Query
from .util import *

# Page rendering
def Index(request):
   return My_Request(request)


# Adding garage details
def AddGarageDetails(request):
    gname= request.POST['gname']
    gaddress= request.POST['gaddress']
    gcity= request.POST['gcity']
    gmobileno= request.POST['gmobileno']
    gimage= request.FILES['gimage']
    sp_id= Master_Table.objects.get(Email= request.session['Email'])

    if "general_service" in request.POST:
        serv1= "General Service"
        serv1_price= request.POST['general_service_price']
    else:
        serv1= ""
        serv1_price= 0
    if "electrical_issue" in request.POST:
        serv2= "Electrical Issue"
        serv2_price= request.POST['electrical_issue_price']
    else:
        serv2= ""
        serv2_price= 0
    if "engine/silencer_noise" in request.POST:
        serv3= "Engine/Silencer Noise"
        serv3_price= request.POST['engine/silencer_noise_price']
    else:
        serv3= ""
        serv3_price= 0
    if "repainting/scratch_removal" in request.POST:
        serv4= "Repainting/Scratch Removal"
        serv4_price= request.POST['repainting/scratch_removal_price']
    else:
        serv4= ""
        serv4_price= 0
    if "oil_changing" in request.POST:
        serv5= "Oil Changing"
        serv5_price= request.POST['oil_changing_price']
    else:
        serv5= ""
        serv5_price= 0
    if "tyre_puncture/replacement" in request.POST:
        serv6= "Tyre puncture/Replacement"
        serv6_price= request.POST['tyre_puncture/replacement_price']
    else:
        serv6= ""
        serv6_price= 0

    if "chain_and_spocket_issue" in request.POST:
        serv7= "Chain and Spocket Issue"
        serv7_price= request.POST['chain_and_spocket_issue_price']
    else:
        serv7= ""
        serv7_price= 0


    pro_name= Service_Provider.objects.filter(SP_Id= sp_id).first()

    new_garage= GarageDetails.objects.create(
        Gname= gname, 
        Gaddress= gaddress,
        City= gcity,
        Mobile_No= gmobileno,
        Gimage=  gimage,
        Provider_Name= pro_name.UserName,
        SP_ID= sp_id,
        Ser1= serv1, 
        Ser2= serv2, 
        Ser3= serv3, 
        Ser4= serv4, 
        Ser5= serv5, 
        Ser6= serv6, 
        Ser7= serv7, 
        Ser1_Price= serv1_price,
        Ser2_Price= serv2_price,
        Ser3_Price= serv3_price,
        Ser4_Price= serv4_price,
        Ser5_Price= serv5_price,
        Ser6_Price= serv6_price,
        Ser7_Price= serv7_price,   
        )

    return render(request,'providerapp/index_pro.html')



# Request Handling

def My_Request(request): # retrieving provider specific request
    username= Service_Provider.objects.get(SP_Id= request.session['Email'])
    my_request= Request_Details.objects.filter(Provider_ID= request.session['Email'])

    return render(request, 'providerapp/index_pro.html', {'requests': my_request, 'name': username.UserName })


def Request_Handle(request,req_id): # accepting or deleting request
    user_req= Request_Details.objects.get(id= req_id)
    user_det= User.objects.get(UserName= user_req.User_Name)
    provider_det= Service_Provider.objects.get(SP_Id= user_req.Provider_ID)
    username= user_det.UserName
    useremail= str(user_det.User_Id)
    providername= provider_det.UserName
    #email= user_det.User_Id
    if "accept" in request.POST:
        sendmail('Request Accepted','request_accept',useremail, {'u_name': username, 'pro_name': providername} ) 
    elif "reject" in request.POST:
        req= Request_Details.objects.get(id= req_id)
        req.delete()
        sendmail('Request Rejected', 'request_reject', useremail, {'pro_name': providername, 'u_name': username}) 

    return My_Request(request)
    #sendmail('Urgent service needed','service_need',provider_id, {'name':  request.session['UserName'],'pro_name': providername.UserName})

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






