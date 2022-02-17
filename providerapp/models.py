from django.db import models
from authapp.models import Master_Table

# Create your models here.

class GarageDetails(models.Model):
    Gimage= models.ImageField(upload_to = 'image/', default= 'abc.jpg')
    Gname= models.CharField(max_length= 25)
    Gaddress= models.CharField(max_length= 254)
    City= models.CharField(max_length= 10)
    Mobile_No= models.CharField(max_length= 10)
    Ser1= models.CharField(max_length= 25)
    Ser1_Price=  models.CharField(max_length= 25)
    Ser2= models.CharField(max_length= 25)
    Ser2_Price=  models.CharField(max_length= 25)
    Ser3= models.CharField(max_length= 25)
    Ser3_Price=  models.CharField(max_length= 25)
    Ser4= models.CharField(max_length= 25)
    Ser4_Price=  models.CharField(max_length= 25)
    Ser5= models.CharField(max_length= 25)
    Ser5_Price=  models.CharField(max_length= 25)
    Ser6= models.CharField(max_length= 25, default= 'none')
    Ser6_Price=  models.CharField(max_length= 25, default= 'none')
    Ser7= models.CharField(max_length= 25, default= 'none')
    Ser7_Price=  models.CharField(max_length= 25, default= 'none')

    Provider_Name= models.CharField(max_length= 50, default= "abc")
    SP_ID= models.ForeignKey(Master_Table, on_delete= models.CASCADE, default= "abc@gmail.com")


