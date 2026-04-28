from django.db import models

# Create your models here.
class contact_db(models.Model):
    c_name=models.CharField(max_length=100,null=True,blank=True)
    c_email=models.CharField(max_length=100,null=True,blank=True)
    c_msg=models.CharField(max_length=100,null=True,blank=True)
class save_signup(models.Model):
    s_name=models.CharField(max_length=100,null=True,blank=True)
    s_email=models.CharField(max_length=100,null=True,blank=True)
    s_pass=models.CharField(max_length=100,null=True,blank=True)
    s_repass=models.CharField(max_length=100,null=True,blank=True)
