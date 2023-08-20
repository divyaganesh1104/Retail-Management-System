from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser
# Create your models here.
class AuthUser(AbstractUser):
    is_admin = models.BooleanField('Is admin',default=False)
    is_manager = models.BooleanField('Is manager', default=False)
    is_salesperson = models.BooleanField('Is salesperson', default=False)

class Customer(models.Model):
    custom_id = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    custom_contact = models.CharField(max_length=200)
    custom_add = models.TextField()
    def __str__(self):
        return self.custom_id

class Supplier(models.Model):
    supplier_id = models.CharField(max_length=100, unique=True)
    supplier_name = models.CharField(max_length=100)
    supplier_phone = models.CharField(max_length=200)
    supplier_email = models.EmailField(max_length=200, null=True)
    supplier_add = models.TextField(null=True)


class Product_cls(models.Model):
    product_cls_id = models.CharField(max_length=100, unique=True)
    product_cls_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.product_cls_id}'


class Product(models.Model):
    product_id = models.CharField(max_length=100, unique=True, null=True)
    product_name = models.CharField(max_length=100)
    product_product_cls = models.ForeignKey(Product_cls, on_delete=models.CASCADE, null=True, related_name='productClass')
    def __str__(self):
        return f'{self.product_id}'


class Item_cls(models.Model):
    CHOICE_YES = 'Yes'
    CHOICE_NO = 'No'
    PACK_CHOICES = [
        (CHOICE_YES, 'Yes'),
        (CHOICE_NO, 'No')
    ]
    SAME_CHOICES = [
        (CHOICE_YES, 'Yes'),
        (CHOICE_NO, 'No')
    ]

    item_cls_id = models.CharField(max_length=100, unique=True)
    item_cls_name = models.CharField(max_length=100)
    item_product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    packed = models.CharField(max_length=5, choices=PACK_CHOICES, default=CHOICE_NO)
    same = models.CharField(max_length=20, choices=SAME_CHOICES,null=True,blank=True)
    no_of_diff = models.IntegerField(null=True,blank=True)
    qty = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return f'{self.item_cls_id}'


class Purchase(models.Model):
    purchase_id = models.CharField(max_length=100)
    supplier_id = models.CharField(max_length=100)
    bill_no = models.CharField(max_length=100, unique=True)
    date = models.DateField()
    def __str__(self):
        return self.purchase_id

class Purchase2(models.Model):
    purchase_id = models.CharField(max_length=100, null=True)
    purchase_item_cls = models.CharField(max_length=200, null=True)
    quantity = models.IntegerField(null=True)
    rate = models.IntegerField()

class ItemStock(models.Model):
    item_cls_id = models.CharField(max_length=100)
    quantity = models.IntegerField()
    def __str__(self):
        return self.item_cls_id
class ItemStatus(models.Model):
    PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]
    item_id = models.CharField(max_length=100)
    item_cls_status_id = models.ForeignKey(Item_cls, on_delete=models.CASCADE)
    barcode = models.ImageField(upload_to='images/', blank=True)
    sales_status = models.CharField(max_length=100)
    purchase_rate = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount = models.IntegerField(validators=PERCENTAGE_VALIDATOR, default=0)
    image = models.CharField(max_length=100, default='image not found')
    purchase_id= models.ForeignKey(Purchase, on_delete=models.CASCADE, null=True)
    status_qty = models.IntegerField(null=True)
class ItemClsDiffer(models.Model):
    item_cls_id = models.ForeignKey(Item_cls, on_delete=models.CASCADE, null=True, blank=True)
    item_cls_differ_id = models.CharField(max_length=100)
    specification = models.CharField(max_length=100)
class SaleEntry(models.Model):
    sale_id = models.CharField(max_length=100, null=True)
    sell_date = models.DateField(null=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    def __str__(self):
        return self.sale_id
class Sale(models.Model):
    sale_id = models.ForeignKey(SaleEntry, on_delete=models.CASCADE, null=True)
    sales_item_id = models.CharField(max_length=100)
    item_name = models.ForeignKey(Item_cls, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()
    rate=models.DecimalField(max_digits=10, decimal_places=2)

