from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Student(models.Model):
    StudentNumber = models.CharField(primary_key=True,max_length=11,null=False, blank=False, validators=[
        MinLengthValidator(11, 'Name must have atleast 3 charactors')
    ])
    
    Firstname = models.CharField(max_length=150,null=False, blank=False, validators=[
        MinLengthValidator(3, 'Name must have atleast 3 charactors')
    ])

    MiddleName = models.CharField(max_length=150,null=True, blank=True, validators=[
        MinLengthValidator(3, 'Name must have atleast 3 charactors')
    ])

    LastName = models.CharField(max_length=150,null=False, blank=False, validators=[
        MinLengthValidator(3, 'Name must have atleast 3 charactors')
    ])

    photo = models.ImageField(upload_to ='uploads/')

