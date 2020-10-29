import time
from django.db import models
from mptt import models as mptt_models

def upload_product_img(instance,filename):
    lastDot = filename.rfind('.')
    extension = filename[lastDot:len(filename):1]
    return 'images/product/%s-%s-%s' % (instance.slug,time.time(),extension)

# Create your models here.
class Category(mptt_models.MPTTModel):
    category_name = models.CharField(max_length=255)
    parent = mptt_models.TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    slug = models.SlugField(max_length=500, unique=True)

    class MPTTMeta:
        order_insert_by=['name']

    def __str__(self):
        return self.category_name

class Characteristic(models.Model):
    manufacturer = models.CharField(max_length=500)
    weight = models.IntegerField()
    color = models.CharField(max_length=255)
    model = models.CharField(max_length=255)

    def __str__(self):
        return self.model

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_description = models.TextField()
    product_price = models.IntegerField()
    product_image = models.FileField(upload_to=upload_product_img)
    product_count = models.IntegerField()
    product_sale = models.IntegerField()
    is_featured = models.BooleanField(default=False)
    publish_date= models.DateField()
    categories = mptt_models.TreeManyToManyField(Category,related_name='products')
    slug = models.SlugField(max_length=500)
    characteristic = models.OneToOneField(Characteristic, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name



