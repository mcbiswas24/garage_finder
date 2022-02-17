from django.db import models
from authapp.models import Master_Table

# Create your models here.
class User_Query(models.Model):
    User_Name= models.CharField(max_length= 20)
    Email= models.EmailField()
    Subject= models.CharField(max_length= 30)
    Message= models.CharField(max_length= 50)

class Master_Vehicle(models.Model):
    Vimage= models.ImageField(upload_to = 'image/', default= 'abc.jpg')
    Vname= models.CharField(max_length= 20)
    Vmodel= models.CharField(max_length= 20)
    Vtype= models.CharField(max_length= 20)
    Vnumber= models.CharField(max_length= 20, primary_key= True)
    Vcolor= models.CharField(max_length= 20)
    User_ID= models.ForeignKey(Master_Table, on_delete= models.CASCADE, default= "abc@gmail.com")

class User_Vehicle(models.Model):
    Vimage= models.ImageField(upload_to = 'image/', default= 'abc.jpg')
    Vname= models.CharField(max_length= 20)
    Vmodel= models.CharField(max_length= 20)
    Vtype= models.CharField(max_length= 20)
    Vcolor= models.CharField(max_length= 20)
    Vehicle_ID= models.ForeignKey(Master_Vehicle, on_delete= models.CASCADE, default= "")

class Request_Details(models.Model):
    User_Name= models.CharField(max_length= 30)
    Provider_ID= models.CharField(max_length= 254,default= "abc@gmail.com")
    City= models.CharField(max_length= 30)
    Need= models.CharField(max_length= 30)
    Vehicle_ID= models.CharField(max_length= 30)


