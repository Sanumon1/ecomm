from django.db import models
from base.models import BaseModel

# Create your models here.

class category(BaseModel):
    category_name=models.CharField(max_length=100)
    category_image=models.ImageField(upload="catogoriescd")

class product(BaseModel):
    product_name = models.CharField(max_length=100)
    category =models.ForeignKey(category,on_delete= models.CASCADE,related_name="products")
    price = models.IntegerField()
    product_descreption=models.TextField()

class productImage(BaseModel):
    product = models.ForeignKey(product,on_delete=models.CASCADE,related_name="product_images")
    image = models.ImageField(upload="product")
