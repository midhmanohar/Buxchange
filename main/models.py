from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class Student(models.Model):
    username = models.ForeignKey(User,on_delete = models.CASCADE)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex],max_length=15,blank = True)

class Branch(models.Model):
    name = models.CharField(max_length=50)
class Semester(models.Model):
    values = models.CharField(max_length=20)

class Books(models.Model):
    name = models.CharField(max_length=100)
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester,on_delete=models.CASCADE)
    upload_id = models.ForeignKey(User,on_delete=models.CASCADE)
    book_url = models.ImageField(upload_to='images/',blank=True,null=True)






