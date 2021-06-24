from django.db import models

class Product(models.Model):
    product_img=models.CharField(max_length=10000)
    product_id = models.CharField(max_length=100)
    product_name = models.CharField(max_length=30)
    product_price = models.CharField(max_length=100)
    product_manu = models.CharField(max_length=30)
    class Meta:
        db_table="product_details"

class Deleted(models.Model):
    product_img=models.CharField(max_length=10000)
    product_id = models.CharField(max_length=100)
    product_name = models.CharField(max_length=30)
    product_price = models.CharField(max_length=100)
    product_manu = models.CharField(max_length=30)
    class Meta:
        db_table="deleted_details"    
 
