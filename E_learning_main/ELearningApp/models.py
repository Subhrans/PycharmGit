from django.db import models
from django.utils import timezone

# Create your models here.

secondaryExaminationBoard=(
    ('1',"WBBSE"),
    ('2','BBSE'),
    ('3','DBSE'),
)

class Onwer(models.Model):
    Onwer_name=models.CharField(max_length=128)
    Onwer_contact_number=models.IntegerField()
    Onwer_address=models.TextField(max_length=500)
    Onwer_ID=models.CharField(max_length=500)

    def __str__(self):
        return self.Onwer_name
    def OwnerValid(self):
        pass

class Organization(models.Model):
    Organization_name = models.CharField(max_length=128)
    Organization_ragistration_number=models.CharField(max_length=128)
    Organization_contact_number=models.BigIntegerField()
    Organization_address=models.TextField(max_length=500)
    Organization_number_of_employee=models.IntegerField(default=0)
    Established_date=models.DateField()
    Owner_details = models.ForeignKey(Onwer, on_delete=models.CASCADE)
    created_date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.Organization_name

    def OrganizationValid(self):
        pass

class Teacher(models.Model):
    Teacher_name=models.CharField(max_length=128)
    TID=models.CharField(max_length=128,default="19MCA1027")
    Teacher_permanent_address=models.TextField(max_length=500)
    Teacher_residential_address = models.TextField(max_length=500)
    Secondary_examination=models.CharField(max_length=128,choices=secondaryExaminationBoard)

    def __str__(self):
        return self.Teacher_name
