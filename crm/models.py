from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=200)
    department=models.CharField(max_length=120)
    options=(
        ('male','male'),
        ('female','female')
    )
    gender=models.CharField(max_length=200,choices=options,default='female')
    salary=models.PositiveIntegerField()
    email=models.EmailField()
    profile_pic=models.ImageField(upload_to='images',null=True,blank=True)
    address=models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.name

