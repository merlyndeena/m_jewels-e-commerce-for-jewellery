from django.db import models
class category_db(models.Model):
    c_name=models.CharField(max_length=100,null=True,blank=True)
    c_img=models.ImageField(upload_to="Category",null=True,blank=True)
    c_desc=models.TextField(max_length=100,null=True,blank=True)
class product_db(models.Model):
    cat_name=models.CharField(max_length=100,null=True,blank=True)
    p_name=models.CharField(max_length=100,null=True,blank=True)
    p_mrp=models.CharField(max_length=100,null=True,blank=True)
    p_quan=models.CharField(max_length=100,null=True,blank=True)
    p_img=models.ImageField(upload_to="Products",null=True,blank=True)
    p_img1=models.ImageField(upload_to="Products",null=True,blank=True)
    p_desc=models.TextField(max_length=100,null=True,blank=True)
class product_database(models.Model):
    cat_name = models.CharField(max_length=100, null=True, blank=True)
    p_name = models.CharField(max_length=100, null=True, blank=True)
    p_mrp = models.CharField(max_length=100, null=True, blank=True)
    p_quan = models.CharField(max_length=100, null=True, blank=True)
    p_img = models.ImageField(upload_to="Products", null=True, blank=True)
    p_img1 = models.ImageField(upload_to="Products", null=True, blank=True)
    p_desc = models.TextField(max_length=100, null=True, blank=True)
