from django.db import models

# Create your models here.

class Master_Table(models.Model):
    Email = models.EmailField(primary_key= True)
    Role = models.CharField(max_length = 50)
    Password = models.CharField(max_length = 20)
    Otp = models.IntegerField(default = 459)
    Is_Active = models.BooleanField(default=True)
    Is_Verfied = models.BooleanField(default=False)
    Created_At= models.DateTimeField(auto_now_add=True,blank=False)
    Updated_At = models.DateTimeField(auto_now = True, blank=False)

    def __str__(self):
        return '%s' % (self.Email)

class User(models.Model):
    User_Id = models.ForeignKey(Master_Table, on_delete= models.CASCADE)
    UserName = models.CharField(max_length=50)

class Service_Provider(models.Model):
    SP_Id = models.ForeignKey(Master_Table, on_delete= models.CASCADE)
    UserName = models.CharField(max_length=50) 

class Parts_Details(models.Model):
    Part_Image = models.ImageField(upload_to = 'image/', default= 'abc.jpg')
    Part = models.CharField(max_length= 50)
    Sub_Part = models.CharField(max_length= 50)
    Name = models.CharField(max_length= 150)
    Brand = models.CharField(max_length= 40)
    Price = models.CharField(max_length= 60)
    Fitment = models.CharField(max_length= 500)

class Part_Camshaft(models .Model):
    Bike_Name = models.CharField(max_length= 30)
    Bike_Model = models.CharField(max_length= 30)
    Price = models.CharField(max_length= 30)
    Availibility = models.CharField(max_length= 30)



